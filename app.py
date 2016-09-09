from flask import Flask, request, url_for
from flask_sqlalchemy import SQLAlchemy

from myproject import views
from myproject import app 

# import views
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

