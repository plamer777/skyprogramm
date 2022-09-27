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
        self.tagged_posts = self.create_tagged_posts()

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
        return self.tagged_posts

    def get_by_pk(self, pk: int = 1) -> dict:
        """The method returns a post found by 'pk' or an empty dict

        :param pk: the id of desired post

        Return:
            post - a post found by pk, or an empty dict instead
        """
        posts = self.tagged_posts

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
        posts = self.tagged_posts
        found_posts = []

        for post in posts:

            if keyword.lower() in post.get('content', '').lower():

                found_posts.append(post)

        return found_posts

    def refresh_cache(self):
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
        posts = self.tagged_posts
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

    def create_tagged_posts(self):
        """This method turns tags with '#' into links"""
        tagged_posts = []

        for post in self.posts:

            # use copy of current post to save original post without links
            added_post = post.copy()

            if '#' in post.get('content'):

                added_post = self._create_tag_link(added_post)

            tagged_posts.append(added_post)

        return tagged_posts

    @staticmethod
    def _create_tag_link(post: dict):
        """Secondary method to create links for tags in posts.

        :param post: the post to find and create link for tags starts with '#'
        """
        words = post.get('content').split(' ')

        for num, word in enumerate(words):

            if word.startswith("#"):
                tagged_str = f'<a href=/tags/{word[1:]}>{word}</a>'

                # changing tag with prepared link
                words[num] = tagged_str

                # write new content field with html tags
                post['content'] = ' '.join(words)

        return post

    def get_all_tagged_posts(self):
        """The method return all posts also including ones having tags"""
        return self.tagged_posts

    def refresh_tagged_posts(self):
        """Refreshing of a tagged posts cache if original posts were changed"""
        self.refresh_cache()
        self.tagged_posts = self.create_tagged_posts()

    def search_by_tag(self, tag_name: str):
        """This method serves to find all posts contains tags starting with
        '#'.

        :param tag_name: name of searching tag without '#' symbol
        """
        found_posts = []
        tag_name = '#' + tag_name.lower()

        for post in self.posts:

            word_list = post.get('content').lower().split(' ')

            if tag_name in word_list:

                found_posts.append(post)

        return found_posts



