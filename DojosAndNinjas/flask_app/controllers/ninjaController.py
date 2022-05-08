from sqlalchemy import null
from flask_app import app
from flask import Flask, render_template, redirect, session, request
from flask_app.models.Ninjas import Ninja
from flask_app.models.Dojos import Dojo

@app.route('/')
def index():
    AllTheDojos = Dojo.getAll();
    length = len(AllTheDojos)
    return render_template('AllDojos.html', X=AllTheDojos, length=length)



@app.route('/createNinja/', methods=['post'])
def createNinja():
    data = {
        'firstName': request.form['firstName'],
        'lastName': request.form['lastName'],
        'email': request.form['email']
    }
    id = Ninja.save(data)  # id = so that we can use id to put the Ninja in session
    session['NinjaID'] = id
    session['DojoID']  = (Ninja.getOne(data2)).DojoID
    data2 = {'DojoID': id}
    # session['NinjaID'] = id # this just puts the Ninja in session so that we can use the id for creating the game NinjaID
    print("creating Ninja on controller file: ", id)
    return redirect('/dashboard/')

@app.route('/dashboard/')
def dashboard():
    print("the Ninja: ", session['NinjaID'])
    data = {
        'id': session['NinjaID']
    }
    theNinja = Ninja.getOne(data) # allowing us to display the sessioned Ninja
    theDojo = Dojo.getAll()
    return render_template('ParituclarDojo.html', Nin=theNinja, Do=theDojo)