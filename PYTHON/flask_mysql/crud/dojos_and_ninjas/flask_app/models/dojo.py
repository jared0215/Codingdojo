from flask_app.config.mysqlconnection import connectToMySQL


class Dojo():

    db = "dojos_and_ninjas_schema"

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']

    # Class methods to query our database

    @classmethod
    # Defines a method that will return a list of all the dojos in the database
    def get_all(cls):

        # Query that selects all the data from the dojos table
        query = "SELECT * FROM dojos;"

        # Call the function that will return an instance of a connection
        results = connectToMySQL(cls.db).query_db(query)

        # Create an empty list to append our instances of dojos
        dojos = []

        # Iterates over the db results and create instances of users with cls.
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    # SAVE
    @classmethod
    # Defines a method that saves a new dojo to the database
    def save(cls, data):

        # Query that inserts the data into the dojos table
        query = """
        INSERT INTO dojos (name, created_at, updated_at)
        VALUES (%(name)s, NOW(), NOW());
        """
        # Call the function that will return an instance of a connection
        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)
        return results

    @classmethod
    def get_one(cls, id):
        data = {
            'id': id
        }
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_ninjas_by_dojo(cls, dojo_id):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(dojo_id)s;"
        data = {'dojo_id': dojo_id}
        results = connectToMySQL(cls.db).query_db(query, data)
        ninjas = []
        for row in results:
            ninjas.append(cls(row))
        return ninjas
