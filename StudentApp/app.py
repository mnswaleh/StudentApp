"""
The flask application package.
"""

from flask import Flask
from flask_migrate import Migrate
from config import config
from StudentApp.models.db import db
from StudentApp.views import student_app

migrate = Migrate()


def create_app(config_name):
    app = Flask(__name__, static_folder=None)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.register_blueprint(student_app)
    db.init_app(app)
    migrate.init_app(app, db)
    return app
