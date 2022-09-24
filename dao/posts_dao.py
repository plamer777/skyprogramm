import json


class PostsDao:

    def __init__(self, posts_filename: str, comments_filename: str):

        self.posts_filename = posts_filename
        self.comments_filename = comments_filename
        self.posts = self.load_posts()
        self.comments = self.load_comments()

    def load_posts(self) -> list:

        with open(self.posts_filename, encoding='utf-8') as fin:

            posts_data = json.load(fin)

        return posts_data

    def load_comments(self):

        with open(self.comments_filename, encoding='utf-8') as fin:

            comments_data = json.load(fin)

        return comments_data

    def get_all(self) -> list:

        return self.posts

    def get_by_pk(self, pk: int = 1) -> list:

        posts = self.posts

        for post in posts:

            if post.get('pk') == pk:

                return post

        return []

    def search_by_keyword(self, keyword: str = '') -> list:

        posts = self.posts
        found_posts = []

        for post in posts:

            if keyword.lower() in post.get('content', '').lower():

                found_posts.append(post)

        return found_posts

    def refresh_cash(self):

        self.posts = self.load_posts()

    def get_by_user(self, username: str = '') -> list:

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
