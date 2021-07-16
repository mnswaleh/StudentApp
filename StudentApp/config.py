"""Configure application"""

import os
import urllib

basedir = os.path.abspath(os.path.dirname(__file__))
connString = urllib.parse.quote_plus(os.getenv('DATABASE_URL'))


class Config(object):
    """Default application configuration"""

    DEBUG = True  # Turns on debugging features in Flask
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv('SECRET_KEY') or 'blablabla'
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=%s" % connString or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    """Production application configuration"""

    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    """Development application configuration"""

    DEBUG = True


class TestingConfig(Config):
    """Testing application configuration"""

    TESTING = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
