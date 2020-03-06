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
    temp = IntegerField('Temp')
    link = StringField('Link')
    latlon = StringField('latlon')

class NewCountryForm(FlaskForm):
    id = IntegerField('Id')
    maa = StringField('Name')
    lat = StringField('Latitude')
    lon = StringField('Longitude')
    koodi = StringField('Country code')

class NewTownForm(FlaskForm):
    id = IntegerField('Id')
    paikkakunta = StringField('Town')
    maa_id = SelectField('Country code', choices=[])
    lat = StringField('Latitude')
    lon = StringField('Longitude')

class NewTypeForm(FlaskForm):
    id = IntegerField('Id')
    name = StringField('Name')
