from flask import render_template, Flask, request
app = Flask(__name__)

# templates
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

# Receiving data

with app.test_request_context('/hello', method='POST'):
    # Now you can do something with request until the
    # end of the with block such as basic assertion
    assert request.path == '/hello'
    assert request.method == 'POST'



