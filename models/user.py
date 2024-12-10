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
        # object creation and session creation is yet to be done

    @staticmethod
    def registerUser(username, email, name, nid, date_of_birth, address, password, contact, blood_type):
        query2 = f'''select count(*) from users where username={username};'''
        if int(get_result_from_query(query2)[0][0])>0:
            return {False, "Username already registered!"}
        query1 = '''select count(*) from users;'''
        c = int(get_result_from_query(query1)[0][0]) + 100000
        query = f"""INSERT INTO users (username, userid, name, nid, dateofbirth, email, address, password, contact, bloodtype) VALUES ({username}, {c}, {email}, {name}, {nid}, {date_of_birth}, {address}, {password}, {contact}, {blood_type});"""
        execute_query(query)
        return {True, "User registered!"}