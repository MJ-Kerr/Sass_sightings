from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import user_model


class Sighting:
    def __init__(self, data):
        self.sight_id = data['id']
        self.location = data['location']
        self.what_happened = data['what_happened']
        self.sight_date = data['sight_date']
        self.how_many = data['how_many']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


# ===================Create Sighting=====================


    @classmethod
    def create_sighting(cls, data):
        query = """
        INSERT INTO sightings
            (location,
            what_happened, 
            sight_date, 
            how_may, 
            user_id)
        VALUES 
            (%(location)s, 
            %(what_happened)s, 
            %(sight_date)s, 
            %(how_many)s, 
            %(user_id)s)
        """
        return connectToMySQL(DATABASE).query_db(query, data)

# =================Get All Sightings=====================

    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM sightings
        JOIN users
        ON users.id = sightings.user_id;
        """
        results = connectToMySQL(DATABASE).query_db(query)
        # print(results)
        list_of_sightings = []
        for  row in results:
            this_sighting = cls(row)
            # create user for sighting
            user_data = {
                **row,
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at']
            }
            this_user = user_model.User(user_data)
            this_sighting.users = this_user
            list_of_sightings.append(this_sighting)
            print(this_sighting)
        return list_of_sightings


