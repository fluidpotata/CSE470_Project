<<<<<<< HEAD
from . import db  


class User(db.Model):
    __tablename__ = 'user'  

    
    userid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    nid = db.Column(db.String(50), unique=True, nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    address = db.Column(db.String(200), nullable=True)
    password = db.Column(db.String(200), nullable=False)
    contact = db.Column(db.String(20), nullable=False)
    blood_type = db.Column(db.String(5), nullable=True)

   
    def __init__(self, username, name, nid, date_of_birth, email, address, password, contact, blood_type):
        self.username = username
        self.name = name
        self.nid = nid
        self.date_of_birth = date_of_birth
        self.email = email
        self.address = address
        self.password = password
        self.contact = contact
        self.blood_type = blood_type

   
    def __repr__(self):
        return f'<User {self.username}>'
=======
from database import *
>>>>>>> d15fc0049d49b9858e8026f46f5f30eb39e4a156
