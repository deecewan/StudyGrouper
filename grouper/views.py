from flask import render_template
from grouper import app

__author__ = 'David'

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
