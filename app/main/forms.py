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
    set_instructor = BooleanField('Instruktör')

    pass



class Schedule(FlaskForm):
    # Sätt en vecka och sprid ut den över hela året
    # Terminsstart och Terminsslut för respektive termin
    # Datum
    # Hall A eller B Dold tills vi kan utnyttja
    # Om vardag tidslott 1 eller 2. Om helg mer valmöjligheter
    # Klumpigt men duger tills jag kommer på något bättre. 
    # Vad händer om man ändrar mitt i terminen?
    # 
    weapon_class = RadioField(choices=[
        'Brottning', 
        'Långsvärd Grundkurs', 
        'Långsvärd Fortsättning', 
        'Sabel', 
        'Rapir & Dolk', 
        'Svärd & Bucklare', 
        'Barn & Ungdom'
    ], validators=[DataRequired()])
    submit = SubmitField('Spara Schema')


