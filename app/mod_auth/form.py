from flask import flash
from flask_wtf import FlaskForm
from flask_wtf import RecaptchaField
from wtforms import TextField, PasswordField, TextAreaField, StringField, IntegerField, SelectField, HiddenField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Optional

from app import db

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
            cursor = db.connection.cursor()
            sql = "UPDATE users SET name=%s, email=%s, location=%s, address=%s, postnumber=%s, bornyear=%s, email2=%s, homepage=%s, info=%s, hobbies=%s, extrainfo=%s, sukupuoli=%s, icq=%s, apulainen=%s, chat=%s, oikeus=%s, lang_id=%s, login_count=%s, emails=%s, puhelin=%s, blogs=%s, messenger=%s, myspace=%s, rss=%s, youtube=%s, ircgalleria=%s, last_profile_update=%s, avatar=%s, flickr_username=%s WHERE username=%s LIMIT 1"
            cursor.execute(sql, (user['name'], user['email'], user['location'], user['address'], user['postnumber'], user['bornyear'], user['email2'], user['homepage'], user['info'], user['hobbies'], user['extrainfo'], user['sukupuoli'], user['icq'], user['apulainen'], user['chat'], user['oikeus'], user['lang_id'], user['login_count'], user['emails'], user['puhelin'], user['blogs'], user['messenger'], user['myspace'], user['rss'], user['youtube'], user['ircgalleria'], user['last_profile_update'], user['avatar'], user['flickr_username'], user['username'], ))
            db.connection.commit()
            flash("User details updated")
        except Exception as e:
            print("UPDATE failed")
            print(e)
