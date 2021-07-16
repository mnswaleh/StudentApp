"""
Routes and views for the flask application.
"""

import json

from .models.Certificate import Certificate
from datetime import datetime
from flask import Blueprint, render_template, request
from .models.Student import Student
from .models.Course import Course
from .models.db import db

student_app = Blueprint(
    "student_app", __name__, template_folder="templates", static_folder="static"
)


@student_app.route("/", methods=["GET", "POST"])
@student_app.route("/home", methods=["GET", "POST"])
def home():
    """Renders the home page."""
    if request.method == "POST":
        name = request.form["name"]
        student_no = request.form["studentNo"]
        new_student = Student(name=name, StudentNo=student_no)
        db.session.add(new_student)
        db.session.commit()

    students = Student.query.all()
    courses = Course.query.all()
    return render_template(
        "index.html",
        title="Home Page",
        students=students,
        courses=courses,
        year=datetime.now().year,
    )


@student_app.route("/courses", methods=["GET", "POST"])
def courses():
    """Renders the contact page."""
    if request.method == "POST":
        name = request.form["name"]
        new_course = Course(name=name)
        db.session.add(new_course)
        db.session.commit()

    courses = Course.query.all()
    return render_template(
        "courses.html",
        title="Courses",
        courses=courses,
        year=datetime.now().year,
    )


@student_app.route("/certificates", methods=["GET", "POST", "PUT"])
def certificates():
    """Renders the about page."""
    if request.method == "POST":
        applicant = request.form["applicant"]
        course = request.form["course"]
        new_request = Certificate(applicant=applicant, course=course)
        db.session.add(new_request)
        db.session.commit()
    elif request.method == "PUT":
        cert_id = request.json["certificate"]
        cert = Certificate.query.get(cert_id)
        cert.recieved = not cert.recieved

        if not cert.recieved:
            cert.recievedDate = None
        else:
            cert.recievedDate = datetime.now()

        db.session.commit()
        data = {}
        data["operation"] = "succesfull"
        return json.dumps(data)

    certificates = Certificate.query.all()
    return render_template(
        "certificates.html",
        title="Certificates",
        certificates=certificates,
        year=datetime.now().year,
    )
