from flask import Flask, render_template, request, redirect, session
from sqlalchemy import true
app = Flask(__name__)

app.secret_key = 'The new lion king is a bad bad bad movie'
counter = 0;

@app.route('/')
def main():
    if "count" not in session:
        session["counter"] = 0
    else:
        session['counter'] += 1
    return render_template("LaCounter.html", c=session['counter'])

@app.route('/c1', methods=['POST'])
def clickC1():
    t = keycheck(session)
    print("Got Post Info")
    print(request.form)
    print(session)
    session['counter']+=1
    # Never render a template on a POST request.
    # Instead we will redirect to our index route.
    return redirect('/')

@app.route('/cx', methods=['POST'])
def clickCx():
    t = keycheck(session)
    print("Got Post Info")
    print(request.form)
    print(session)
    session['counter']+= (int)(request.form['number'])
    # Never render a template on a POST request.
    # Instead we will redirect to our index route.
    return redirect('/')

@app.route('/reset', methods=['POST'])
def clickReset():
    t = keycheck(session)
    session['counter']=0
    # Never render a template on a POST request.
    # Instead we will redirect to our index route.
    return redirect('/')

def keycheck(session):
    if 'key_name' in session:
        print('key exists!')
        return true
    else:
        print("key 'key_name' does NOT exist")
        return False

if __name__ == "__main__":
    app.run(debug = True)