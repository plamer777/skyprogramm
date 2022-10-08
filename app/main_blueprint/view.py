"""This unit contains views for main blueprint. There are index, post,
search and user routes here"""
from flask import Blueprint, render_template, request
from config.config import post_dao

# main_blueprint initialization
main_blueprint = Blueprint('main_blueprint',
                           __name__,
                           template_folder='bp_templates')


@main_blueprint.route('/')
def main_index():
    """This is a view for an index page"""
    posts = post_dao.get_all()
    bookmarks = post_dao.load_bookmarks()

    # cutting all posts' content
    posts_cut = post_dao.cut_posts_content(posts, 50)

    # calculating bookmarks' amount
    bookmarks_count = len(bookmarks)

    return render_template('index.html',
                           posts=posts_cut,
                           bookmarks_count=bookmarks_count)


@main_blueprint.route('/post/<int:post_id>')
def single_post_page(post_id):
    """The view for a single post page by provided id"""
    post = post_dao.get_by_pk(post_id)

    try:
        comments_to_post = post_dao.get_comments_by_post(post_id)

    # if comments not found then return an empty list
    except ValueError:
        comments_to_post = []

    return render_template("post.html", post=post, comments=comments_to_post)


@main_blueprint.route('/search/')
def search_page():
    """The search page view"""

    # getting keyword for searching
    s = request.args.get('s')

    if s is None:
        return "Введите параметр поиска"

    s = s.casefold()
    posts = post_dao.search_by_keyword(s)
    cut_posts = post_dao.cut_posts_content(posts, 80)

    # decreasing posts' amount if there're more than 10 posts
    if len(posts) > 10:
        posts = posts[0:10]

    # calculating posts' amount
    quantity = len(posts)

    return render_template('search.html', posts=cut_posts, quantity=quantity)


@main_blueprint.route('/user/<username>')
def user_page(username):
    """This view serves to process all /user/ requests"""
    try:
        list_by_user = post_dao.get_by_user(username)
        cut_posts = post_dao.cut_posts_content(list_by_user, 80)

    # if user not found then return an empty list
    except ValueError:
        cut_posts = []

    return render_template('user-feed.html', posts=cut_posts,
                           username=username)
