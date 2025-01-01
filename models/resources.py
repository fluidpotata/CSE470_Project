from database import *

class Resource(db.Model):
    __tablename__ = 'resources'
    resID = db.Column(db.Integer, primary_key=True)
    campID = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __init__(self, campID, type, quantity):
        self.campID = campID
        self.type = type
        self.quantity = quantity

    @staticmethod
    def addResource(campID, type, quantity):
        new_resource = Resource(campID=campID, type=type, quantity=quantity)
        db.session.add(new_resource)
        try:
            db.session.commit()
            print("Resource added successfully")
        except Exception as e:
            db.session.rollback()
            print("Failed to add resource")
            print(e)

    @staticmethod
    def updateQuantity(resID, campID, quantity):
        resource = Resource.query.filter_by(resID=resID, campID=campID).first()
        if resource:
            resource.quantity = quantity
            try:
                db.session.commit()
                print(f"Resource {resID} at camp {campID} updated successfully")
            except Exception as e:
                db.session.rollback()
                print(f"Failed to update resource {resID} at camp {campID}")
                print(e)
        else:
            print(f"Resource {resID} at camp {campID} not found")
