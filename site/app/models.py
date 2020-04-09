# coding: utf-8
from sqlalchemy import BigInteger, Column, Date, DateTime, Index, Integer, SmallInteger, String, Table, Text
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy

from app import app, db

class Country(db.Model):
    __tablename__ = 'countries'
    id = db.Column(db.Integer, db.ForeignKey('media.country_id'), primary_key= True)
    country_code = db.Column(db.String(50))
    country_name = db.Column(db.String(50))

class Page(db.Model):
    __tablename__ = 'page'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    page_id = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue())
    header = db.Column(db.Text)
    text = db.Column(db.Text)
    info = db.Column(db.Text)
    lang_id = db.Column(db.SmallInteger)

class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    type_id = db.Column(db.Integer, db.ForeignKey('media.media_id'))
    type_name = db.Column(db.String(50))

class MapCountry(db.Model):
    __tablename__ = 'map_country'
    id = db.Column(db.Integer, primary_key=True)
    maa = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue())
    lat = db.Column(db.String(50))
    lon = db.Column(db.String(50))
    koodi = db.Column(db.String(2))

class MapTown(db.Model):
    __tablename__ = 'map_town'
    id = db.Column(db.Integer, primary_key=True)
    paikkakunta = db.Column(db.String(40), nullable=False, unique=True, server_default=db.FetchedValue())
    maa_id = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue())
    lat = db.Column(db.String(50))
    lon = db.Column(db.String(50))

class MapSpot(db.Model):
    __tablename__ = 'map_spot'
    kartta_id = db.Column(db.Integer, primary_key=True, unique=True)
    paikkakunta_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    user_id = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue())
    nimi = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue())
    info = db.Column(db.String(512), nullable=False)
    tyyppi = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    temp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    paivays = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    karttalinkki = db.Column(db.String(200))
    maa_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    latlon = db.Column(db.String(512))

class MapType(db.Model):
    __tablename__ = 'map_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue())

class Comment(db.Model):
    __tablename__ = 'comment'
    __table_args__ = (
        db.Index('user_id', 'media_id', 'comment_user_id', 'youtube_id'),
    )
    id = db.Column(db.BigInteger, primary_key=True, unique=True)
    user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    header = db.Column(db.String(250))
    comment = db.Column(db.String(2048))
    media_id = db.Column(db.BigInteger)
    comment_user_id = db.Column(db.BigInteger)
    youtube_id = db.Column(db.BigInteger)
    timestamp = db.Column(db.DateTime, nullable=False, index=True, server_default=db.FetchedValue())
    tapahtuma_id = db.Column(db.BigInteger, index=True)
    diary_id = db.Column(db.Integer, index=True)
    kilpailu_id = db.Column(db.Integer, index=True)
    videoblog_id = db.Column(db.Integer)

class LinkCategories(db.Model):
    __tablename__ = 'link_categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer)
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue())

class Links(db.Model):
    __tablename__ = 'links'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    category = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer)
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue())

class Media(db.Model):
    __tablename__ = 'media'
    media_id = db.Column(db.Integer, primary_key = True)
    media_topic = db.Column(db.String(50))
    media_desc = db.Column(db.String(50))
    media_text = db.Column(db.String(50))
    media_type = db.Column(db.String(50))
    media_genre = db.Column(db.String(50))
    story_type = db.Column(db.String(50))
    create_time = db.Column(db.String(50))
    owner = db.Column(db.String(50))
    lang_id = db.Column(db.Integer)
    country_id = db.Column(db.Integer, index=True)
    hidden = db.Column(db.Integer)

class MediaType(db.Model):
    __tablename__ = 'media_type'
    id = db.Column(db.Integer, primary_key=True)
    type_id = db.Column(db.Integer, db.ForeignKey('media.media_id'))
    type_name = db.Column(db.String(50))

class PwdRecover(db.Model):
    __tablename__ = 'pwdrecover'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    token = db.Column(db.String(255), nullable=False)
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue())

class StoryType(db.Model):
    __tablename__ = 'story_type'
    id = db.Column(db.Integer, primary_key=True)
    type_id = db.Column(db.Integer, db.ForeignKey('media.media_id'))
    type_name = db.Column(db.String(50))

class Uploads(db.Model):
    __tablename__ = 'uploads'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(255), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    path = db.Column(db.String(255), nullable=False)

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue())
    username = db.Column(db.String(20), nullable=False, index=True, server_default=db.FetchedValue())
    password = db.Column(db.String(60), index=True)
    name = db.Column(db.String(128), nullable=False)
    bornyear = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    email = db.Column(db.String(512), nullable=False)
    email2 = db.Column(db.String(512))
    homepage = db.Column(db.String(1024))
    info = db.Column(db.String(2048))
    location = db.Column(db.String(2048), nullable=False)
    date = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    hobbies = db.Column(db.Text)
    open = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue())
    extrainfo = db.Column(db.String(2048))
    sukupuoli = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    icq = db.Column(db.String(15))
    apulainen = db.Column(db.Integer, server_default=db.FetchedValue())
    last_login = db.Column(db.DateTime)
    chat = db.Column(db.Integer)
    oikeus = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    lang_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    login_count = db.Column(db.BigInteger)
    lastloginip = db.Column(db.String(128))
    lastloginclient = db.Column(db.String(128))
    address = db.Column(db.Text, nullable=False)
    postnumber = db.Column(db.String(16), nullable=False)
    emails = db.Column(db.Integer, server_default=db.FetchedValue())
    puhelin = db.Column(db.String(16))
    kantaasiakasnro = db.Column(db.String(32))
    lamina_lisatieto = db.Column(db.String(256))
    blogs = db.Column(db.BigInteger)
    user_showid = db.Column(db.BigInteger)
    blog_level = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    last_login2 = db.Column(db.DateTime, index=True)
    messenger = db.Column(db.String(50))
    myspace = db.Column(db.String(50))
    rss = db.Column(db.String(100))
    youtube = db.Column(db.String(50))
    ircgalleria = db.Column(db.String(50))
    last_profile_update = db.Column(db.DateTime)
    avatar = db.Column(db.String(100))
    flickr_username = db.Column(db.String(256))

class LoggedInUser(db.Model):
    __tablename__ = 'user_online'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, index=True, server_default=db.FetchedValue())
    created_time = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())