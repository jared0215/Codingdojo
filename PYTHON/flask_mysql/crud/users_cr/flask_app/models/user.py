# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL

# Creating a class for the user table


class User:

    # Putitng our schema into a variable
    db = "users_schema"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Class methods to query our database
    @classmethod
    # Defines a method that will return a list of all the users in the database
    def get_all(cls):

        # Query that selects all the data from the users table
        query = "SELECT * FROM users;"

        # Call the function that will return an instance of a connection
        results = connectToMySQL('users_schema').query_db(query)

        # Create an empty list to append our instances of users
        users = []

        # Iterates over the db results and create instances of users with cls.
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    # Defines a method that saves a new user to the database
    def save(cls, data):

        # Query that inserts the data into the users table
        query = """
        INSERT INTO users (first_name, last_name, email, created_at, updated_at)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());
        """
        # Call the function that will return an instance of a connection
        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)
        return results

    # Get one user by id
    @classmethod
    def get_one(cls, id):
        data = {
            'id': id
        }
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])

    # UPDATE USER
    @classmethod
    def update(cls, data):
        query = """
        UPDATE users SET 
        first_name = %(first_name)s, 
        last_name = %(last_name)s, 
        email = %(email)s,
        updated_at = NOW() WHERE id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        return results

    # DELETE USER
    @classmethod
    def delete(cls, id):
        data = {
            'id': id
        }
        query = """
        DELETE FROM users WHERE id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        return results
