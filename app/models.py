from datetime import datetime, timedelta
from datetime import datetime
from time import time
from flask_login import UserMixin
import json
import os
import jwt
from werkzeug.security import  generate_password_hash, check_password_hash
from hashlib import md5
from app import db, login


attendees_trainingsession= db.Table('attendees_trainingsession',
    db.Column('attendee_id', db.Integer, db.ForeignKey('attendee.id'), primary_key=False),
    db.Column('training_session_id', db.Integer, db.ForeignKey('training_sessions.id'), primary_key=False)
    )

class Attendee(db.Model):
    __tablename__ = "attendee"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
#    training_dates = db.relationship('TrainingSession', secondary=attendees_trainingsession, back_populates='attendees', lazy='subquery')

class TrainingSession(db.Model):
    __tablename__ = "training_sessions"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    weapon = db.Column(db.String(30), nullable=False)
    instructor = db.Column(db.String(50), server_default='ingen' )
#    attendees = db.relationship('Attendee',  secondary=attendees_trainingsession, back_populates='training_dates', lazy='subquery')

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    role = db.Column(db.String(20), server_default='member')
    email =  db.Column(db.String(60), nullable=False)
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)


    def __repr__(self):
        return f'<User {self.username}'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_reset_password(token):
        try:
            id = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])['reset_password']

        except:
            return
        return User.query.get(id)




@login.user_loader
def load_user(id):
    return User.query.get(int(id))
