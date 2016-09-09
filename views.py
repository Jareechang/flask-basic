from flask import render_template 
from myproject import app

# Basic routing 
@app.route('/')
def index():
    return "Index page"

@app.route('/hello')
def hello():
    return "hello"

@app.route('/template')
def template():
    user = { "name" : "Jerry" }
    return render_template(
        'index.html',
        title='Home',
        user=user
    )
