from  flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, RadioField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User
from flask import request

class RegisterSession(FlaskForm):
    attendee = StringField('Förnamn och efternamn', validators=[DataRequired()])
    date = DateField('Datum', format='%Y%m%d', validators=[DataRequired()])
    instructor = StringField('Instruktör', validators=[DataRequired()])
    weapon_class = RadioField(choices=[
        'Brottning', 
        'Långsvärd Grundkurs', 
        'Långsvärd Fortsättning', 
        'Sabel', 
        'Rapir & Dolk', 
        'Svärd & Bucklare', 
        'Barn & Ungdom'
    ], validators=[DataRequired()])
    submit = SubmitField('Registrera')

class AdminAttendee(FlaskForm):
    
    pass



class Schedule(FlaskForm):
    weapon_class = RadioField(choices=[
        'Brottning', 
        'Långsvärd Grundkurs', 
        'Långsvärd Fortsättning', 
        'Sabel', 
        'Rapir & Dolk', 
        'Svärd & Bucklare', 
        'Barn & Ungdom'
    ], validators=[DataRequired()])


