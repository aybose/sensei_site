import os
import sqlite3

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing


# configuration
DATABASE = '/tmp/prnet_site.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'admin'


app = Flask(__name__)
app.config.from_object(__name__)

# DB METHODS #

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/show_entries')
def show_entries():
    cur = g.db.execute('select school, date, primary_student, secondary_student, rsval from SocialProximity order by id desc')
    entries = [dict(school=row[0], date=row[1], primary_student=row[2], secondary_student=row[3], rsval=row[4]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)

@app.route('/add_entry', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into SocialProximity (school, date, primary_student, secondary_student, rsval) values (?, ?, ?, ?, ?)',
                 [request.form['school'], request.form['date'], request.form['primary'], request.form['secondary'], request.form['rsval']])
    g.db.commit()
    return show_entries()

# TEMPLATES #

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if session.get('logged_in'):
        return redirect(url_for('home'))
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('home'))
    return render_template('index.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('login'))

@app.route("/home")
def home():
    return render_template('home.html')

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
def real_data():
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
        cur = g.db.execute('select school, date, primary_student, secondary_student, rsval from SocialProximity where primary_student = ? order by id desc', [primary_student])
        entries = [dict(school=row[0], date=row[1], primary_student=row[2], secondary_student=row[3], rsval=row[4]) for row in cur.fetchall()]
        return render_template('students.html', entries=entries, primary_student=primary_student)
    else:
        cur = g.db.execute('select school, date, primary_student, secondary_student, rsval from SocialProximity order by id desc')
        entries = [dict(school=row[0], date=row[1], primary_student=row[2], secondary_student=row[3], rsval=row[4]) for row in cur.fetchall()]
        return render_template('students.html', entries=entries, primary_student=None)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print port
    app.run(host='0.0.0.0', port=port)