from flask import flash
from flask_wtf import FlaskForm
from flask_wtf.recaptcha import RecaptchaField
from wtforms import TextField, PasswordField, TextAreaField, StringField, IntegerField, DateField, SelectField, HiddenField, SubmitField
from wtforms.validators import DataRequired, InputRequired, Length, Email, Optional, NumberRange

from app import app, db
from app.models import User


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired("Name is required"), Length(min=4)])
    username = StringField('Username', validators=[InputRequired("Username is required"), Length(min=4)])
    password = PasswordField('Password', validators=[InputRequired("Password is required")])
    email = StringField('Email', validators=[InputRequired("Email is required"), Email("Invalid E-mail Address")])
    bornyear = IntegerField('Born (year)', [InputRequired("Year is required")])
    gender = SelectField('Gender', choices=[('1', 'Male'), ('2', 'Female')])
    address = StringField('Address')
    postnumber = IntegerField('Postnumber', validators=[InputRequired("Postnumber is required")])
    location = StringField('City')
    recaptcha = RecaptchaField()
    submit = SubmitField('Signup')

class ProfileForm(FlaskForm):
    id = HiddenField('User ID')
    level = HiddenField('Level')
    username = HiddenField('Username')
    name = StringField('Name', [DataRequired(), Length(min=4)])
    bornyear = IntegerField('Born (year)', [DataRequired()])
    email = StringField('Email', [DataRequired()])
    homepage = StringField('Homepage')
    info = StringField('Info')
    location = StringField('Location', [DataRequired()])
    date = HiddenField('Registered')
    hobbies = StringField('Hobbies')
    gender = SelectField('Gender', choices=[('1', 'Male'), ('2', 'Female')])
    last_login = HiddenField('Last login')
    lang_id = SelectField('Language ID', choices=[('1', 'English'), ('2', 'Finnish'), ('3', 'Swedish')])
    login_count = HiddenField('Login count', [Optional(strip_whitespace=True)])
    address = StringField('Address')
    postnumber = StringField('Postnumber')
    telephone = StringField('Telephone')
    youtube = StringField('Youtube')
    last_update = HiddenField('Last update')
    avatar = StringField('Avatar')
    submit = SubmitField('Save')

    def update_details(self, user):
        try:
            #print("user", user)
            username = user['username']
            result = db.session.query(User).filter(User.username == username).update(user, synchronize_session=False)
            db.session.commit()
            flash("User details updated")
        except Exception as e:
            print("UPDATE failed")
            print(e)
