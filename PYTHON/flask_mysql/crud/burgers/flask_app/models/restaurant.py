# We need to import the burger class from our models
from ..models.burger import Burger
from flask_app.config.mysqlconnection import connectToMySQL


class Restaurant:
    ...

    @classmethod
    def get_restaurant_with_burgers(cls, data):
        query = "SELECT * FROM restaurants LEFT JOIN burgers ON burgers.restaurant_id = restaurants.id WHERE restaurants.id = %(id)s;"
        results = connectToMySQL('burgers').query_db(query, data)
        # results will be a list of topping objects with the burger attached to each row.
        restaurant = cls(results[0])
        for row_from_db in results:
            # Now we parse the burger data to make instances of burgers and add them into our list.
            burger_data = {
                "id": row_from_db["burgers.id"],
                "name": row_from_db["burgers.name"],
                "bun": row_from_db["bun"],
                "meat": row_from_db["meat"],
                "calories": row_from_db["calories"],
                "created_at": row_from_db["burgers.created_at"],
                "updated_at": row_from_db["burgers.updated_at"]
            }
            restaurant.burgers.append(Burger.Burger(burger_data))
        return restaurant
