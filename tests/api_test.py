"""The unit contains test class - TestApi to test API views"""
import pytest
from run import app
from config.config import POSTS_KEYS


@pytest.fixture()
def test_api():
    """Pytest fixture returns test client of flask app"""
    test_app = app.test_client()

    return test_app


class TestApi:
    """TestApi is a class for testing API blueprints"""

    def test_all_posts_json(self, test_api):
        """The test method for testing 'all_posts_json' view

        :param test_api: the fixture with test client.
        """
        request = test_api.get('/api/posts/')
        json_api = request.json

        assert request.status_code == 200, 'Ответ сервера не ОК'
        assert type(json_api) == list, 'В json приходит не список'
        assert type(json_api[0]) == dict, 'Внутри json не словарь'
        assert len(json_api) != 0, 'Список пустой'

    def test_post_by_id_api(self, test_api):
        """The test method checking 'post_by_id_json' view

        :param test_api: the fixture with test client.
        """
        request = test_api.get('/api/posts/1')
        json_api = request.json

        assert request.status_code == 200, 'Ответ сервера не ОК'
        assert type(json_api) == dict, 'В json приходит не словарь'
        assert set(json_api.keys()) == POSTS_KEYS, 'Ключи не найдены'
