from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .. import db
# from .forms import NameForm
# from ..models import User


@main.route('/')
def index():
    return '<h1>Hello World!<h1/>'

@main.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)