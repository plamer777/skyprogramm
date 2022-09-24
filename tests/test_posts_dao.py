"""This unit contains tests class - TestPostsDao to test PostsDao class"""
import pytest
from config.config import POSTS_FILE, COMMENTS_FILE, \
    POSTS_KEYS, COMMENTS_KEYS
from dao.posts_dao import PostsDao


@pytest.fixture()
def dao_test():
    """This function is fixture for test class, returns an instance of
    PostsDao class"""
    posts_dao_test = PostsDao(POSTS_FILE, COMMENTS_FILE)

    return posts_dao_test


class TestPostsDao:
    """The TestPostsDao class for testing PostsDao"""
    def test_load_posts(self, dao_test):
        """This method tests load post method from PostsDao"""
        loaded_data = dao_test.load_posts()

        assert type(loaded_data) == list, 'Загружается не список'
        assert len(loaded_data) != 0, 'Список пустой'
        assert type(loaded_data[0]) == dict, 'Внутри списка не словарь'

    def test_load_posts_errors(self):
        """The method serves to check if FileNotFoundError raises when
        filename is wrong"""
        with pytest.raises(FileNotFoundError):

            PostsDao('wrong_path', COMMENTS_FILE)

    def test_load_comments(self, dao_test):
        """The test method to check load_comments method of PostsDao"""
        loaded_data = dao_test.load_comments()

        assert type(loaded_data) == list, 'Загружается не список'
        assert len(loaded_data) != 0, 'Список пустой'
        assert type(loaded_data[0]) == dict, 'Внутри списка не словарь'

    def test_load_comments_errors(self):
        """Checking if FileNotFoundError raises when comments file name
        is wrong"""
        with pytest.raises(FileNotFoundError):

            PostsDao(POSTS_FILE, 'wrong_path')

    def test_get_all_posts(self, dao_test):
        """Testing 'get_all_posts' method of PostsDao class"""
        all_posts = dao_test.get_all()

        assert type(all_posts) == list, 'Загружается не список'
        assert len(all_posts) != 0, 'Список пустой'
        assert type(all_posts[0]) == dict, 'Внутри списка не словарь'

    def test_get_by_pk(self, dao_test):
        """Testing get_by_pk method of PostsDao"""
        single_post = dao_test.get_by_pk()

        assert type(single_post) == dict, 'Пост приходит не в виде словаря'
        assert len(single_post) != 0, 'Словарь пуст'

        # Checking if all dict keys are correct
        for key in POSTS_KEYS:

            assert key in single_post.keys(), 'Ключ не найден'

    def test_search_by_keyword(self, dao_test):
        """Checking if the 'search_by_keyword' method works correct"""
        found_post = dao_test.search_by_keyword('кот')

        assert type(found_post) == list, 'Загружается не список'
        assert len(found_post) != 0, 'Список пустой'
        assert type(found_post[0]) == dict, 'Внутри списка не словарь'

    def test_get_by_user(self, dao_test):
        """Testing 'get_by_user' method of PostsDao class"""
        found_posts = dao_test.get_by_user('leo')

        assert type(found_posts) == list, 'Загружается не список'
        assert len(found_posts) != 0, 'Список пустой'
        assert type(found_posts[0]) == dict, 'Внутри списка не словарь'

    def test_get_by_user_errors(self, dao_test):
        """Checking if ValueError raises when user isn't found"""
        with pytest.raises(ValueError):

            dao_test.get_by_user('plamer')

    def test_get_comments_by_post(self, dao_test):
        """Testing 'get_comments_by_post' method of PostsDao class"""
        found_comments = dao_test.get_comments_by_post()

        assert type(found_comments) == list, 'Загружается не список'
        assert len(found_comments) != 0, 'Список пустой'
        assert type(found_comments[0]) == dict, 'Внутри списка не словарь'
        assert COMMENTS_KEYS == set(found_comments[0].keys()), 'Ключ не найден'

    def test_get_comments_by_post_errors(self, dao_test):
        """Checking if ValueError raises when post id isn't found'"""
        with pytest.raises(ValueError):

            dao_test.get_comments_by_post(50)
