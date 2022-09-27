from flask import Blueprint, render_template

from config.config import post_dao

bookmarks_blueprint = Blueprint('bookmarks_blueprint',
                                __name__,
                                template_folder='bookmarks_templates')


@bookmarks_blueprint.route('/tag/<tag_name>')
def tags_page(tag_name: str):

    found_tagged_posts = post_dao.search_by_tag(tag_name)

    return render_template('tag.html', tag=tag_name.upper(),
                           found_posts=found_tagged_posts)
