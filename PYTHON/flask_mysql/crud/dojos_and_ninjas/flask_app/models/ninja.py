from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:

    db = "dojos_and_ninjas_schema"

    def __init__(self, data):
        self.id = data['id']
        self.dojo_id = data['dojo_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    # Defines a method that will return a list of all the ninjas in the database
    def get_all_ninja(cls):

        # Query that selects all the data from the ninjas table
        query = "SELECT * FROM ninjas;"

        # Call the function that will return an instance of a connection
        results = connectToMySQL(cls.db).query_db(query)

        # Create an empty list to append our instances of ninjas
        ninjas = []

        # Iterates over the db results and create instances of ninjas with cls.
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas

    @classmethod
    # Defines a method that saves a new user to the database
    def save_ninja(cls, data):

        # Query that inserts the data into the users table
        query = """
        INSERT INTO ninjas (dojo_id, first_name, last_name, age, created_at, updated_at)
        VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s, NOW(), NOW());
        """
        # Call the function that will return an instance of a connection
        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)
        return results

    # UPDATE ninja
    @classmethod
    def update(cls, data):
        query = """
        UPDATE ninjas SET 
        first_name = %(first_name)s, 
        last_name = %(last_name)s, 
        age = %(age)s,
        updated_at = NOW() WHERE id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        return results

    # DELETE NINJA
    @classmethod
    def delete(cls, id):
        data = {
            'id': id
        }
        query = """
        DELETE FROM ninjas WHERE id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        return results

    # Get one ninja by id

    @classmethod
    def get_one_ninja(cls, id):
        data = {
            'id': id
        }
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])

    # Get all ninjas by dojo
    @classmethod
    def get_ninjas_by_dojo(cls, dojo_id):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(dojo_id)s;"
        data = {'dojo_id': dojo_id}
        results = connectToMySQL(cls.db).query_db(query, data)
        ninjas = []
        for row in results:
            ninjas.append(cls(row))
        return ninjas

    # Gets the dojo id from a ninja
    @classmethod
    def get_dojo_id(cls, id):
        data = {
            'id': id
        }
        query = "SELECT dojo_id FROM ninjas WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)

        # Check if the results are not empty
        if len(results) > 0:
            return results[0]['dojo_id']
        else:
            return None
