from database import * 
class Incident:
    def __init__(self, id, type, location, status):
        self.id = id
        self.type = type
        self.location = location
        self.status = status

    @staticmethod
    def getInfo(id):
        
        query = f'''
        select * from incident where id = '{id}';
        '''
        res = get_result_from_query(query)
        
        if res:
            return Incident(res[0][0], res[0][1], res[0][2], res[0][3]) 
        else:
            return None

    @staticmethod
    def updateInfo(id, new_status):
        
        query = f'''
        update incident set status = '{new_status}' where id = '{id}';
        '''
        update_result = execute_query(query)  
        
        if update_result:
            return f"Incident {id} updated to status: {new_status}"
        else:
            return f"Failed to update incident {id}"

    def getIncidentDetails(self):
        
        return {
            'id': self.id,
            'type': self.type,
            'location': self.location,
            'status': self.status
        }
