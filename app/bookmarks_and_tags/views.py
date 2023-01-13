from flask import Blueprint, render_template, redirect, abort, url_for

from config.config import post_dao

bookmarks_blueprint = Blueprint('bookmarks_blueprint',
                                __name__,
                                template_folder='bookmarks_templates')


@bookmarks_blueprint.route('/tags/<tag_name>/')
def tags_page(tag_name: str):

    posts = post_dao.search_by_tag(tag_name)

    # if posts not found then raise 404 error
    if not posts:
        abort(404)

    cut_posts = post_dao.cut_posts_content(posts, 80)

    return render_template('tag.html', tag=tag_name.upper(),
                           found_posts=cut_posts)


@bookmarks_blueprint.route('/bookmarks/add/<int:post_id>/')
def add_bookmark(post_id):

    post_dao.save_to_bookmarks(post_id)

    return redirect('/', code=302)


@bookmarks_blueprint.route('/bookmarks/remove/<int:post_id>/')
def remove_bookmark(post_id):

    post_dao.remove_from_bookmarks(post_id)

    return redirect(url_for('bookmarks_blueprint.bookmarks_page'), code=302)


@bookmarks_blueprint.route('/bookmarks/')
def bookmarks_page():

    all_bookmarks = post_dao.get_all_bookmarks()

    cut_bookmarks = post_dao.cut_posts_content(all_bookmarks, 80)

    return render_template('bookmarks.html', bookmarks=cut_bookmarks)
