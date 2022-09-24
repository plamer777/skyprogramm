import pytest
from coursework2_source.config.config import POSTS_FILE, COMMENTS_FILE, \
    POSTS_KEYS, COMMENTS_KEYS

from coursework2_source.dao.posts_dao import PostsDao


@pytest.fixture()
def dao_test():

    posts_dao = PostsDao(POSTS_FILE, COMMENTS_FILE)

    return posts_dao


class TestPostsDao:

    def test_load_posts(self, dao_test):

        loaded_data = dao_test.load_posts()

        assert type(loaded_data) == list, 'Загружается не список'
        assert len(loaded_data) != 0, 'Список пустой'
        assert type(loaded_data[0]) == dict, 'Внутри списка не словарь'

    def test_load_posts_errors(self):

        with pytest.raises(FileNotFoundError):

            PostsDao('wrong_path', COMMENTS_FILE)

    def test_load_comments(self, dao_test):

        loaded_data = dao_test.load_comments()

        assert type(loaded_data) == list, 'Загружается не список'
        assert len(loaded_data) != 0, 'Список пустой'
        assert type(loaded_data[0]) == dict, 'Внутри списка не словарь'

    def test_load_comments_errors(self):

        with pytest.raises(FileNotFoundError):

            PostsDao(POSTS_FILE, 'wrong_path')

    def test_get_all_posts(self, dao_test):

        all_posts = dao_test.get_all()

        assert type(all_posts) == list, 'Загружается не список'
        assert len(all_posts) != 0, 'Список пустой'
        assert type(all_posts[0]) == dict, 'Внутри списка не словарь'

    def test_get_by_pk(self, dao_test):

        single_post = dao_test.get_by_pk()

        assert type(single_post) == dict, 'Пост приходит не в виде словаря'
        assert len(single_post) != 0, 'Словарь пуст'
        for key in POSTS_KEYS:

            assert key in single_post.keys(), 'Ключ не найден'

    def test_search_by_keyword(self, dao_test):

        found_post = dao_test.search_by_keyword('кот')

        assert type(found_post) == list, 'Загружается не список'
        assert len(found_post) != 0, 'Список пустой'
        assert type(found_post[0]) == dict, 'Внутри списка не словарь'

    def test_get_by_user(self, dao_test):

        found_posts = dao_test.get_by_user('leo')

        assert type(found_posts) == list, 'Загружается не список'
        assert len(found_posts) != 0, 'Список пустой'
        assert type(found_posts[0]) == dict, 'Внутри списка не словарь'

    def test_get_by_user_errors(self, dao_test):

        with pytest.raises(ValueError):

            dao_test.get_by_user('plamer')

    def test_get_comments_by_post(self, dao_test):

        found_comments = dao_test.get_comments_by_post()

        assert type(found_comments) == list, 'Загружается не список'
        assert len(found_comments) != 0, 'Список пустой'
        assert type(found_comments[0]) == dict, 'Внутри списка не словарь'
        assert COMMENTS_KEYS == set(found_comments[0].keys()), 'Ключ не найден'

    def test_get_comments_by_post_errors(self, dao_test):

        with pytest.raises(ValueError):

            dao_test.get_comments_by_post(50)
