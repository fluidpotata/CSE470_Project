from database import *


class Rcamp(db.Model):
    __tablename__ = 'Reliefcamp'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    v_capacity = db.Column(db.Integer, nullable=False)
    v_occupied = db.Column(db.Integer, nullable=False)

    def __init__(self, id, name, location, v_capacity, v_occupied):
        self.id = id
        self.name = name
        self.location = location
        self.v_capacity = v_capacity
        self.v_occupied = v_occupied

    @staticmethod
    def addcamp(id, name, location, v_capacity, v_occupied):
        new_camp = Rcamp(id, name, location, v_capacity, v_occupied)
        db.session.add(new_camp)
        db.session.commit()
        return new_camp

    @staticmethod
    def get_camp_status(v_id):
        query1 = '''select assignedIN from workAssigned where volnID = :v_id;'''
        arr = db.session.execute(query1, {'v_id': v_id}).fetchall()
        if not arr:
            return None
        query2 = '''select * from Reliefcamp where rcampID = :rcamp_id;'''
        result = db.session.execute(query2, {'rcamp_id': arr[0][0]}).fetchall()
        if not result:
            return None
        return Rcamp(result[0][0], result[0][1], result[0][2], result[0][3], result[0][4])

    def track_resources(self):
        pass

    def update_camp(self, v_cap, v_occ):
        self.v_capacity = v_cap
        self.v_occupied = v_occ
        db.session.commit()
