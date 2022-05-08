from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db = 'usersdb'
    def __init__(self, data):
        self.UserID = data['UserID']
        self.FristName = data['FristName']
        self.Lastname = data['Lastname']
        self.Email = data['Email']
        self.CreatedAt = data['CreatedAt']
        self.UpdatedAt = data['UpdatedAt']
        self.Description = data['Description']
    
    def fullName(self):
        return f'{self.FristName} {self.Lastname}'

    @classmethod
    def getAll(cls):
        query = 'SELECT * from users;'
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * from users WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO users (FristName, LastName, Email, Description) VALUES (%(FristName)s, %(LastName)s, %(Email)s, %(Description)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def UpdateOne(cls, data):
        query = 'Update users Set FristName=%(FristName)s, LastName=%(LastName)s, Email%(Email)s, Description=%(Description)s) where UserID=%(UserID)s;'
        return connectToMySQL(cls.db).query_db(query, data)


    @classmethod
    def update():
        pass

    @classmethod
    def delete(cls, data):
        query = 'Delete from users where id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)
