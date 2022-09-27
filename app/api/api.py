"""The API blueprint of Flask app. There're two views returning
all posts and post found by id in JSON format
"""
from flask import Blueprint, jsonify
from config.config import post_dao
from config.config import POSTS_FILE, COMMENTS_FILE, LOG_FILE, LOG_FORMAT
from utils import get_new_logger

# Creating Blueprint, PostsDao and Logger instances
api_blueprint = Blueprint('api_blueprint', __name__)
api_logger = get_new_logger(LOG_FILE)


@api_blueprint.route('/api/posts/')
def all_posts_json():
    """The view returns all posts in JSON format"""
    all_posts = post_dao.get_all()

    api_logger.info('Запрос /api/posts/')

    return jsonify(all_posts)


@api_blueprint.route('/api/posts/<int:post_id>')
def post_by_id_json(post_id):
    """The view returns a single post found by id"""
    found_post = post_dao.get_by_pk(post_id)

    api_logger.info(f'Запрос /api/posts/{post_id}')

    return jsonify(found_post)
