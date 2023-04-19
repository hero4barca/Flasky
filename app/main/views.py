from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .. import db
from flask_login import login_required
from ..decorators import admin_required, permission_required
# from .forms import NameForm
from ..models import Permission


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


@main.route('/admin')
@login_required
@admin_required
def for_admins_only():
    return "For administrators!"

@main.route('/moderate')
@login_required
@permission_required(Permission.MODERATE)
def for_moderators_only():
    return "For comment moderators!"