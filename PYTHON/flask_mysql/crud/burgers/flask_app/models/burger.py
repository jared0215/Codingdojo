from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import topping
from flask import flash

# burger.py


class Burger:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.bun = data['bun']
        self.meat = data['meat']
        self.calories = data['calories']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # We now create a list so that later we can add in all the topping objects that relate to a burger.
        self.toppings = []

    @classmethod
    def save(cls, data):
        query = "INSERT INTO burgers ( name , bun, meat, calories, restaurants_id, created_at , updated_at ) VALUES (%(name)s, %(bun)s, %(meat)s, %(calories)s, %(restaurants_id)s,NOW(),NOW());"
        return connectToMySQL('burgers').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM burgers;"
        burgers_from_db = connectToMySQL('burgers').query_db(query)
        burgers = []
        for b in burgers_from_db:
            burgers.append(cls(b))
        return burgers

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM burgers WHERE burgers.id = %(id)s;"
        burger_from_db = connectToMySQL('burgers').query_db(query, data)

        return cls(burger_from_db[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE burgers SET name=%(name)s, bun=%(bun)s, meat=%(meat)s, calories=%(calories)s,updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('burgers').query_db(query, data)

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM burgers WHERE id = %(id)s;"
        return connectToMySQL('burgers').query_db(query, data)

    # This method will retrieve the burger with all the toppings that are associated with the burger.

    @classmethod
    def get_burger_with_toppings(cls, data):
        query = "SELECT * FROM burgers LEFT JOIN add_ons ON add_ons.burger_id = burgers.id LEFT JOIN toppings ON add_ons.topping_id = toppings.id WHERE burgers.id = %(id)s;"
        results = connectToMySQL('burgers').query_db(query, data)
        # results will be a list of topping objects with the burger attached to each row.
        burger = cls(results[0])
        for row_from_db in results:
            # Now we parse the topping data to make instances of toppings and add them into our list.
            topping_data = {
                "id": row_from_db["toppings.id"],
                "topping_name": row_from_db["topping_name"],
                "created_at": row_from_db["toppings.created_at"],
                "updated_at": row_from_db["toppings.updated_at"]
            }
            burger.toppings.append(topping.Topping(topping_data))
        return burger

    @classmethod
    def update_toppings(cls, data):
        # Delete all existing add_ons for the burger
        query = "DELETE FROM add_ons WHERE burger_id = %(burger_id)s;"
        connectToMySQL('burgers').query_db(query, data)

        # Add the new toppings for the burger
        for topping_id in data['topping_ids']:
            query = "INSERT INTO add_ons (burger_id, topping_id) VALUES (%(burger_id)s, %(topping_id)s);"
            connectToMySQL('burgers').query_db(
                query, {'burger_id': data['burger_id'], 'topping_id': topping_id})

    @staticmethod
    def validate_burger(burger):
        is_valid = True  # we assume this is true
        if len(burger['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(burger['bun']) < 3:
            flash("Bun must be at least 3 characters.")
            is_valid = False
        if int(burger['calories']) < 200:
            flash("Calories must be 200 or greater.")
            is_valid = False
        if len(burger['meat']) < 3:
            flash("Bun must be at least 3 characters.")
            is_valid = False
        return is_valid
