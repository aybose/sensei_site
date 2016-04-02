from app import db


# Helper table for many-to-many relationship
# questions have different tags
# school_students = db.Table('school_students',
#                          db.Column('school_id', db.Integer, db.ForeignKey('school.id')),
#                          db.Column('student_id', db.Integer, db.ForeignKey('student.id')))


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text)
    password = db.Column(db.Text)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return self.username

class School(db.Model):
    __tablename__ = 'schools'

    id = db.Column(db.Integer, primary_key=True)
    school = db.Column(db.Text)
    teachers = db.relationship('Teacher', backref='school',
                                lazy='dynamic')
    students = db.relationship('Student', backref='school',
                                lazy='dynamic')

    def __init__(self, school):
        self.school = school

    def __repr__(self):
        return '<School: %s>' % self.school.encode('utf-8')

class Teacher(db.Model):
    __tablename__ = 'teachers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    school_id = db.Column(db.Integer, db.ForeignKey('schools.id'))

    def __init__(self, name):
        self.name= name

    def __repr__(self):
        return self.name

class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    school_id = db.Column(db.Integer, db.ForeignKey('schools.id'))

    def __init__(self, name):
        self.name= name

    def __repr__(self):
        return self.name