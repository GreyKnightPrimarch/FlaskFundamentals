from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    db = 'dojos_and_ninjas_schema'
    def __init__(self, data):
        self.NinjaID = data['NinjaID']
        self.firstName = data['firstName']
        self.lastName = data['lastName']
        self.age = data['age']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.Dojo_DojoID = data['Dojo_DojoID']
    
    def fullName(self):
        return f'{self.firstName} {self.lastName}'

    @classmethod
    def getAll(cls):
        query = 'SELECT * from ninjas;'
        results = connectToMySQL(cls.db).query_db(query)
        ninjas = []
        for row in results:
            ninjas.append(cls(row))
        return ninjas

    @classmethod
    def getAllofDojo(cls,data):
        query = 'SELECT * from ninjas WHERE Dojo_DojoID = %(Dojo_DojoID)s;'
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        ninjas = []
        for row in results:
            ninjas.append(cls(row))
        return ninjas

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * from ninjas WHERE NinjaID = %(NinjaID)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def update(cls, data):
        query = 'UPDATE dojos SET firstName=%(firstName)s, lastName=%(lastName)s, age=%(age)s, Dojo_DojoID=%(Dojo_DojoID)s   WHERE NinjaID = %(NinjaID)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO ninjas (firstName, lastName, age, Dojo_DojoID) VALUES (%(firstName)s, %(lastName)s, %(age)s, %(Dojo_DojoID)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update():
        pass

    @classmethod
    def delete():
        pass
