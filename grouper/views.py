from flask import render_template, session, url_for, redirect, g
from flask.ext.login import login_required, login_user, current_user
from grouper import app, lm
from grouper.forms import LoginForm, SignUpForm
from markupsafe import Markup
from models import User
from mongoengine.errors import DoesNotExist

__author__ = 'David'

@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html')

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
            if u.password == form.password.data:
                session['logged_in'] = True
                login_user(u)
                return redirect(url_for('index'))
            else:
                form.username.errors.append('Incorrect Password')
                print 'Invalid Password!'
        except DoesNotExist:
            form.username.errors.append(Markup('No such user - sign up <a href="/signup">here</a>.'))
    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        pass
    return render_template('signup.html', form=form)

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('index'))