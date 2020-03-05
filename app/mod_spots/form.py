from flask import flash
from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, TextAreaField, StringField, IntegerField, DateField, SelectField, HiddenField, SubmitField

class NewSpotForm(FlaskForm):
    country = SelectField('country', choices=[])
    town = SelectField('town', choices=[])
    tyyppi = SelectField('tyyppi', choices=[])
    name = StringField('Name')
    description = StringField('Description')
    temp = StringField('Temp')
    link = StringField('Link')
    latlon = StringField('latlon')

class UpdateSpotForm(FlaskForm):
    country = SelectField('country', choices=[])
    town = SelectField('town', choices=[])
    tyyppi = SelectField('tyyppi', choices=[])
    name = StringField('Name')
    description = TextAreaField('Description')
    temp = StringField('Temp')
    link = StringField('Link')
    latlon = StringField('latlon')
