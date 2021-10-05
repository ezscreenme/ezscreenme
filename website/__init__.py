from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import LoginManager
import json

# getting secret key from config file
with open('secrets.json') as f:
    data = json.load(f)

# initializing flask
app = Flask(__name__)
app.config['SECRET_KEY'] = data['secret_key']

# setting up db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# flask-login setup for auth
login_manager = LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'

# routes to allow the site to work
from website import routes
