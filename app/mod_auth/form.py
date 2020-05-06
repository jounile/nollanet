from flask import flash
from flask_wtf import FlaskForm
from flask_wtf import RecaptchaField
from wtforms import TextField, PasswordField, TextAreaField, StringField, IntegerField, DateField, SelectField, HiddenField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Optional

from app import app, db
from app.models import User

class RegisterForm(FlaskForm):
    name = StringField('Name', [DataRequired(), Length(min=4)])
    username = StringField('Username', [DataRequired(), Length(max=255)])
    password = PasswordField('Password', [DataRequired()])
    email = StringField('Email', [DataRequired()])
    bornyear = IntegerField('Born (year)', [DataRequired()])
    gender = SelectField('Gender', choices=[('1', 'Male'), ('2', 'Female')])
    address = StringField('Address')
    postnumber = StringField('Postnumber')
    location = StringField('City', [DataRequired()])
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
