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
        query2 = f'''select * from users where username='{username}';'''
        print(password)
        f = get_result_from_query(query)[0][0]
        print(f)
        try:
            if password==f:
                res = get_result_from_query(query2)
                user = User(res[0][0], res[0][2], res[0][3], res[0][4], res[0][5], res[0][6], res[0][7], res[0][8], res[0][9])
                return (True, user)
        except:
            print("error")
        return (False, None)

    @staticmethod
    def registerUser(username, email, name, nid, date_of_birth, address, password, contact, blood_type):
        query2 = f'''select count(*) from users where username='{username}';'''
        if int(get_result_from_query(query2)[0][0])>0:
            return (False, "Username already registered!")
        query1 = '''select count(*) from users;'''
        c = int(get_result_from_query(query1)[0][0]) + 100000
        query = f"""INSERT INTO users (username, userid, name, nid, dateofbirth, email, address, password, contact, bloodtype) VALUES ('{username}', '{c}', '{email}', '{name}', '{nid}', '{date_of_birth}', '{address}', '{password}', '{contact}', '{blood_type}');"""
        execute_query(query)
        return (True, "User registered!")