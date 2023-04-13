from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import register

# Creating a Class for our Comments


class Comment:

    db = "register"

    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_id = data['users_id']
        self.posts_id = data['posts_id']
        self.creator = None

    # Method to save the comment

    @classmethod
    def save_comment(cls, data):
        query = """
        INSERT INTO comments (content, users_id, posts_id)
        VALUES (%(content)s, %(users_id)s, %(posts_id)s)
        """
        return connectToMySQL(cls.db).query_db(query, data)

    # Method to get all the comments, joins them with the users
    @classmethod
    def get_all_comments(cls, data):

        query = """
        SELECT * FROM comments 
        JOIN users ON comments.users_id = users.id 
        WHERE posts_id = %(posts_id)s 
        ORDER BY comments.created_at ASC
        """
        results = connectToMySQL(cls.db).query_db(query, data)

        comments = []

        for row in results:
            one_comment = cls(row)

            one_comment_author_info = {
                "id": row['users.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "password": row['password'],
                "created_at": row['created_at'],
                "updated_at": row['updated_at']
            }

            author = register.User(one_comment_author_info)

            one_comment.creator = author

            comments.append(one_comment)

        return comments
