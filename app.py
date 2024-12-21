<<<<<<< HEAD
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return '<h1>Welcome to the Volunteer and User Dashboard System</h1><p>Visit <a href="/resources">Resources Dashboard</a> to view resources.</p>'
=======
import os

from flask import Flask, render_template, request
from models.user import User  


app = Flask(__name__)
user = None

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    global user
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        is_success = User.authenticate(username, password)
        if is_success[0]:
            user = is_success[1]
            # return f"Success, welcome {user.name}" #User class creation here
            return render_template('vdash.html', user=user)
        else:
            # return render_template('login.html', is_success=is_success)
            return render_template('login.html', msg={'class':'text-danger bg-warning','content':"Username or password incorrect"})


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    elif request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        name = request.form['name']
        nid = request.form['nid']
        date_of_birth = request.form['dob']
        print(date_of_birth)
        address = request.form['address']
        password = request.form['password']
        contact = request.form['phone']
        blood_type = request.form['bloodgroup']
        is_success = User.registerUser(username, email, name, nid, date_of_birth, address, password, contact, blood_type)
        return is_success[1]
>>>>>>> 5bd6143b44b2413efc18c10326f9fb13f1bcea95

# Route to display the Resources Dashboard
@app.route('/resources')
def resources_dashboard():
    # Connect to SQLite database
    conn = sqlite3.connect('resources.db')  # Replace 'resources.db' with your database file name
    cursor = conn.cursor()

    # Query to fetch resources
    cursor.execute('SELECT id, type, quantity, location FROM resources')
    resources = [
        {'id': row[0], 'type': row[1], 'quantity': row[2], 'location': row[3]}
        for row in cursor.fetchall()
    ]
    
    conn.close()

    # Render the resources_dashboard.html template
    return render_template('resources_dashboard.html', resources=resources)

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)




