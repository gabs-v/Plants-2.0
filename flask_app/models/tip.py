from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Tip:
    db_name = 'plants_schema'
    def __init__(self,db_data):
        self.id = db_data['id']
        self.tip = db_data['tip']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.user_id = db_data['user_id']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO tips (tip, user_id) VALUES (%(tip)s,%(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM tips;"
        results = connectToMySQL(cls.db_name).query_db(query)
        all_tips =[]
        for row in results:
            print(row['tip'])
            all_tips.append(cls(row))
        return all_tips

    

    @classmethod
    def update(cls, data):
        query = "UPDATE tips SET tip=%(tip)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM tips WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls( results[0] )

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM tips WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @staticmethod
    def validate_tip(tip):
        is_valid = True
        if len(tip['tip']) < 2:
            is_valid = False
            flash("Please enter a tip!","tip")
        return is_valid