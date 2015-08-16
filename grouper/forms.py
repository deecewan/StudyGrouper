from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SelectField, DateTimeField
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


class QUTLoginForm(Form):
    qut_username = StringField('username', validators=[DataRequired()])
    qut_password = PasswordField('password', validators=[DataRequired()])


class ManualClassForm(Form):
    title = StringField('title', validators=[DataRequired()])
    unit_code = StringField('unit-code', validators=[DataRequired()])


class ManualClassTimes(Form):
    choices = [('mon', 'Monday'), ('tue', 'Tuesday'), ('wed', 'Wednesday'), ('thu', 'Thursday'), ('fri', 'Friday'),
               ('sat', 'Saturday'), ('sun', 'Sunday')]
    day = SelectField(u'Day', choices=choices)
    class_type = StringField('Class Type')
    start_time = DateTimeField('start-time', format='%H:%M:%S')
    end_time = DateTimeField('start-time', format='%H:%M:%S')
