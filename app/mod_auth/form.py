from flask import flash
from flask_wtf import FlaskForm
from flask_wtf import RecaptchaField
from wtforms import TextField, PasswordField, TextAreaField, StringField, IntegerField, SelectField, HiddenField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Optional

from app import app, dba
from app.models import User

class RegisterForm(FlaskForm):
    name = StringField('Name', [DataRequired(), Length(min=4)])
    username = StringField('Username', [DataRequired(), Length(max=255)])
    password = PasswordField('Password', [DataRequired()])
    email = StringField('Email', [DataRequired()])
    location = StringField('Location', [DataRequired()])
    address = StringField('Address', [DataRequired()])
    postnumber = StringField('Postnumber', [DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField('Signup')

class ProfileForm(FlaskForm):
    user_id = HiddenField('User ID')
    username = HiddenField('Username')
    date = HiddenField('Registered')
    last_login = HiddenField('Last login')
    name = StringField('Name', [DataRequired(), Length(min=4)])
    email = StringField('Email', [DataRequired()])
    location = StringField('Location', [DataRequired()])
    address = StringField('Address', [DataRequired()])
    postnumber = StringField('Postnumber', [DataRequired()])
    bornyear = IntegerField('Born (year)')
    email2 = StringField('Email 2')
    homepage = StringField('Homepage')
    info = StringField('Info')
    hobbies = StringField('Hobbies')
    extrainfo = StringField('Extra info')
    sukupuoli = SelectField('Sex', choices=[('1', 'Male'), ('2', 'Female')])
    icq = StringField('ICQ')
    apulainen = IntegerField('Helper')
    chat = IntegerField('Chat', [Optional(strip_whitespace=True)])
    oikeus = IntegerField('Rights')
    lang_id = SelectField('Language ID', choices=[('1', 'English'), ('2', 'Finnish'), ('3', 'Swedish')])
    login_count = HiddenField('Login count', [Optional(strip_whitespace=True)])
    emails = IntegerField('Emails')
    puhelin = StringField('Telephone')
    blogs = IntegerField('Blogs', [Optional(strip_whitespace=True)])
    messenger = StringField('Messenger')
    myspace = StringField('Myspace')
    rss = StringField('RSS')
    youtube = StringField('Youtube')
    ircgalleria = StringField('IRC galleria')
    last_profile_update = HiddenField('Last profile update')
    avatar = StringField('Avatar')
    flickr_username = StringField('Flickr username')
    submit = SubmitField('Save')

    def update_details(self, user):
        try:
            username = user['username']
            result = dba.session.query(User).filter(User.username == username).update(user, synchronize_session=False)
            dba.session.commit()
            flash("User details updated")
        except Exception as e:
            print("UPDATE failed")
            print(e)
