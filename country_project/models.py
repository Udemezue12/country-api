from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import generate_password_hash, check_password_hash
from country_project.database import db
from country_project.login import login_manager
from country_project.secure import encrypt_data, decrypt_data
from flask_login import UserMixin
from geopy.geocoders import Nominatim
import uuid


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    api_key = db.Column(db.String(50), unique=True, nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.username}>'

    def __init__(self,  role, email, username, password):

        self.email = email
        # self.phone_number = phone_number
        self.username = username
        self.password = generate_password_hash(
            password).decode('utf-8') if password else None
        self.role = role
    def generate_api_key(self):
        self.api_key = str(uuid.uuid4())
        db.session.commit()

class APIUser(db.Model):
    __tablename__ = 'passenger'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user.id'), unique=True, nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)

    date_of_birth = db.Column(db.Date(), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    user = db.relationship(
        'User', backref=db.backref('passenger', uselist=False))

    def __repr__(self):
        return f'<Passenger {self.first_name} {self.last_name}>'