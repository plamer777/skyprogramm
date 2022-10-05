from flask import Blueprint, render_template, request
from config.config import post_dao

main_blueprint = Blueprint('main_blueprint',
                           __name__,
                           template_folder='bp_templates')


@main_blueprint.route('/')
def main_index():

    posts = post_dao.get_all()
    bookmarks = post_dao.load_bookmarks()
    posts_cut = post_dao.cut_posts_content(posts, 50)
    bookmarks_count = len(bookmarks)

    return render_template('index.html',
                           posts=posts_cut,
                           bookmarks_count=bookmarks_count)


@main_blueprint.route('/post/<int:post_id>')
def single_post_page(post_id):

    post = post_dao.get_by_pk(post_id)
    comments_to_post = post_dao.get_comments_by_post(post_id)

    return render_template("post.html", post=post, comments=comments_to_post)


@main_blueprint.route('/search/')
def search_page():

    s = request.args.get('s')

    if s is None:
        return "Введите параметр поиска"

    s = s.casefold()
    posts = post_dao.search_by_keyword(s)
    cut_posts = post_dao.cut_posts_content(posts, 80)

    if len(posts) > 10:
        posts = posts[0:10]

    quantity = len(posts)

    return render_template('search.html', posts=cut_posts, quantity=quantity)


@main_blueprint.route('/user/<username>')
def user_page(username):

    list_by_user = post_dao.get_by_user(username)
    cut_posts = post_dao.cut_posts_content(list_by_user, 80)

    return render_template('user-feed.html', posts=cut_posts,
                           username=username)
