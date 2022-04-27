import os

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class Settings:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
