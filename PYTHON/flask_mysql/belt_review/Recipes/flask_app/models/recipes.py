from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, request
from flask_app.models import register
from datetime import datetime


# Creating a class for recipes
class Recipe:

    # Adding our schema to a variable to make life easier
    db = "myrecipes"

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.cooked_date = data['cooked_date']
        self.cooked_in_30 = data['cooked_in_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_id = data['users_id']

        # Empty place to store all recipes that a single user created
        self.creator = None

    # SAVE RECIPE
    @classmethod
    def save_recipe(cls, data):
        # Query to save the recipe
        query = """
        INSERT INTO recipes (name, description, instructions, cooked_date, cooked_in_30, users_id)
        VALUES (%(name)s, %(description)s, %(instructions)s, %(cooked_date)s, %(cooked_in_30)s, %(user_id)s);
        """
        results = connectToMySQL(cls.db).query_db(query, data)

        return results

    # GET ALL RECIPES
    @classmethod
    def get_all_recipes_with_creator(cls):
        # Query to get all recipes and their associated User
        query = """
        SELECT * FROM recipes Join users on recipes.users_id = users.id;
        """
        results = connectToMySQL("myrecipes").query_db(query)

        all_recipes = []

        # Loop through the results
        for row in results:

            # Recipe class instance from each db row
            one_recipe = cls(row)

            # User class instance
            one_recipe_author_info = {
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            }

            # Creating the User class instance
            author = register.User(one_recipe_author_info)

            # Associating the User class instance with the Recipe class instance
            one_recipe.creator = author

            # Appending the Recipe containing the associated User to list of recipes
            all_recipes.append(one_recipe)

        return all_recipes

    # GET ALL RECIPES BY ID
    @classmethod
    def get_recipe_by_id(cls, data):
        query = """
        SELECT * FROM recipes WHERE id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, data)

        if results:
            return cls(results[0])
        else:
            return None

    # DELETE RECIPE
    @classmethod
    def delete_recipe(cls, data):
        query = """
        DELETE FROM recipes WHERE id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        return results

    # UPDATE RECIPE
    @classmethod
    def update_recipe(cls, data):
        query = """
        UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, 
        cooked_date = %(cooked_date)s, cooked_in_30 = %(cooked_in_30)s 
        WHERE id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        return results

    # Static Method that validates the recipe

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True

        # Valdates the name so that it cannot be empty and or contain less than 3 characters
        if len(recipe['name']) == 0:
            is_valid = False
            flash('Recipe name cannot be empty')
        elif len(recipe['name']) < 3:
            is_valid = False
            flash('Recipe name must be at least 3 characters long')

        # Valdates the description so that it cannot be empty and or contain less than 3 characters
        if len(recipe['description']) == 0:
            is_valid = False
            flash('Recipe description cannot be empty')
        elif len(recipe['description']) < 3:
            is_valid = False
            flash('Recipe description must be at least 3 characters long')

        # Valdates the instructions so that it cannot be empty and or contain less than 3 characters
        if len(recipe['instructions']) == 0:
            is_valid = False
            flash('Recipe instructions cannot be empty')
        elif len(recipe['instructions']) < 3:
            is_valid = False
            flash('Recipe instructions must be at least 3 characters long')

        # Validates the date so that it cannot be in the future
        cooked_date = datetime.strptime(
            recipe['cooked_date'], '%Y-%m-%d').date()
        today = datetime.today().date()
        if cooked_date > today:
            is_valid = False
            flash('Cooked date cannot be in the future')

        return is_valid
