import hashlib
import md5
from flask import render_template, session, url_for, redirect, g
from flask.ext.login import login_required, login_user, current_user
from flask.helpers import flash, get_flashed_messages
from forms import QUTLoginForm, ManualClassForm, ManualClassTimes
from functions import auto_import
from grouper import app, lm
from grouper.forms import LoginForm, SignUpForm
from markupsafe import Markup
from models import User, UserForm
from mongoengine.errors import DoesNotExist, NotUniqueError
from wtforms.validators import ValidationError

__author__ = 'David'


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', page='index')


@lm.user_loader
def load_user(id):
    return User.objects.with_id(id)


@app.before_request
def before_request():
    g.user = current_user


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            u = User.objects.get(username=form.username.data)
            if u.password == hashlib.md5(form.password.data).hexdigest():
                session['logged_in'] = True
                login_user(u)
                return redirect(url_for('index'))
            else:
                form.password.errors.append('Incorrect Password')
                print 'Invalid Password!'
        except DoesNotExist:
            form.username.errors.append(Markup('No such user - sign up <a href="/signup">here</a>.'))
    return render_template('login.html', form=form, page='login')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # TODO: Update with salt information?
    form = SignUpForm()
    is_logged_in = session['logged_in']
    if form.validate_on_submit():
        u = User()
        u.username = form.username.data
        u.password = hashlib.md5(form.password.data).hexdigest()
        u.email = form.email.data
        if len(form.name.data.split(' ')) != 2:
            form.name.errors.append("Please include only a first name and last name.")
            form.email.errors.append("Something Emaily")
        else:
            u.first_name = form.name.data.split(" ")[0]
            u.last_name = form.name.data.split(" ")[1]
        try:
            u.save()
            session['logged_in'] = True
            login_user(u)
            flash("Welcome to StudyGrouper, %s!" % u.first_name)
            return redirect(url_for('index'))
        except ValidationError:
            form.email.errors.append("Invalid Email Address.")
        except NotUniqueError as e:
            if 'email' in e.message:
                form.email.errors.append(
                    "That email address is already in use.  Log In?")  # TODO: Link to the login page
            elif 'username' in e.message:
                form.username.errors.append("Username taken.  Please choose another.")
            else:
                form.errors['unknown'] = ['An unknown error has occurred.  Please try again.']
    if not is_logged_in:
        return render_template('signup.html', form=form, page='signup', logged=is_logged_in)
    else:
        flash("You are already logged in!")
        return render_template('index.html', page='index')


@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('index'))


@app.route('/<username>')
@login_required
def profile(username):
    try:
        u = User.objects.get(username=username)
    except DoesNotExist:
        u = None
    return render_template('profile.html', user=u)


@app.route('/edit_classes', methods=['GET', 'POST'])
def edit_classes():
    qut_login_form = QUTLoginForm()
    class_add_form = ManualClassForm()
    time_form = ManualClassTimes()
    if qut_login_form.validate_on_submit():
        auto_import(qut_login_form.qut_username.data, qut_login_form.qut_password.data)
    return render_template('edit_classes.html', u=g.user, classes=g.user.subjects, qut_login_form=qut_login_form,
                           class_add_form=class_add_form, time_form=time_form)
