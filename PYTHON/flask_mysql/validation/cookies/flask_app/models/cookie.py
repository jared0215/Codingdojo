from flask_app.config.mysqlconnection import connectToMySQL


class Order:

    db = "cookie_schema"

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.cookie = data['cookie']
        self.boxes = data['boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):

        # Selects all orders from the database
        query = "SELECT * FROM orders"

        # Connects to the database
        results = connectToMySQL(cls.db).query_db(query)

        # Created an empty list to store the orders
        orders = []

        # Loops through the results and appends them to the orders list
        for row in results:
            orders.append(cls(row))
        return orders

    @classmethod
    def save(cls, data):

        # Saves the order to the database
        query = """
        INSERT INTO orders (name, cookie, boxes)
        VALUES (%(name)s, %(cookie)s, %(boxes)s)
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        return results

    @classmethod
    def update(cls, data):
        query = """UPDATE orders 
        SET name = %(name)s, cookie = %(cookie)s, boxes = %(boxes)s WHERE id = %(id)s"""
        results = connectToMySQL(cls.db).query_db(query, data)
        return results

    @classmethod
    def get_by_id(cls, id):
        data = {
            'id': id
        }
        query = """SELECT * FROM orders WHERE id = %(id)s"""
        results = connectToMySQL(cls.db).query_db(query, {'id': id})
        return cls(results[0])
