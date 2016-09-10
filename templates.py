from flask import render_template, Flask, request
app = Flask(__name__)

# Receiving data
with app.test_request_context('/hello', method='POST'):
    # Now you can do something with request until the
    # end of the with block such as basic assertion
    assert request.path == '/hello'
    assert request.method == 'POST'

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username or password'

    return render_template('login.html', error)
