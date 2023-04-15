from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, request
from flask_app.models import register
from datetime import datetime


# Creating a Tree class instance
class Tree:

    # Storing schema in a variable
    db = "users_trees"

    def __init__(self, data):
        self.id = data['id']
        self.species = data['species']
        self.location = data['location']
        self.reason = data['reason']
        self.date_planted = data['date_planted']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_id = data['users_id']

        self.creator = None

    @classmethod
    # SAVE TREE
    def save_tree(cls, data):
        # Query to save tree
        query = """
        INSERT INTO trees (species, location, reason, date_planted, users_id)
        VALUES (%(species)s, %(location)s, %(reason)s, %(date_planted)s, %(user_id)s);
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        return results

    @classmethod
    # GET ALL TREES WITH CREATOR
    def get_all_trees_with_creator(cls):
        query = """
            SELECT * FROM trees LEFT JOIN users ON trees.users_id = users.id;
        """
        results = connectToMySQL(cls.db).query_db(query)

        all_trees = []

        # Loop through the results
        for row in results:

            # Tree class instance from each db row
            one_tree = cls(row)

            # User class instance
            one_tree_author_info = {
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            }

            # Creating the User class instance
            author = register.User(one_tree_author_info)

            # Associating the User class instance with the Tree class instance
            one_tree.creator = author

            # Appending the Tree containing the associated User to list of trees
            all_trees.append(one_tree)

        return all_trees

    @classmethod
    # GET ALL TREES BY ID
    def get_tree_by_id(cls, data):
        # Query to get all trees by id
        query = """
        SELECT * FROM trees LEFT JOIN users ON trees.users_id = users.id WHERE trees.id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        print("Results:", results)

        if results:
            one_tree = cls(results[0])

            # User class instance
            one_tree_author_info = {
                'id': results[0]['users.id'],
                'first_name': results[0]['first_name'],
                'last_name': results[0]['last_name'],
                'email': results[0]['email'],
                'password': results[0]['password'],
                'created_at': results[0]['created_at'],
                'updated_at': results[0]['updated_at']
            }

            # Creating the User class instance
            author = register.User(one_tree_author_info)

            # Associating the User class instance with the Tree class instance
            one_tree.creator = author

            return one_tree
        else:
            return None

    @classmethod
    # DELETE TREES
    def delete_trees(cls, data):
        # Query to delete trees by ID
        query = """
        DELETE FROM trees WHERE id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        return results

    @classmethod
    # UPDATE TREES
    def update_trees(cls, data):
        # Query to update trees by ID
        query = """
        UPDATE trees SET species = %(species)s, location = %(location)s, reason = %(reason)s,
        date_planted = %(date_planted)s, users_id = %(user_id)s
        WHERE id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        return results

    @staticmethod
    # VALIDATE TREE
    def validate_tree(tree):
        # Making a variable to check if the tree is valid
        is_valid = True

        # Checks if the species name is empty
        if len(tree['species']) == 0:
            is_valid = False
            flash('Species Name is required')
        # Checks if the species name is less than 5 characters long
        elif len(tree['species']) < 5:
            is_valid = False
            flash('Species must be at least 5 characters long')

        # Checks if the location name is empty
        if len(tree['location']) == 0:
            is_valid = False
            flash('Location is required')
        # Checks if the location name is less than 2 characters long
        elif len(tree['location']) < 2:
            is_valid = False
            flash('Location must be at least 2 characters long')

        # Checks if the reason is empty
        if len(tree['reason']) == 0:
            is_valid = False
            flash('Reason is required')
        # Checks if the reason is greater than 50 characters long
        elif len(tree['reason']) > 50:
            is_valid = False
            flash('Reason must be less than 50 characters long')

        # Validates the date so that it cannot be set in the future
        date_planted = datetime.strptime(
            tree['date_planted'], '%Y-%m-%d').date()
        today = datetime.today().date()
        if date_planted > today:
            is_valid = False
            flash('Date Planted cannot be in the future')

        return is_valid
