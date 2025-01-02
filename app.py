import sqlite3
import os
from flask import Flask, render_template, request, flash, redirect, url_for, session, make_response
from werkzeug.utils import secure_filename
from models import *
from database import db, init_db
import logging
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key'


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
            session['user'] = user.id
            session['role'] = user.role
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
    if 'user' in session:
        user = User.getUser(session['user'])
        info = user.getInfo()
        return render_template('dash.html', user = user, info=info)
    return redirect(url_for('login'))


@app.route('/makedonation', methods=['GET', 'POST'])
def makeDonation():
    if session.get('user') is not None:
        if request.method == 'POST':
            donorid = session['user']
            method = request.form['method']
            amount = request.form['amount']
            date = datetime.now().strftime('%m-%d-%Y')
            tid = request.form['tid']
            Donation.add_donation(method, donorid, amount, date, tid)
            return redirect(url_for('dashboard'))
        return render_template('makedonation.html')
    return redirect(url_for('login'))


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

@app.route('/donateblood', methods = ["GET", "POST"])
def donateblood():
    if session.get('user') is None:
        return redirect(url_for('login'))
    id = session['user']
    result = User.donate_blood(id)
    return redirect(url_for('dashboard'))


@app.route('/bloodavailability', methods=['GET', 'POST'])
def bloodavailability():
    if request.method == 'GET':
        user = User.getAlluser()
        return render_template('bloodavailability.html', user=user)
    elif request.method == 'POST':
        bloodgroup = request.form['bloodgroup']
        location = request.form['location']
        is_success = User.filter_bloodbank(bloodgroup, location)
        return render_template('bloodavailability.html', user=is_success)



@app.route('/missingperson', methods=['GET', 'POST'])
def missingperson():
    if request.method == 'GET':
        return render_template('registermissing.html')
    elif request.method == 'POST':
        name = request.form['personName']
        last_seen = request.form['lastSeen']
        contact_number = request.form['contactNumber']
        photo = request.files['uploadPhoto'].read()

        mperson = MissingPerson(name, last_seen, contact_number, photo)
        is_success = mperson.registerMissing()

        if is_success:
            flash('Missing person report submitted successfully.', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Failed to submit the missing person report.', 'danger')
            return render_template('registermissing.html')


@app.route('/viewmissing', methods=['GET', 'POST'])
def viewmissing():
    missingpersons = MissingPerson.getMissingPersons()
    return render_template('showmissingpersons.html', missingpersons=missingpersons)

@app.route('/photo/<int:person_id>')
def serve_photo(person_id):
    person = MissingPerson.getMissingPersonByParam(id=person_id)
    photo_data = person.photo  # Assume this is the binary data
    
    # Serve image as response
    response = make_response(photo_data)
    response.headers.set('Content-Type', 'image/jpeg')  # Adjust if PNG or other format
    return response

@app.route('/logout' , methods=['GET', 'POST'])
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
