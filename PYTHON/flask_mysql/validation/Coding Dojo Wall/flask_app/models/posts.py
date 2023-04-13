from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, request
from flask_app.models import register

# Creating a Post Class


class Post:

    db = "register"

    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_id = data['users_id']

        self.creator = None

    # Method to get a post from the database that belongs to a specific user

    @classmethod
    def get_all_posts_with_creator(cls):

        query = "SELECT * FROM posts JOIN users ON posts.users_id = users.id ORDER BY posts.created_at DESC"
        results = connectToMySQL(cls.db).query_db(query)

        all_posts = []

        for row in results:
            one_post = cls(row)

            one_post_author_info = {
                "id": row['users.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "password": row['password'],
                "created_at": row['created_at'],
                "updated_at": row['updated_at']
            }

            author = register.User(one_post_author_info)

            one_post.creator = author

            all_posts.append(one_post)

        return all_posts

    # Method that saves a post to the database

    @classmethod
    def save(cls, data):
        query = "INSERT INTO posts (content, users_id) VALUES (%(content)s, %(user_id)s);"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    # Method that deletes a post to the database

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM posts WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    #  Method that gets a post from the database by the ID

    @classmethod
    def get_post_by_id(cls, data):
        query = "SELECT * FROM posts WHERE id = %(id)s"
        results = connectToMySQL(cls.db).query_db(query, data)

        if results:
            return cls(results[0])
        else:
            return None
