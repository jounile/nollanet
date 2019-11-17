from datetime import datetime
from sqlalchemy import inspect
from sqlalchemy.types import Integer, String, DateTime

from . import dba

class Media(dba.Model):
    __tablename__ = 'media_table'
    media_id = dba.Column(dba.Integer, primary_key = True)
    media_topic = dba.Column(dba.String(50))
    media_desc = dba.Column(dba.String(50))
    media_text = dba.Column(dba.String(50))
    media_type = dba.Column(dba.String(50))
    media_genre = dba.Column(dba.String(50))
    story_type = dba.Column(dba.String(50))
    create_time = dba.Column(dba.String(50))
    owner = dba.Column(dba.String(50))
    lang_id = dba.Column(dba.Integer)

class Page(dba.Model):
    __tablename__ = 'general'
    id = dba.Column(dba.Integer, primary_key = True)
    page_id = dba.Column(dba.Integer)
    header = dba.Column(dba.String(50))
    text = dba.Column(dba.String(50))
    info = dba.Column(dba.String(50))
    lang_id = dba.Column(dba.Integer)

class User(dba.Model):
    __tablename__ = 'users'
    user_id = dba.Column(dba.Integer, primary_key = True)
    username = dba.Column(dba.String(50))
    password = dba.Column(dba.String(50))
    level = dba.Column(dba.String(50))
    name = dba.Column(dba.String(50))
    email = dba.Column(dba.String(50))
    location = dba.Column(dba.String(50))
    address = dba.Column(dba.String(50))
    postnumber = dba.Column(dba.String(50))
    bornyear = dba.Column(dba.String(50))
    email2 = dba.Column(dba.String(50))
    homepage = dba.Column(dba.String(50))
    info = dba.Column(dba.String(50))
    date = dba.Column(dba.String(50))
    hobbies = dba.Column(dba.String(50))
    extrainfo = dba.Column(dba.String(50))
    sukupuoli = dba.Column(dba.String(50))
    icq = dba.Column(dba.String(50))
    apulainen = dba.Column(dba.String(50))
    last_login = dba.Column(dba.DateTime, default=datetime.now, onupdate=datetime.now)
    chat = dba.Column(dba.String(50))
    oikeus = dba.Column(dba.String(50))
    lang_id = dba.Column(dba.String(50))
    login_count = dba.Column(dba.String(50))
    lastloginip = dba.Column(dba.String(50))
    lastloginclient = dba.Column(dba.String(50))
    emails = dba.Column(dba.String(50))
    puhelin = dba.Column(dba.String(50))
    kantaasiakasnro = dba.Column(dba.String(50))
    lamina_lisatieto = dba.Column(dba.String(50))
    blogs = dba.Column(dba.String(50))
    user_showid = dba.Column(dba.String(50))
    messenger = dba.Column(dba.String(50))
    myspace = dba.Column(dba.String(50))
    rss = dba.Column(dba.String(50))
    youtube = dba.Column(dba.String(50))
    ircgalleria = dba.Column(dba.String(50))
    last_profile_update = dba.Column(dba.String(50))
    avatar = dba.Column(dba.String(50))
    flickr_username = dba.Column(dba.String(50))

class Comment(dba.Model):
    __tablename__ = 'kommentti'
    id = dba.Column(dba.Integer, primary_key = True)
    user_id = dba.Column(dba.Integer)
    header = dba.Column(dba.String(50))
    comment = dba.Column(dba.String(50))
    timestamp = dba.Column(dba.String(50))
    media_id = dba.Column(dba.String(50))
    comment_user_id = dba.Column(dba.String(50))
    youtube_id = dba.Column(dba.String(50))
    tapahtuma_id = dba.Column(dba.String(50))
    diary_id = dba.Column(dba.String(50))

class Storytype(dba.Model):
    __tablename__ = 'storytype'
    id = dba.Column(dba.Integer, primary_key= True)
    type_id = dba.Column(dba.Integer, dba.ForeignKey('media_table.story_type'))
    type_name = dba.Column(String(50))

class Genre(dba.Model):
    __tablename__ = 'genre'
    id = dba.Column(dba.Integer, primary_key= True)
    type_id = dba.Column(dba.Integer, dba.ForeignKey('media_table.media_genre'))
    type_name = dba.Column(String(50))

class Mediatype(dba.Model):
    __tablename__ = 'mediatype'
    id = dba.Column(dba.Integer, primary_key= True)
    type_id = dba.Column(dba.Integer, dba.ForeignKey('media_table.media_type'))
    type_name = dba.Column(String(50))