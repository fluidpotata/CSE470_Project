import sqlite3
import os
from flask import Flask, render_template, request, flash, redirect, url_for
from models import User, Volunteer, Rcamp
from database import db, init_db
import logging

app = Flask(__name__)
app.secret_key = 'your-secret-key'
user = None

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app)


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

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
            return redirect(url_for('dashboard'))
        else:
            # return render_template('login.html', is_success=is_success)
            return render_template('login.html', msg={'class':'text-danger bg-warning','content':"Username or password incorrect"})

@app.route('/volunteer')
def volunteer():
    voln = Volunteer.getVolunteer(1)
    info = voln.getInfo()
    return render_template('dash.html', voln=voln, info=info)

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
        if is_success[0]:
            flash(is_success[1], 'success')
            return redirect(url_for('login'))
        else:
            flash(is_success[1],'danger')
            return redirect(url_for('signup'))



@app.route('/dashboard')
def dashboard():
    info = user.getInfo()
    return render_template('dash.html', user=user, info=info)


@app.route('/resources')
def resources_dashboard():
    resources = [
        {'id': 1, 'type': 'type', 'quantity': 15, 'location': 'Tangail'}
    ]
    return render_template('resources_dashboard.html', resources=resources, user=user)

@app.route('/rcamp', methods=['GET', 'POST'])
def r_camp_info(v_cap, v_occ):
    if request.method == 'GET':
        result = Rcamp.get_camp_status(v_id)
        return render_template('rcamp.html', rcamp=result)
    elif request.method == 'POST':
        return Rcamp.update_camp(v_cap, v_occ)

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
