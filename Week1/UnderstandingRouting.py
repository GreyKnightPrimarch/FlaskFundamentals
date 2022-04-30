from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)  

@app.route("/")
def hello_world():
    return 'Hello World!'

@app.route("/dojo")
def SayDojo():
    return 'Dojo!'

@app.route("/say/<thing>")
def SayThing(thing):
    s = "Hello "+thing+"!"
    return s;

@app.route("/repeat/<inte>/<thing>")
def RepeatThing(inte, thing):
    s=thing+" "
    t=""
    for i in range (0,int(inte)):
        t+=s;
    return t;


if __name__=="__main__":
    app.run(debug=True)