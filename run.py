from flask import Flask, send_from_directory
from app.api.api import api_blueprint
from app.bookmarks_and_tags.views import bookmarks_blueprint
from config.config import IMG_PATH


app = Flask(__name__, static_folder='css')
app.config['JSON_AS_ASCII'] = False

# Blueprints' registration
app.register_blueprint(api_blueprint)
app.register_blueprint(bookmarks_blueprint)


@app.route('/img/<path:path>')
def upload_img(path):
    """This view gives access to img folder with pictures"""

    return send_from_directory(IMG_PATH, path)


if __name__ == '__main__':
    app.run()
