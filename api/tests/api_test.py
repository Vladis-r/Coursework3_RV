import pytest
from flask import jsonify

from api_views.views import api_posts_dao
from posts_blueprint.dao.posts_dao import PostsDAO


class TestApi:

    @pytest.fixture
    def posts_dao(self):
        return PostsDAO("data/data.json")

    @pytest.fixture
    def data_json_keys(self):
        return ["poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"]

    def test_type_api_posts(self, posts_dao):
        posts = jsonify(api_posts_dao.get_posts_all())
        assert type(posts) == list, "Посты должны передаваться списком"
