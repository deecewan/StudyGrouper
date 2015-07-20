from grouper import app

__author__ = 'David'

@app.route('/')
@app.route('/index')
def index():
    return 'Hello World! This is me!'
