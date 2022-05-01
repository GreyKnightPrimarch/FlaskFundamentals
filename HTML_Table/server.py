from flask import Flask, render_template
app = Flask(__name__)

users = [{
        'first_name': 'Michael',
        'last_name': 'Choi'
    },
    {
        'first_name': 'John',
        'last_name': 'Supsupin'
    },
    {
        'first_name': 'Mark',
        'last_name': 'Guillen'
    },
    {
        'first_name': 'KB',
        'last_name': 'Tonel'
    }
]
lene = len(users)

@app.route('/')
def main():
    return render_template("daTable.html", Users = users, iter = lene)

if __name__ == "__main__":
    app.run(debug = True)