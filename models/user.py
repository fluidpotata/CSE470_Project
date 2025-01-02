from database import *
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    nid = db.Column(db.String(20), nullable=False)
    date_of_birth = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    address = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(20), nullable=False)
    blood_type = db.Column(db.String(3), nullable=False)
    role = db.Column(db.String(20), default='user', nullable=False)
    blood_donation = db.Column(db.String(6))

    def __repr__(self):
        return f'<User {self.username}>'

    @staticmethod
    def authenticate(username, password):
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            return (True, user)
        return (False, None)

    @staticmethod
    def registerUser(username, email, name, nid, date_of_birth, address, password, contact, blood_type):
        if User.query.filter_by(username=username).first():
            return (False, "Username already registered!")

        try:
            if isinstance(date_of_birth, str):
                datetime.strptime(date_of_birth, '%Y-%m-%d')
            else:
                date_of_birth = date_of_birth.strftime('%Y-%m-%d')
        except ValueError:
            return (False, "Invalid date format. Use YYYY-MM-DD")
            
        user = User(
            username=username,
            email=email,
            name=name,
            nid=nid,
            date_of_birth=date_of_birth,
            address=address,
            password=password,
            contact=contact,
            blood_type=blood_type
        )
        db.session.add(user)
        db.session.commit()
        return (True, "User registered!")

    def getInfo(self):
        return {
            'username': self.username,
            'name': self.name,
            'nid': self.nid,
            'date_of_birth': self.date_of_birth,
            'email': self.email,
            'address': self.address,
            'contact': self.contact,
            'blood_type': self.blood_type,
            'blood_donation': self.blood_donation
        }
    
    @staticmethod
    def getUser(id):
        return User.query.filter_by(id=id).first()
    
    @staticmethod
    def donate_blood(id):
        user = User.getUser(id)
        if user.blood_donation == "False":
            user.blood_donation = "True"
        else:
            user.blood_donation = "False"
        db.session.commit()
        return user
    

    @staticmethod
    def getAlluser():
        return User.query.order_by(User.address, User.blood_type).all()
    

    @staticmethod
    def filter_bloodbank(blood_type, address):
        return User.query.filter_by(blood_type=blood_type, address=address).all()   
