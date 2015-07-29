from flask.ext.login import LoginManager
from flask.ext.mongoengine import MongoEngine

__author__ = 'David'

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')
db = MongoEngine(app)
lm = LoginManager()
lm.login_view = 'login'
lm.init_app(app)



import views
