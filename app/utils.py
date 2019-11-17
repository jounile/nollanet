
import os
from flask import Flask, jsonify
import datetime
from flask_paginate import Pagination, get_page_args
import string, random

from models import Media

from . import app

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

def get_media_genre_id(genre):
    if(genre == "skateboarding"):
        media_genre = 1
    if(genre == "snowboarding"):
        media_genre = 2
    if(genre == "nollagang"):
        media_genre = 10
    if(genre == "snowskate"):
        media_genre = 11
    return media_genre

def get_total_photos_count_by_genre(media_genre):
    return Media.query.filter_by(media_type=1).filter_by(media_genre=media_genre).filter_by(lang_id=2).count()

def get_total_videos_count_by_genre(media_genre):
    return Media.query.filter_by(media_type=6).filter_by(media_genre=media_genre).filter_by(lang_id=2).count()

def get_total_news_count():
    return Media.query.filter(Media.media_type.in_((4,5,))).filter_by(story_type=4).filter_by(lang_id=2).count()

def write_file(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)

def get_story_type(story_type):
    if(story_type == "general"):
        media_id = 1
    if(story_type == "reviews"):
        media_id = 2
    if(story_type == "interviews"):
        media_id = 3
    if(story_type == "news"):
        media_id = 4
    if(story_type == "other"):
        media_id = 99
    return media_id

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