# Imports
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, request
import re

# Email format validation
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Creating a User Class


class User:

    # Adding our schema to a variable
    db = "myrecipes"

    # Constructor for the User Class
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.recipes = []

    # Method gets all the users from the database

    @classmethod
    def get_all(cls):

        query = "SELECT * FROM users"

        results = connectToMySQL(cls.db).query_db(query)

        users = []

        for row in results:
            users.append(cls(row))
        return users

    # Method saves a user to the database

    @classmethod
    def save(cls, data):

        query = """
        INSERT INTO users (first_name, last_name, email, password) 
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        return results

    # Method gets a user by email

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])

    # Method validates a users inputs during login and Registration

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['f_name']) < 2:
            flash("First name must be at least 2 characters long", "register_error")
            is_valid = False
        if len(user['l_name']) < 2:
            flash("Last name must be at least 2 characters long", "register_error")
            is_valid = False
        if len(user['email']) < 1:
            flash("Email cannot be empty", "register_error")
            is_valid = False
        if not user['password']:
            flash("Password cannot be empty", "register_error")
            is_valid = False
        elif len(user['password']) < 8:
            flash("Password must be at least 8 characters long", "register_error")
            is_valid = False
        elif not re.search(r'^(?=.*[A-Z])(?=.*\d)', request.form['password']):
            flash(
                'Password must contain at least one uppercase letter and one digit', 'register_error')
            is_valid = False
        if request.form['confirm'] != user['password']:
            flash("Passwords do not match", "register_error")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email", "register_error")
            is_valid = False
        if User.unique_email(user['email']):
            flash("Email is already in use", "register_error")
            is_valid = False
        return is_valid

    # Makes sure that the email is not already in use

    @staticmethod
    def unique_email(email):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('myrecipes').query_db(
            query, {'email': email})
        if len(results) > 0:
            return True
        return False

    # Method gets a user by their first and last name

    @staticmethod
    def get_name(cls, data):
        query = "SELECT first_name, last_name FROM users WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])
