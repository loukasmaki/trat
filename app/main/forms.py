from  flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User
from flask import request

class RegisterSession(FlaskForm):
    attendee = StringField('Förnamn och efternamn', validators=[DataRequired()])
    date = DateField('Datum', format='%Y%m%d', validators=[DataRequired()])
    instructor = StringField('Instruktör', validators=[DataRequired()])
    weapon_class = StringField('Kurs', validators=[DataRequired()])
    submit = SubmitField('Registrera')

