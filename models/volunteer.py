from database import *

class Volunteer():
    def __init__(self, volunteerid,role,availability):
        self.volunteerid = volunteerid
        self.availability = availability
        self.role = role

    def assignTask(self, task):
        pass

    @staticmethod
    def registerVolunteer(volunteerid, skills, availability, type):
        return Volunteer(volunteerid, skills, availability, type)

    @staticmethod
    def getVolunteer(volunteerid):
        query = f'''select * from volunteers where volnID='{volunteerid}';'''
        res = get_result_from_query(query)
        return Volunteer(res[0][0], res[0][1], res[0][2])

    def trackActivity(self):
        pass

    def getAvailability(self):
        return self.availability

    def setAvailability(self, new_availability):
        self.availability = new_availability
    
    def getInfo(self):
        query = f'''
        SELECT w.*, u.name 
        FROM workAssigned w
        JOIN volunteers v ON w.volnID = v.volnID
        JOIN users u ON v.userID = u.userID
        WHERE w.volnID = '{self.volunteerid}';
        '''
        # data still not available, need to implement others first!
        res = get_result_from_query(query)
        return res