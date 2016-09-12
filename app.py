from flask import Flask, request, url_for
from flask_sqlalchemy import SQLAlchemy

from myproject import views
from myproject import app 

# import REST routes
from myproject import rest_server 

# load file specified by APP_CONFIG_FILE
# -- contains environment specific variables (production, development..etc)
app.config.from_envvar('APP_CONFIG_FILE')

db = SQLAlchemy(app)

