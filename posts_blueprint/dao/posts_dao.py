import json


class PostsDAO:

    def __init__(self, path):
        self.path = path

    def get_posts_all(self):
        with open(self.path, encoding="utf-8") as file:
            posts = json.load(file)
        return posts

    def get_posts_by_user(self, user_name):
        posts = self.get_posts_all()
        posts_by_user = []
        user_count = 0
        for post in posts:
            if post["poster_name"] == user_name:
                user_count += 1
                posts_by_user.append(post)
        if user_count == 0:
            raise ValueError
        return posts_by_user

    def get_comments_by_post_pk(self, post_pk):
        with open("../../data/comments.json", encoding="utf-8") as file:
            comments = json.load(file)
        comments_by_post = []
        post_count = 0
        for comment in comments:
            if comment["post_pk"] == post_pk:
                comments_by_post.append(comment["comment"])
                post_count += 1
        if post_count == 0:
            raise ValueError
        return comments_by_post

    def search_for_posts(self, query):
        posts = self.get_posts_all()
        posts_by_search = []
        for post in posts:
            if query.lower() in post["content"].lower():
                posts_by_search.append(post)
        return posts_by_search

    def get_post_by_pk(self, pk):
        posts = self.get_posts_all()
        for post_by_pk in posts:
            if post_by_pk["pk"] == pk:
               return post_by_pk
