from flask.ext.wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, InputRequired

__author__ = 'David'

class SignUpForm(Form):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('')

class LoginForm(Form):
    username = StringField('username', validators=[DataRequired(message='Please enter your username')])
    password = PasswordField('password', validators=[DataRequired(message='Please enter your password')])