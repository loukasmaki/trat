from  flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User
from flask import request

class RegisterSession(FlaskForm):
    attendee = StringField('Namn')
    date = DateField('Datum', format='%Y%m%d')
    instructor = StringField('Instruktör')
    weapon_class = StringField('')


