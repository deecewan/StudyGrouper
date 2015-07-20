from flask import render_template, session, url_for, redirect
from grouper import app, lm
from grouper.forms import LoginForm, SignUpForm

__author__ = 'David'

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@lm.user_loader
def load_user(id):
    pass

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print form.username.data, form.password.data
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