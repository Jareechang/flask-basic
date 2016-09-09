from flask import Flask
app = Flask(__name__, template_folder='./app/templates/')
from myproject import views
