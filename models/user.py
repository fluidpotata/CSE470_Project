from database import *


class User():
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


    @staticmethod
    def authenticate(username, password):
        query = f"SELECT password FROM users WHERE username='{username}';"

        if password==get_result_from_query(query)[0][0]:
            return True
        return False

    @staticmethod
    def registerUser():
        pass #will be done by maishatasnim25