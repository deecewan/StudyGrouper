from flask import session
from grouper import db

__author__ = 'David'

class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    username = db.StringField(required=True)
    avatar = db.ImageField(size=(200,200,True), thumbnail=(60,60,True))
    password = db.StringField(required=True)

    def is_authenticated(self):
        return session['logged_in']

    def is_active(self):
        return True



class Subject(db.EmbeddedDocument):
    title = db.StringField(required=True)
    unit_code = db.StringField(required=True)
    times = db.EmbeddedDocumentField(Time)

class Time(db.EmbeddedDocument):
    type = db.StringField(required=True)
    start_time = db.StringField(required=True)
    end_time = db.StringField(required=True)
    day = db.StringField(required=True)