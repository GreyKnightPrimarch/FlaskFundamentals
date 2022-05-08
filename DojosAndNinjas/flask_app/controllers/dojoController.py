from sqlalchemy import null
from flask_app import app
from flask import Flask, render_template, redirect, session, request
from flask_app.models.Dojos import Dojo
from flask_app.models.Ninjas import Ninja


@app.route('/ShowDojo/<int:xid>', methods=['post'])
def createGame(xid):
    session['DojoID'] = xid
    return redirect('/ParituclarDojo/')

@app.route('/ParituclarDojo/')
def createGame():
    if(session['DojoID'] ==null):
        return redirect('/')
    data = {
        'DojoID': session['DojoID'] 
    }
    raw = Ninja.getAllofDojo(data) # no need to set a variable here as we are just saving to the database we don't need this in session
    return redirect('/ParituclarDojo.html/', Nin=raw)

@app.route('/createDojo', methods=['POST'])
def createDojo():
    data = {
        'name' : request.form['dojoName']
    }
    session['DojoID'] = Dojo.save(data)
    return render_template('AllDojos.html')