from flask.ext.wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
__author__ = 'David'

class SignUpForm(Form):
    username = StringField('username', validators=[DataRequired(message='Please Choose A Username')])
    email = StringField('email', validators=[DataRequired()])
    name = StringField('name')
    qut_email = StringField('qut_email')
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm_password', validators=[DataRequired()])



class LoginForm(Form):
    username = StringField('username', validators=[DataRequired(message='Please enter your username')])
    password = PasswordField('password', validators=[DataRequired(message='Please enter your password')])