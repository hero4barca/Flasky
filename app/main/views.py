from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .. import db
from flask_login import login_required
# from .forms import NameForm
# from ..models import User


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

@main.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'