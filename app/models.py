from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app import db, login

Base = declarative_base()

db = SQLAlchemy()

attendees_trainingday = db.Table('attendees_trainingday',
    #db.Column('attendee_id', db.Integer, db.ForeignKey('attendee.id'), primary_key=True),
    #db.Column('training_day_id', db.Integer, db.ForeignKey('training_day.id'), primary_key=True)
    db.Column('attendee_id', db.Integer, db.ForeignKey('attendee.id'), primary_key=False),
    db.Column('training_day_id', db.Integer, db.ForeignKey('training_day.id'), primary_key=False)
    )

class Attendee(db.Model):
    __tablename__ = "attendee"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    training_dates = db.relationship('Training_day', secondary=attendees_trainingday, back_populates='attendees', lazy='subquery')

class Training_day(db.Model):
    __tablename__ = "training_day"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    weapon = db.Column(db.String(30), nullable=False)
    instructor = db.Column(db.String(50), server_default='ingen' )
    attendees = db.relationship('Attendee',  secondary=attendees_trainingday, back_populates='training_dates', lazy='subquery')

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    role = db.Column(db.String(20), server_default='member')

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
