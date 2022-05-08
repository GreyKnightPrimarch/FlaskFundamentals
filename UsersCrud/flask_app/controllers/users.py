from flask_app import app
from flask import Flask, render_template, redirect, session, request
from flask_app.models.user import User


@app.route('/')
def index():
    return render_template('addUser.html')

@app.route('/createUser/', methods=['post'])
def createUser():
    data = {
        'FristName': request.form['FristName'],
        'Lastname': request.form['Lastname'],
        'Email': request.form['Email'],
        'Description': request.form['Description']
    }
    id = User.save(data)  # id = so that we can use id to put the user in session
    session['user_id'] = id # this just puts the user in session so that we can use the id for creating the game user_id
    print("creating user on controller file: ", id)
    print(data)
    return redirect('/TableOfUsers/')

@app.route('/TableOfUsers/')
def TableOfUsers():
    tbl = User.getAll()
    l = len(tbl)
    return render_template('TableOfUsers.html', X=tbl, num=l)

@app.route('/user/<int:xid>')
def showuser(xid):
    session['user_id'] = xid
    aUser = User.getOne(xid)
    return render_template('ShowUser.html', X=aUser)


@app.route('/user/<int:xid>/Edit', methods=['post'])
def showuser(xid):
    session['user_id'] = xid
    data = {
        'FristName': request.form['FristName'],
        'Lastname': request.form['Lastname'],
        'Email': request.form['Email'],
        'Description': request.form['Description']
    }
    
    return render_template('/user/<int:xid>.html', X=aUser)
