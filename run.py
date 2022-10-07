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


@app.errorhandler(404)
def error_404(error_code):

    print(f'Возникла ошибка {error_code}')

    return 'Упс, страница, которую вы искали не существует, код ошибки - 404'


@app.errorhandler(500)
def error_500(error_code):

    print(f'Возникла ошибка {error_code}')

    return 'Возникла ошибка со стороны сервера, код ошибки - 500'


if __name__ == '__main__':
    app.run()
