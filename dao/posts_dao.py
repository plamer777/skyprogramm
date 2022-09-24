"""The unit contains DAO class to get posts from JSON files and
get posts by different conditions like 'pk', 'keyword', etc"""
import json


class PostsDao:
    """This class serves as DAO"""

    def __init__(self, posts_filename: str, comments_filename: str):
        """Initialization of PostsDao class.

        :param posts_filename: the filename of JSON with posts data
        :param comments_filename: the filename of JSON with comments data
        """
        self.posts_filename = posts_filename
        self.comments_filename = comments_filename
        self.posts = self.load_posts()
        self.comments = self.load_comments()

    def load_posts(self) -> list:
        """This method uploads all posts from file

        Return:
            post_data - a list of dicts with posts data
        """
        with open(self.posts_filename, encoding='utf-8') as fin:

            posts_data = json.load(fin)

        return posts_data

    def load_comments(self):
        """The method uploads all comments from JSON file

        Return:
            comments_data - a list of dicts with comments data
        """
        with open(self.comments_filename, encoding='utf-8') as fin:

            comments_data = json.load(fin)

        return comments_data

    def get_all(self) -> list:
        """This method returns all posts from posts field of an instance"""
        return self.posts

    def get_by_pk(self, pk: int = 1) -> dict:
        """The method returns a post found by 'pk' or an empty dict

        :param pk: the id of desired post

        Return:
            post - a post found by pk, or an empty dict instead
        """
        posts = self.posts

        for post in posts:

            if post.get('pk') == pk:

                return post

        return {}

    def search_by_keyword(self, keyword: str = '') -> list:
        """The method returns a list of posts found by keyword

        :param keyword: a search string in posts list

        Return:
            found_posts - a list of dicts with found posts data
        """
        posts = self.posts
        found_posts = []

        for post in posts:

            if keyword.lower() in post.get('content', '').lower():

                found_posts.append(post)

        return found_posts

    def refresh_cash(self):
        """This is additional method on the future to refresh data in posts
        field"""
        self.posts = self.load_posts()

    def get_by_user(self, username: str = '') -> list:
        """The method returns posts found by username or ValueError if user
        isn't found

        :param username: the user's name for searching

        Return:
            found_posts - a list of dicts with posts data
        """
        found_posts = []
        posts = self.posts
        is_user_found = False

        for post in posts:

            if username.lower() in post.get('poster_name', '').lower():

                is_user_found = True

                if post.get('content'):
                    found_posts.append(post)

        if not is_user_found:

            raise ValueError('Нет такого пользователя')

        return found_posts

    def get_comments_by_post(self, post_id: int = 1) -> list:
        """The method returns all comments found by post id or ValueError if
        post_id isn't found

        :param post_id: the post's identificator

        Return:
            found_comments - a list of dicts with comments data
        """
        comments = self.comments
        found_comments = []
        is_found = False

        for comment in comments:

            if comment.get('post_id') == post_id:

                is_found = True

                if comment.get('comment'):
                    found_comments.append(comment)

        if not is_found:
            raise ValueError('Нет такого поста')

        return found_comments
