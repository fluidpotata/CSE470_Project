from database import *
from models.user import User

class Volunteer(db.Model):
    __tablename__ = 'volunteers'
    
    volunteerid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role = db.Column(db.String)
    availability = db.Column(db.String)
    userId = db.Column(db.Integer, db.ForeignKey('users.id')) 
    
    def __init__(self, volunteerid, role, availability, userId):
        self.volunteerid = volunteerid
        self.role = role
        self.availability = availability
        self.userId = userId

    def assignTask(self, task):
        pass

    @staticmethod
    def registerVolunteer(volunteerid, role, availability):
        volunteer = Volunteer(volunteerid, role, availability)
        db.session.add(volunteer)
        db.session.commit()
        return volunteer

    @staticmethod
    def getVolunteer(userId):
        return Volunteer.query.filter_by(userId=userId).first()

    def trackActivity(self):
        pass

    def getAvailability(self):
        return self.availability

    def setAvailability(self, new_availability):
        self.availability = new_availability
        db.session.commit()
    
    def getInfo(self):
        query = db.session.query(WorkAssigned, User.name).join(Volunteer, WorkAssigned.volnID == Volunteer.volunteerid).join(User, Volunteer.userID == User.id).filter(WorkAssigned.volnID == self.volunteerid)
        res = query.all()
        return res

class WorkAssigned(db.Model):
    __tablename__ = 'workAssigned'
    
    id = db.Column(db.Integer, primary_key=True)
    volnID = db.Column(db.String, db.ForeignKey('volunteers.volunteerid'))
    # other fields...
