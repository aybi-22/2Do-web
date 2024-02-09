from flask_sqlalchemy import SQLAlchemy
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    assword_hash = db.Column(db.String(128))
    birthdate = db.Column(db.Date, nullable=False)

def set_password(self, password):
        self.password_hash = generate_password_hash(password)

def check_password(self, password):
        return check_password_hash(self.password_hash, password)