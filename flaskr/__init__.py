from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__) # used by manage.py
app.config.from_object('flaskr.config')

db = SQLAlchemy(app)  # used by models.py

import flaskr.views