"""This unit contains tests class - TestPostsDao to test PostsDao class"""
from os import path
import pytest
from config.config import POSTS_FILE, COMMENTS_FILE, \
    POSTS_KEYS, COMMENTS_KEYS, BOOKMARKS_PATH
from dao.posts_dao import PostsDao


@pytest.fixture()
def dao_test():
    """This function is fixture for test class, returns an instance of
    PostsDao class"""
    posts_dao_test = PostsDao(POSTS_FILE, COMMENTS_FILE, BOOKMARKS_PATH)

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

            PostsDao('wrong_path', COMMENTS_FILE, BOOKMARKS_PATH)

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

            PostsDao(POSTS_FILE, 'wrong_path', BOOKMARKS_PATH)

    def test_load_bookmarks_errors(self):
        """Checking if FileNotFoundError raises when bookmarks file name
                is wrong"""
        with pytest.raises(FileNotFoundError):

            PostsDao(POSTS_FILE, COMMENTS_FILE, 'wrong_path')

    def test_get_all_posts(self, dao_test):
        """Testing 'get_all_posts' method of PostsDao class"""
        all_posts = dao_test.get_all()

        assert type(all_posts) == list, 'Загружается не список'
        assert len(all_posts) != 0, 'Список пустой'
        assert type(all_posts[0]) == dict, 'Внутри списка не словарь'

    def test_get_by_pk(self, dao_test):
        """Testing get_by_pk method of PostsDao"""
        single_post = dao_test.get_by_pk(8)

        assert type(single_post) == dict, 'Пост приходит не в виде словаря'
        assert len(single_post) != 0, 'Словарь пуст'

        # Checking if all dict keys are correct
        for key in POSTS_KEYS:

            assert key in single_post.keys(), 'Ключ не найден'

        assert single_post.get('comments_count') == 'Нет комментариев'


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

            dao_test.get_comments_by_post(8)

    def test_create_tagged_posts(self, dao_test):
        """Testing create_tagged_posts method of PostsDao"""
        tagged_posts = dao_test.create_tagged_posts()
        post = tagged_posts[0]

        assert type(tagged_posts) == list, 'Загружается не список'
        assert len(tagged_posts) != 0, 'Список пустой'
        assert type(tagged_posts[0]) == dict, 'Внутри списка не словарь'
        assert '<a href=/tags/тарелка>#тарелка</a>' in post.get('content')

    def test_search_by_tag(self, dao_test):
        """Testing search_by_tag method of PostsDao"""
        found_posts = dao_test.search_by_tag('кот')

        assert type(found_posts) == list, 'Загружается не список'
        assert len(found_posts) == 1, 'Список длиннее одного элемента'
        assert type(found_posts[0]) == dict, 'Внутри списка не словарь'
        assert "#кот" in found_posts[0].get('content')

    def test_save_to_bookmarks(self, dao_test):
        """The test method to check if bookmarks were saved to cache and
        JSON file"""
        start_file_size = path.getsize(BOOKMARKS_PATH)

        dao_test.save_to_bookmarks(1)

        end_file_size = path.getsize(BOOKMARKS_PATH)
        all_bookmarks = dao_test.get_all_bookmarks()

        assert end_file_size > start_file_size, 'Запись в файл не удалась'
        assert type(all_bookmarks) == list, 'Неверный тип данных'
        assert len(all_bookmarks) == 1, 'Данные не сохранились в кэш'

    def test_load_bookmarks(self, dao_test):
        """Checking if bookmarks were loaded from JSON file"""
        loaded_data = dao_test.load_bookmarks()

        assert type(loaded_data) == list, 'Загружается не список'
        assert len(loaded_data) == 1, 'Список пуст'

    def test_get_all_bookmarks(self, dao_test):
        """Testing get_all_bookmarks method of PostsDao to be sure the
        bookmarks were saved in cache"""
        all_bookmarks = dao_test.get_all_bookmarks()

        assert type(all_bookmarks) == list, 'Загружается не список'
        assert len(all_bookmarks) == 1, 'Список пуст'

    def test_remove_from_bookmarks(self, dao_test):
        """Testing remove_from_bookmarks method of PostsDao"""
        start_file_size = path.getsize(BOOKMARKS_PATH)

        dao_test.remove_from_bookmarks(1)

        end_file_size = path.getsize(BOOKMARKS_PATH)

        all_bookmarks = dao_test.get_all_bookmarks()

        assert end_file_size < start_file_size, 'Запись в файл не удалась'
        assert type(all_bookmarks) == list, 'Неверный тип данных'
        assert len(all_bookmarks) == 0, 'Данные из кэш не удалены'

    def test_cut_content(self, dao_test):
        """Testing cut_content method of PostsDao"""
        cut_post = dao_test.cut_content(2, 50)

        assert type(cut_post) == dict, 'Неверный тип данных поста'
        assert len(cut_post.get('content')) == 50, 'Неверная длина текста'
        assert cut_post.get('pk') == 2, 'Неверный идентификатор поста'
        assert set(cut_post.keys()) == POSTS_KEYS, 'Проблема с ключами поста'

    def test_cut_posts_content(self, dao_test):
        """Testing cut_posts_content method of PostsDao"""
        all_posts = dao_test.get_all()
        cut_posts = dao_test.cut_posts_content(all_posts, 50)

        assert type(cut_posts) == list, 'Неверный тип данных'
        assert len(cut_posts[1].get('content')) == 50, 'Неверная длина текста'
        assert cut_posts[1].get('pk') == 2, 'Неверный идентификатор поста'
        assert set(cut_posts[0].keys()) == POSTS_KEYS, 'Проблема с ключами ' \
                                                       'поста'

