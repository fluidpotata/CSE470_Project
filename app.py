import os

from flask import Flask, render_template, request
from models.user import User  


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        is_success = User.authenticate(username, password)
        if is_success:
            return "Success" #User class creation here
        else:
            # return render_template('login.html', is_success=is_success)
            return "rejected"


@app.route('/signup')
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    elif request.method == 'POST':
        pass # will be done by mystics


if __name__ == '__main__':
    app.run(debug=True)

