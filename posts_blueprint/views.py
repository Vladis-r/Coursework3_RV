from flask import Blueprint, render_template
import logging

from .dao.posts_dao import PostsDAO
import logger

logger_posts = logging.getLogger("logs_posts")

posts_blueprint = Blueprint("posts_blueprint", __name__, template_folder="templates")
posts_dao = PostsDAO("data/data.json")


@posts_blueprint.route("/")
def posts_page():
    """Главная страница со всеми постами"""
    try:
        logger_posts.debug(f"Получаем все посты на странице /")
        posts = posts_dao.get_posts_all()
        return render_template("index.html", posts=posts)
    except Exception:
        return logger_posts.debug(f"Произошла ошибка при запросе к главной /")


@posts_blueprint.route("/post/<int:post_pk>")
def post_page(post_pk):
    """Страница поста по его номеру"""
    try:
        logger_posts.debug(f"Получаем пост {post_pk} на странице /post/{post_pk}")
        post = posts_dao.get_post_by_pk(post_pk)
        logger_posts.debug(f"Получаем комментарии для поста {post_pk} на странице /post/{post_pk}")
        comments = posts_dao.get_comments_by_post_pk(post_pk)
        len_comments = len(comments)
        return render_template("post.html", post=post, comments=comments, len_comments=len_comments)
    except Exception:
        return logger_posts.debug(f"Произошла ошибка при получении поста {post_pk}")


@posts_blueprint.route("/search/<query>")
def search_page(query):
    """Страница с постами по поиску"""
    try:
        logger_posts.debug(f"Получаем посты по поиску: {query} на странице /search/{query}")
        posts_by_search = posts_dao.search_for_posts(query)
        len_posts = len(posts_by_search)
        return render_template("search.html", posts_by_search=posts_by_search, len_posts=len_posts)
    except Exception:
        return logger_posts.debug(f"Произошла ошибка при попытке поиска {query}")


@posts_blueprint.route("/user/<user_name>")
def user_page(user_name):
    """Страница с постами по имени пользователя"""
    try:
        logger_posts.debug(f"Получаем посты по имени пользователя: {user_name} на странице /user/{user_name}")
        posts_by_user = posts_dao.get_posts_by_user(user_name)
        return render_template("user-feed.html", posts_by_user=posts_by_user)
    except Exception:
        return logger_posts.debug(f"Произошла ошибка при получении странички пользователя {user_name}")
