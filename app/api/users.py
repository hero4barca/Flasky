from . import api
from app import db
from app.models import User, Permission
from app.decorators import permission_required
from flask import request, jsonify, g, url_for
from .errors import forbidden

@api.route('/users/<int:id>/')
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_json())

@api.route('/users/<int:id>/posts/')
def get_user_posts(id):
    user = User.query.get_or_404(id)
    query = user.posts
    # add pagination
    page = request.args.get('page', 1, type=int)
    pagination = query.paginate( page=page, per_page=10, error_out=False)
    posts = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_user_posts', page=page-1)
    next = None
    if pagination.has_next:
        next = url_for('api.get_user_posts', page=page+1)
    return jsonify({
        'posts': [post.to_json() for post in posts],
        'prev_url': prev,
        'next_url': next,
        'count': pagination.total
        })


