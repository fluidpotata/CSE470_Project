from database import *
class Rcamp():
    def __init__(self, id, name, location, v_capacity, v_occupied):
        self.id = id
        self.name = name
        self.location = location
        self.v_capacity = v_capacity
        self.v_occupied = v_occupied
    @staticmethod
    def addcamp( id, name, location, v_capacity, v_occupied):
        return Rcamp(id, name, location, v_capacity, v_occupied)


    def get_camp_status(self, v_id):
        query1 = '''select assignedIN from workAssigned where volnID = ?;'''
        arr = get_result_from_query(query1, v_id)
        query2 = '''select * from Reliefcamp where rcampID = ?;'''
        result = get_result_from_query(query2, arr[0][0])
        return Rcamp(result[0][0], result[0][1], result[0][2], result[0][3], result[0][4])


    def track_resources(self):
        pass


    def update_camp(self, v_cap, v_occ):
        self.v_capacity = v_cap
        self.v_occupied = v_occ
