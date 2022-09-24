from os import path
POSTS_FILE = path.join('..', 'data', 'posts.json')
COMMENTS_FILE = path.join('..', 'data', 'comments.json')
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
