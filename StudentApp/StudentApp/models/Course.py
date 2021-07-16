from .db import db


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    certificates = db.relationship('Certificate', backref=db.backref('courses', lazy=True))
