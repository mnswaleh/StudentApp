from datetime import datetime
from .db import db


class Certificate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    applicant = db.Column(db.Integer, db.ForeignKey("student.id"), nullable=False)
    course = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=False)
    applicationDate = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    recieved = db.Column(db.Boolean, nullable=False, server_default="false")
    recievedDate = db.Column(db.DateTime(timezone=True), nullable=True)
