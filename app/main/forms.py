from  flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField, HiddenField, BooleanField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User
from flask import request
from config import Config

class RegisterSessionForm(FlaskForm):
    attendee = StringField('Förnamn och efternamn', validators=[DataRequired()])
    date = DateField('Datum', format='%Y%m%d', validators=[DataRequired()])
    instructor = StringField('Instruktör', validators=[DataRequired()])
    weapon_class = SelectField('Kurs',choices=Config.weapon_class_list, 
                              validators=[DataRequired()])
    submit = SubmitField('Registrera')

class AdminAttendeeForm(FlaskForm):

    instructor = BooleanField('Instruktör')
    attendee_id = HiddenField(default=1)
    submit = SubmitField()

class ScheduleForm(FlaskForm):
    # Sätt en vecka och sprid ut den över hela året
    # Terminsstart och Terminsslut för respektive termin
    # Datum
    # Hall A eller B Dold tills vi kan utnyttja
    # Om vardag tidslott 1 eller 2. Om helg mer valmöjligheter
    # Klumpigt men duger tills jag kommer på något bättre. 
    # Vad händer om man ändrar mitt i terminen?
    # 
    weapon_class = SelectField(choices=Config.weapon_class_list,
    validators=[DataRequired()])
    submit = SubmitField('Spara Schema')

