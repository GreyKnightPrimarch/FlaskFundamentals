
from flask import Flask, render_template, request, redirect, session
from sqlalchemy import true
app = Flask(__name__)

app.secret_key="Alex Moriarti - Nausicaa: easily a beloved classic all should enjoy and never forgotten! "

locations = ['Chicago', 'Los_Angeeles', 'Online', 'Tokyo', 'Seattle', 'Carnival', 'Unknown']
languages = ['C#', 'C++', 'Java', 'Python', 'Stupid-Go', 'Bash', 'Perl', 'HTML-CSS', 'Swiftard']
@app.route('/')
def main():
    loN=len(locations)
    laN=len(languages)
    return render_template("survey.html", lo=locations, a=loN, la=languages, b=laN)

@app.route('/SurveyComplete', methods=['POST'])
def SurveyComplete():
    session['name'] = request.form['nameInput']
    session['location'] = request.form['locations']
    session['language'] = request.form['languages']
    session['comment'] = request.form['comment']
    return redirect('/UserResult')

@app.route('/UserResult')
def success():
    return render_template('UserResult.html')

if __name__ == "__main__":
    app.run(debug = True)