from app import db


# Helper table for many-to-many relationship
# questions have different tags
question_tags = db.Table('question_tags',
                         db.Column('question_id', db.Integer, db.ForeignKey('questions.id')),
                         db.Column('tag_id', db.Integer, db.ForeignKey('tags.id')))


class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)
    normalized = db.Column(db.Text)
    answer = db.Column(db.Text)
    answered_by = db.Column(db.Text)
    tags = db.relationship('Tag', secondary=question_tags,
                           backref=db.backref('tags', lazy='dynamic'))

    def __init__(self, question, normalized, answer, answered_by):
        self.question = question
        self.normalized = normalized
        self.answer = answer
        self.answered_by = answered_by

    def __repr__(self):
        return '<Question: %s>' % self.question.encode('utf-8')


class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.Text)
    questions = db.relationship('Question', secondary=question_tags,
                                backref=db.backref('questions', lazy='dynamic'))

    def __init__(self, tag):
        self.tag = tag

    def __repr__(self):
        return self.tag