from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    db = 'dojos_and_ninjas_schema'
    def __init__(self, data):
        self.DojoID = data['DojoID']
        self.name = data['name']
        self.created_at = data['created_at']
        self.Updated_at = data['Updated_at']


    def thedojos(self):
        return f'{self.name}'

    @classmethod
    def getAll(cls):
        query = 'SELECT * from dojos;'
        results = connectToMySQL(cls.db).query_db(query)
        dojos = []
        for row in results:
            dojos.append(cls(row))
        return dojos

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * from dojos WHERE DojoID = %(DojoID)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO dojos (name) VALUES (%(name)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE dojos SET name=%(name)s WHERE DojoID = %(DojoID)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM dojos WHERE DojoID = %(DojoID)s;'
        return connectToMySQL(cls.db).query_db(query, data)