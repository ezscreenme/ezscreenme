from flask import render_template, url_for, flash, redirect, request
from website import app, db
# from website.forms import # import specific forms here
# from website.models import # import specific db models here
from flask_login import login_user, current_user, logout_user, login_required
import os
import bcrypt


@app.route('/home', methods=['GET'])
@app.route('/', methods=['GET'])
def home():
    return '<html><body><head></head><h1>Hello World!</h1></body></html>'


