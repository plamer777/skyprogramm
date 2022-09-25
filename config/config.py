"""The unit contains named constants for different purposes like JSON
uploading, DAO testing"""
from os import path

POSTS_FILE = path.join('data', 'posts.json')
COMMENTS_FILE = path.join('data', 'comments.json')
LOG_FILE = path.join('logs', 'api.log')

LOG_FORMAT = '%(asctime)s [%(levelname)s] %(message)s'

POSTS_KEYS = {'poster_name',
              'poster_avatar',
              'pic',
              'content',
              'views_count',
              'likes_count',
              'pk'
              }
COMMENTS_KEYS = {'post_id',
                 'commenter_name',
                 'comment',
                 'pk'
                 }
