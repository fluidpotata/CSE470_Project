from database import *

class WorkAssigned(db.Model):
    __tablename__ = 'workAssigned'
    
    rcamp_id = db.Column(db.Integer, db.ForeignKey('Reliefcamp.id'))
    volnID = db.Column(db.Integer, db.ForeignKey('volunteers.volunteerid'), primary_key=True)
    
    def __init__(self, rcamp_id, volnID):
        self.rcamp_id = rcamp_id
        self.volnID = volnID

    @staticmethod
    def count_volunteers(rcamp_id):
        count = WorkAssigned.query.filter_by(rcamp_id = rcamp_id).count()
        return count