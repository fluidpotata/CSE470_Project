from database import db

class EmergencyDirectory(db.Model):
    __tablename__ = 'emergency_directory'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    designation = db.Column(db.String, nullable=False)
    contact = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)

    def __init__(self, name, designation, contact, location):
        self.name = name
        self.designation = designation
        self.contact = contact
        self.location = location

    @staticmethod
    def get_all_contacts(param=None):
        if param:
            return EmergencyDirectory.query.filter((EmergencyDirectory.location.like(f'%{param}%')) |
                                                   (EmergencyDirectory.name.like(f'%{param}%')) |
                                                   (EmergencyDirectory.designation.like(f'%{param}%'))
                                                   .all())
        return EmergencyDirectory.query.all()
