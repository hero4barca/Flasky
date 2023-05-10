from . import api
from app.models import  Comment
from flask import request, jsonify,  url_for


@api.route('/comments/')
def get_comments():
    page = request.args.get('page', 1, type=int)
    pagination = Comment.query.paginate( page=page, per_page=10, error_out=False)
    comments = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_comments', page=page-1)
    next = None
    if pagination.has_next:
        next = url_for('api.get_comments', page=page+1)
    return jsonify({
        'comments': [comment.to_json() for comment in comments],
        'prev_url': prev,
        'next_url': next,
        'count': pagination.total
        })


@api.route('/comments/<int:id>')
def get_comment(id):
    comment = Comment.query.get_or_404(id)
    return jsonify(comment.to_json())