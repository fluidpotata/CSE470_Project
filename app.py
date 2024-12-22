import sqlite3

from flask import Flask, render_template, request
from models import User, Volunteer


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
            return render_template('dash.html', user=user)
        else:
            # return render_template('login.html', is_success=is_success)
            return render_template('login.html', msg={'class':'text-danger bg-warning','content':"Username or password incorrect"})



@app.route('/volunteer')
def volunteer():
    voln = Volunteer.getVolunteer(1)
    info = voln.getInfo()
    return render_template('vdash.html', voln=voln, info=info[0])


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



@app.route('/resources')
def resources_dashboard():
    resources = [
        {'id': 1, 'type': 'type', 'quantity': 15, 'location': 'Tangail'}
    ]
    return render_template('resources_dashboard.html', resources=resources, user=user)

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)




