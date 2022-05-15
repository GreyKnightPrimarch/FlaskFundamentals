from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db = 'logins'
    def __init__(self, data):
        self.idUser = data['idUser']
        self.Email = data['Email']
        self.password = data['password']
        self.firstname = data['firstname']
        self.lastname = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    
    
    @staticmethod
    def Validate(user):
        def containsNumber(value):
            f = re.search('[0-9]', value)
            return (not(f==None))
        
        def containsLowerCase(value):
            f =re.search('[a-z]', value)
            return (not(f==None))
        
        def containsUpperCase(value):
            f =re.search('[A-Z]', value)
            return (not(f==None))
        
        check =True
        query = 'Select * from user where email = %(Email)s'
        results = connectToMySQL(User.db).query_db(query, user)
        if len(results) >=1:
            check = False
            flash("that email already exists, choose another or login")
        
        if not EMAIL_REGEX.match(user['email']):
            check = False
            flash("that email already exists, choose another or login")
        
        if len(user['lastName']) < 3:
            check = False
            flash("Please use at least 3 characters for last name")
            
        if len(user['firstName']) < 2:
            check = False
            flash("Please use at least 3 characters for first name")
        
        if len(user['password']) < 8:
            check = False
            flash("Password must be at least 8 characters long")
        
        if(not(containsNumber(user['password']))):
            check = False
            flash("Password must contain a number")
        
        if(not(containsLowerCase(user['password']))):
            check = False
            flash("Password must contain a lower case letter")
        
        if(not(containsUpperCase(user['password']))):
            check = False
            flash("Password must contain a upperr case letter")
            
        if( user['password'] != user['passwordconfirm']):
            check = False
            flash("Passwords do not match")
        return check
            
    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM user;'
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users
    
    @classmethod
    def getOne(cls, data):
        query = "SELECT * FROM user WHERE idUser = %(idUser)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def getEmail(cls, data):
        query = "SELECT * FROM user WHERE Email = %(Email)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO user (firstName, lastName, email, password) VALUES (%(firstName)s, %(lastName)s, %(Email)s, %(password)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'Update user set firstName=%(firstName)s, lastName = %(lastName)s, email = %(Email)s, password=%(password)s) where idUser = %(idUser)s;'
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def getEmail(cls, data):
        query = "SELECT * from user where email = %(Email)s;"
        #s=data["Email"]
        #s = f'{s}'
        #print(query, s)
        result = connectToMySQL(cls.db).query_db(query, data)
        #print(result)
        if (len(result)) <1:
            return False
        return cls(result[0])

    @classmethod
    def delete(cls, data):
        pass