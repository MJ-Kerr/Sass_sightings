from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import user_model
from flask import flash


class Sighting:
    def __init__(self, data):
        self.sight_id = data['sight_id']
        self.location = data['location']
        self.what_happened = data['what_happened']
        self.sight_date = data['sight_date']
        self.how_many = data['how_many']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users = None

    def print(self):
        print(self.sight_id)
        print(self.location)
        print(self.what_happened)
        print(self.sight_date)
        print(self.how_many)
        print(self.user_id)
        print(self.created_at)
        print(self.updated_at)
        print(self.users)

# ===================Create Sighting=====================


    @classmethod
    def create_sighting(cls, data):
        query = """
        INSERT INTO sightings
            (location,
            what_happened, 
            sight_date, 
            how_many, 
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
        # print(results)
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
            this_sighting.print()
        return list_of_sightings

# ================Get Sighting=====================

    @classmethod
    def get_sighting(cls,id):
        data ={
            'id': id,
        }
        query = """
        SELECT * FROM sightings
        JOIN users 
        ON users.id = sightings.user_id
        WHERE sight_id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            this_sighting = cls(results[0])
            # create user for sighting
            user_data = {
                **results[0],
                'created_at': results[0]['users.created_at'],
                'updated_at': results[0]['users.updated_at']
            }
            this_user = user_model.User(user_data)
            this_sighting.users = this_user
            return this_sighting
        else:
            return False


# =================Update Sighting=====================

    @classmethod
    def update(cls, data):
        query = """
        UPDATE sightings
        SET
            location = %(location)s, 
            what_happened = %(what_happened)s, 
            sight_date = %(sight_date)s, 
            how_many = %(how_many)s 
        WHERE sight_id = %(sight_id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)


# ================Delete Sighting=====================

    @classmethod
    def delete(cls, data):
        query = """
        DELETE FROM sightings
        WHERE sight_id = %(sight_id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)

# ================Validate Sighting=====================
    @staticmethod
    def val(data):
        is_valid =True

        if len(data['location']) == 0:
            is_valid = False
            flash('Location is required')

        if len(data['what_happened']) ==0 :
            is_valid = False
            flash('What happened is required')

        if len(data['sight_date']) == 0:
            is_valid = False
            flash('Sight date is required')

        if len(data['how_many']) ==0 :
            is_valid = False
            flash('How many is required')

        return is_valid

