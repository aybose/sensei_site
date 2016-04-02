from app import db
from models import *

def setup_db():
	db.drop_all()
	db.create_all()

	school_name = "Wildflower"
    school = School(school_name)
    db.session.add(school)
    db.session.commit()

    school_name = "Violeta"
    school = School(school_name)
    db.session.add(school)
    db.session.commit()

    teacher_name = "mary"
    school_name = "Wildflower"
    teacher_obj = Teacher(teacher_name)
    db.session.add(teacher_obj)
    school_obj = School.query.filter_by(school=school_name)[0]
    school_obj.teachers.append(teacher_obj)
    db.session.commit()

    teacher_name = "erin"
    school_name = "Wildflower"
    teacher_obj = Teacher(teacher_name)
    db.session.add(teacher_obj)
    school_obj = School.query.filter_by(school=school_name)[0]
    school_obj.teachers.append(teacher_obj)
    db.session.commit()

    teacher_name = "mardie"
    school_name = "Violeta"
    teacher_obj = Teacher(teacher_name)
    db.session.add(teacher_obj)
    school_obj = School.query.filter_by(school=school_name)[0]
    school_obj.teachers.append(teacher_obj)
    db.session.commit()

    username = "mary"
    password = "mary"
    if Teacher.query.filter_by(name=username).first() is not None:
        user_obj = User(username, password)
        db.session.add(user_obj)
        db.session.commit()

    username = "erin"
    password = "erin"
    if Teacher.query.filter_by(name=username).first() is not None:
        user_obj = User(username, password)
        db.session.add(user_obj)
        db.session.commit()

    username = "mardie"
    password = "mardie"
    if Teacher.query.filter_by(name=username).first() is not None:
        user_obj = User(username, password)
        db.session.add(user_obj)
        db.session.commit()

    school_name = "Wildflower"
    student_obj = Student("Uriah", 0)
    db.session.add(student_obj)
    school_obj = School.query.filter_by(school=school_name).first()
    school_obj.students.append(student_obj)
    db.session.commit()

    school_name = "Wildflower"
    student_obj = Student("Veylan", 1)
    db.session.add(student_obj)
    school_obj = School.query.filter_by(school=school_name).first()
    school_obj.students.append(student_obj)
    db.session.commit()

    school_name = "Wildflower"
    student_obj = Student("Sofi", 2)
    db.session.add(student_obj)
    school_obj = School.query.filter_by(school=school_name).first()
    school_obj.students.append(student_obj)
    db.session.commit()

    school_name = "Wildflower"
    student_obj = Student("Neve", 3)
    db.session.add(student_obj)
    school_obj = School.query.filter_by(school=school_name).first()
    school_obj.students.append(student_obj)
    db.session.commit()

    school_name = "Wildflower"
    student_obj = Student("Elliot", 4)
    db.session.add(student_obj)
    school_obj = School.query.filter_by(school=school_name).first()
    school_obj.students.append(student_obj)
    db.session.commit()

    school_name = "Wildflower"
    student_obj = Student("Riella", 5)
    db.session.add(student_obj)
    school_obj = School.query.filter_by(school=school_name).first()
    school_obj.students.append(student_obj)
    db.session.commit()

    school_name = "Wildflower"
    student_obj = Student("Dash", 6)
    db.session.add(student_obj)
    school_obj = School.query.filter_by(school=school_name).first()
    school_obj.students.append(student_obj)
    db.session.commit()

    school_name = "Wildflower"
    student_obj = Student("Dario", 7)
    db.session.add(student_obj)
    school_obj = School.query.filter_by(school=school_name).first()
    school_obj.students.append(student_obj)
    db.session.commit()

    school_name = "Wildflower"
    student_obj = Student("Eleanor", 8)
    db.session.add(student_obj)
    school_obj = School.query.filter_by(school=school_name).first()
    school_obj.students.append(student_obj)
    db.session.commit()

    school_name = "Wildflower"
    student_obj = Student("Bodhi", 9)
    db.session.add(student_obj)
    school_obj = School.query.filter_by(school=school_name).first()
    school_obj.students.append(student_obj)
    db.session.commit()

    school_name = "Wildflower"
    student_obj = Student("Mary", 10)
    db.session.add(student_obj)
    school_obj = School.query.filter_by(school=school_name).first()
    school_obj.students.append(student_obj)
    db.session.commit()

    school_name = "Wildflower"
    student_obj = Student("Erin", 11)
    db.session.add(student_obj)
    school_obj = School.query.filter_by(school=school_name).first()
    school_obj.students.append(student_obj)
    db.session.commit()

    school_name = "Wildflower"
    student_obj = Student("Taj", 12)
    db.session.add(student_obj)
    school_obj = School.query.filter_by(school=school_name).first()
    school_obj.students.append(student_obj)
    db.session.commit()

    school_name = "Wildflower"
    student_obj = Student("Silas", 13)
    db.session.add(student_obj)
    school_obj = School.query.filter_by(school=school_name).first()
    school_obj.students.append(student_obj)
    db.session.commit()

    school_name = "Wildflower"
    student_obj = Student("Beatrice", 14)
    db.session.add(student_obj)
    school_obj = School.query.filter_by(school=school_name).first()
    school_obj.students.append(student_obj)
    db.session.commit()

    school_name = "Wildflower"
    student_obj = Student("Willa", 15)
    db.session.add(student_obj)
    school_obj = School.query.filter_by(school=school_name).first()
    school_obj.students.append(student_obj)
    db.session.commit()

if __name__ == '__main__':
	setup_db()

