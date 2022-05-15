from sqlalchemy import null
from flask_app import app
from flask import Flask, render_template, flash, redirect, session, request
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('Login.html')

@app.route('/UserRegister/', methods=['post'])
def Login():
    data = {
        'firstName': request.form['firstName'],
        'lastName': request.form['lastName'],
        'email': request.form['email'],
        'password': request.form['password'],
        'passwordconfirm': request.form['passwordconfirm']
    }
    id = User.save(data)  
    if not id:
        flash("Unknown Error")
        return redirect('/')
    else :
        session['idUser'] = id

@app.route('/UserLogin/', methods=['post'])
def LoginRedirect():
    data = {
        'Email': request.form['Email'],
    }
    auser = User.getEmail(data)  
    if not auser:
        print("yuewfhhfew: ",auser)
        flash("Email is not registered, please register or check email")
        return render_template('Login.html')
    if not bcrypt.check_password_hash(auser.password, request.form['password']):
        flash("You got the wrong password")
        return render_template('Login.html')
    session['idUser'] = auser.idUser
    s = f'Welcome back {auser.firstname}'
    flash(s)
    return redirect('/Welcome')

@app.route('/Welcome/')
def Register():
    if (session['idUser'] is null):
        flash("Login needed")
        redirect('/')
    data = {
        'idUser': session['idUser']
    }
    theUser = User.getOne(data)
    return render_template('Welcome.html', X=theUser)