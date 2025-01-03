from database import *


class ApplyVolunteer(db.Model):
    __tablename__ = 'apply_volunteer'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))


    def __init__(self, email):
        self.email = email

    
    def get_all_applicant(self):
        result = ApplyVolunteer.query.all()
        return result
    def delete_applicant(self, email):
        ApplyVolunteer.query.filter_by(email=email).delete()
        db.session.commit()

    def accept_application(self, email):
        pass
