from flask import Blueprint, render_template
from .dao.posts_dao import PostsDAO

posts_blueprint = Blueprint("posts_blueprint", __name__, template_folder="templates")
posts_dao = PostsDAO("data/data.json")


@posts_blueprint.route("/")
def posts_page():
    # try:
    posts = posts_dao.get_posts_all()
    return render_template("index.html", posts=posts)
    # except FileNotFoundError:
        # return f"Произошла ошибка на главной странице: {FileNotFoundError}"


@posts_blueprint.route("/post/<post_pk>")
def post_page(post_pk):
    return f"это страничка с постом {post_pk}"


@posts_blueprint.route("/search/<query>")
def search_page(query):
    return f"это страничка для поиска {query}"


@posts_blueprint.route("/user/<user_name>")
def user_page(user_name):
    return f"это страничка пользователя {user_name}"
