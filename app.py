import os
from flask import Flask
from models import db  
from models.user import User  


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/database.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  


if not os.path.exists('instance'):
    os.makedirs('instance')


db.init_app(app)


with app.app_context():
    print("Creating tables...")
    db.create_all()  
    print("Tables created!")


@app.route('/')
def home():
    return "Flask app is running!"


if __name__ == '__main__':
    app.run(debug=True)

