
import os
from flask import Flask, jsonify, session
import datetime
from flask_paginate import Pagination, get_page_args
import string, random

from azure.storage import CloudStorageAccount
from azure.storage.blob import BlockBlobService, PublicAccess

from app.models import Media

from . import app

def get_azure_blob_service():
    account = app.config.get('AZURE_ACCOUNT')
    key = app.config.get('AZURE_STORAGE_KEY')
    account = CloudStorageAccount(account_name=account, account_key=key)
    return account.create_block_blob_service()

def get_css_framework():
    return app.config.get('CSS_FRAMEWORK', 'bootstrap4')


def get_link_size():
    return app.config.get('LINK_SIZE', 'sm')


def get_alignment():
    return app.config.get('LINK_ALIGNMENT', '')


def show_single_page_or_not():
    return app.config.get('SHOW_SINGLE_PAGE', False)


def get_pagination(**kwargs):
    kwargs.setdefault('record_name', 'records')
    return Pagination(css_framework=get_css_framework(),
                      link_size=get_link_size(),
                      alignment=get_alignment(),
                      show_single_page=show_single_page_or_not(),
                      **kwargs
                      )

def get_genre_id(genre):
    if(genre == "skateboarding"):
        genre_id = 1
    if(genre == "snowboarding"):
        genre_id = 2
    if(genre == "nollagang"):
        genre_id = 3
    if(genre == "snowskate"):
        genre_id = 4
    if(genre == "none"):
        genre_id = 5
    return genre_id

def get_mediatype_id(mediatype):
    if(mediatype == "photo"):
        mediatype_id = 1
    if(mediatype == "mediatype2"):
        mediatype_id = 2
    if(mediatype == "music"):
        mediatype_id = 3
    if(mediatype == "movies"):
        mediatype_id = 4
    if(mediatype == "stories"):
        mediatype_id = 5
    if(mediatype == "video"):
        mediatype_id = 6
    if(mediatype == "none"):
        mediatype_id = 7
    return mediatype_id

def get_count_by_genre_and_type(selected_genre_id, selected_mediatype_id):
    return Media.query.filter_by(
            genre_id=selected_genre_id
        ).filter_by(
            mediatype_id=selected_mediatype_id
        ).filter_by(
            hidden=0
        ).count()

def get_total_news_count(selected_genre):
    return Media.query.filter(Media.mediatype_id.in_((4,5,))).filter(Media.genre_id==selected_genre).filter_by(storytype_id=4).filter_by(lang_id=2).filter_by(hidden=0).count()

def write_file(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)

def get_storytype_id(storytype_id):
    if(storytype_id == "general"):
        type_id = 1
    if(storytype_id == "reviews"):
        type_id = 2
    if(storytype_id == "interviews"):
        type_id = 3
    if(storytype_id == "news"):
        type_id = 4
    if(storytype_id == "other"):
        type_id = 5
    if(storytype_id == "spotchecks"):
        type_id = 6
    if(storytype_id == "none"):
        type_id = 7
    return type_id

def convertDateTime(datetimestr):
    date_time_obj = datetime.datetime.strptime(datetimestr, '%a, %d %b %Y %H:%M:%S GMT')
    date_time_obj = date_time_obj.strftime('%d/%m/%Y %H:%M:%S')
    return date_time_obj

def get_now():
    utcnow = datetime.datetime.utcnow()
    now = utcnow.strftime('%Y-%m-%d %H:%M:%S')
    return now

def allowed_file(filename):
	ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def id_generator(size=32, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
