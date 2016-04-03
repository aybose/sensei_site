import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
import re
from parse_data_to_db import *

app = Flask(__name__)

# TODO: select config based on environment
app.config.from_object('config.BaseConfig')
app.config['DEBUG'] = True

# Define the database object to be imported by models and controllers
db = SQLAlchemy(app)

from models import *

# DB METHODS #

@app.route('/create_school')
def create_school():
    school_name = "Wildflower"
    school = School(school_name)
    db.session.add(school)
    db.session.commit()
    return 'Created school with id=%s!' % school.id

@app.route('/create_new_teacher')
def create_new_teacher():
    teacher_name = "mary"
    school_name = "Wildflower"
    teacher_obj = Teacher(teacher_name)
    db.session.add(teacher_obj)
    school_obj = School.query.filter_by(school=school_name)[0]
    school_obj.teachers.append(teacher_obj)
    db.session.commit()
    return 'Created teacher with name=%s' % teacher_name

@app.route('/create_new_user')
def create_new_user():
    username = "mary"
    password = "mary"
    if Teacher.query.filter_by(name=username).first() is not None:
        user_obj = User(username, password)
        db.session.add(user_obj)
        db.session.commit()
    else:
        return "Not a valid teacher name"
    return 'Created user with name=%s!' % user_obj.username

@app.route('/create_new_students')
def create_new_students():
    school_name = "Wildflower"
    student_obj = Student("Uriah", 0)
    db.session.add(student_obj)
    school_obj = School.query.filter_by(school=school_name).first()
    school_obj.students.append(student_obj)
    db.session.commit()
    return 'Created student with name=%s!' % student_obj.name

@app.route('/view_data')
def view_data():
    to_view = ""
    schools= School.query.order_by(School.id)
    to_view = to_view + "\n Schools: "
    for school in schools:
        to_view = to_view + "\n" + school.school
    teachers = Teacher.query.order_by(Teacher.school_id)
    to_view = to_view + ",\n Teachers: "
    for teacher in teachers:
        to_view = to_view + "\n" + teacher.name 
    students = Student.query.order_by(Student.sensor_id)
    to_view = to_view + ",\n Students: "
    for student in students:
        to_view = to_view + "\n" + student.name 
    return to_view

@app.route('/parse_data')
def parse_data_inputs():
    parse_data('Wildflower', '03-28-16')
    data = SocialProximity.query.all()
    return render_template('data.html', data=data)

# TEMPLATES #

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if session.get('logged_in'):
         return redirect(url_for('home'))
    if request.method == 'POST':
        usernames = User.query.filter_by(username=request.form['username']).first()
        if usernames is None:
            error = "Invalid username"
        else:
            users = User.query.filter_by(username=request.form['username'], password=request.form['password']).first()
            if users is None:
                error = "Invalid password"
            else:
                session['logged_in'] = True
                session['username'] = request.form['username']
                flash('You were logged in')
                return redirect(url_for('home'))
        return render_template('index.html', error=error)
    return render_template('index.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('login'))

@app.route("/home")
def home():
    school_id = Teacher.query.filter_by(name=session['username']).first().school_id
    school_name = School.query.filter_by(id=school_id).first().school
    return render_template('home.html', school=school_name)

@app.route("/customize_updates")
def customize_updates():
    return render_template('customize_updates.html')

@app.route('/students_demo')
def students_demo():
    return render_template('students_demo.html')

@app.route('/matrix_total')
def matrix_total():
    return render_template('matrix_total.html')

@app.route('/matrix')
def matrix():
    return render_template('matrix.html')

@app.route('/bar_graph')
def bar_graph():
    return render_template('bar_graph.html')

@app.route('/real_data')
def serve_real_data():
    date = request.values.get('date_change', None)
    student = request.values.get('student_change', None)
    check = request.values.get('check', None)
    if check:
        if date:
            if student:
                file_name = "data/" + date + "/"+ student + "_sample.csv"
            else:
                file_name = "data/" + date + "/0_sample.csv"
        else:
            file_name = "data/3-2-16/0_sample.csv"
    else:
        if date:
            if student:
                file_name = "data/" + date + "/"+ student + ".csv"
            else:
                file_name = "data/" + date + "/0.csv"
        else:
            file_name = "data/3-2-16/0.csv"
    return render_template('real_data.html', data=url_for('static', filename=file_name))

@app.route('/students')
def filter():
    primary_student = request.values.get('student', None)
    if primary_student:
        entries = SocialProximity.query.filter_by(primary_person=primary_student)
        return render_template('students.html', entries=entries, primary_student=primary_student)
    else:
        entries = SocialProximity.query.all()
        return render_template('students.html', entries=entries, primary_student=None)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print port
    app.run(host='0.0.0.0', port=port, debug=True)