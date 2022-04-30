from distutils.log import debug
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play/<x>/<colour>')
def hello_world(x, colour):
    x = int(x)
    return render_template('play.html', times=x, phrase=colour)

if __name__=="__main__":
    app.run(debug=True)