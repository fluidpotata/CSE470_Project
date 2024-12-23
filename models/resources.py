from database import *  

class Resources:
    def __init__(self, resID=None, campID=None, type=None, quantity=None):
        self.resID = resID
        self.campID = campID
        self.type = type
        self.quantity = quantity

    @staticmethod
    def addResource(campID, type, quantity):
        
        query = f'''
        insert into resources (campID, type, quantity)
        values ('{campID}', '{type}', {quantity});
        '''
        result = execute_query(query)
        
        if result:
            print("Resource added successfully")
        else:
            print("Failed to add resource")

    @staticmethod
    def updateQuantity(resID, campID, quantity):
        
        query = f'''
        Update resources
        set quantity = {quantity}
        where resID = '{resID}' and campID = '{campID}';
        '''
        result = execute_query(query)
        
        if result:
            print(f"Resource {resID} at camp {campID} updated successfully")
        else:
            print(f"Failed to update resource {resID} at camp {campID}")

