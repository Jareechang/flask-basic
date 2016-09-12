from flask import render_template 
from myproject import app

# Route templates 
# @app.route('/')
# def index():
    # return "Index page"

@app.route('/hello')
def hello():
    return "hello"

@app.route('/hello/<name>')
def hello_name(name=None):
    return render_template('hello.html', name=name)

@app.route('/template')
def template():
    user = { "name" : "Jerry" }
    return render_template(
        'index.html',
        title='Home',
        FLASK_ENV=app.config['FLASK_ENV'],
        user=user
    )
