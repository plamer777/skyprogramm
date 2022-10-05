from flask import Flask
from app.api.api import api_blueprint
from app.bookmarks_and_tags.views import bookmarks_blueprint
from app.main_blueprint.view import main_blueprint


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# Blueprints' registration
app.register_blueprint(api_blueprint)
app.register_blueprint(bookmarks_blueprint)
app.register_blueprint(main_blueprint)

if __name__ == '__main__':
    app.run()
