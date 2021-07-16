from .db import db


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    StudentNo = db.Column(db.String(128), unique=True, nullable=False)
    certificates = db.relationship('Certificate', backref=db.backref('students', lazy=True))
