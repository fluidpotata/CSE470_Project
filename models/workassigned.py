from database import *

class WorkAssigned(db.Model):
    __tablename__ = 'workAssigned'
    
    rcamp_id = db.Column(db.Integer, db.ForeignKey('Reliefcamp.id'))
    volnID = db.Column(db.Integer, db.ForeignKey('volunteers.volunteerid'), primary_key=True)
    
    def __init__(self, rcamp_id, volnID):
        self.id = rcamp_id
        self.volnID = volnID

    def count_volunteers(self, rcamp_id):
        WorkAssigned.query.filter_by(self.id == rcamp_id).count()