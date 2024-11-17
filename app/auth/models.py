from app import db
from flask_login import UserMixin
from sqlalchemy import Enum


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    role = db.Column(Enum('admin', 'manager', 'normal', name='user_roles'), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
