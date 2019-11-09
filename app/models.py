from . import dba
from sqlalchemy import inspect

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