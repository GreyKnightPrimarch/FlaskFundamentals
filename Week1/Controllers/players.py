from flask import render_template, request
from flask_app import app
from flask_app.controllers import players

@app.route('/')
def Hello_World():
    return "Hello World"

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/players/create', method=['POST'])
def createplayer():
    request.form #Is a dictionary with key/value pairs from the form
    return render_template('user_info.html', user_name=request.form['user_name'],email=request.form['user_email'])

@app.route('/players/info')
def player_info():
    return render_template('user_info')