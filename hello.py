from flask import Flask, request
app = Flask(__name__)

# Basic routing 

@app.route('/')
def index():
    return 'Index page'

@app.route('/hello')
def hello():
    return 'Hello world!'

# dynamic routing 

@app.route('/user/<username>')
def show_user_profile(username):
    # show user profile name for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with given id, the id is an integer
    print post_id
    return 'Post %d' % post_id


# Redirection behaviour

@app.route('/project/')
# if project is visited, a redirection from project -> project/ 
def projects():
    return 'the projects page'

@app.route('/about')
def about():
    return 'the about page'

# http Requests

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # do the login
    else 
        # show the login form

