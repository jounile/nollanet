
import os
from flask import Flask, jsonify
import datetime
from flask_paginate import Pagination, get_page_args

from . import app, db

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
    cursor = db.connection.cursor()
    sql = "SELECT count(*) FROM media_table WHERE media_type=1 AND media_genre=%s AND lang_id=2"
    cursor.execute(sql, (media_genre, ))
    total = cursor.fetchone()[0]
    return total

def get_total_videos_count_by_genre(media_genre):
    cursor = db.connection.cursor()
    sql = "SELECT count(*) FROM media_table WHERE media_type=6 AND media_genre=%s AND lang_id=2"
    cursor.execute(sql, (media_genre, ))
    total = cursor.fetchone()[0]
    return total

def create_story_json(media_id, media_topic, media_text, media_desc, create_time, owner):
    if(create_time):
        create_time = create_time.strftime('%d/%m/%Y %H:%M')
    
    storyJson = {
        'media_id': media_id,
        'media_topic': media_topic,
        'media_text': media_text,
        'media_desc': media_desc,
        'create_time': create_time,
        'owner': owner
        }
    return storyJson

def create_photo_json(media_id, media_topic, create_time, owner):
    photoJson = {
        'media_id': media_id,
        'media_topic': media_topic,
        'create_time': create_time.strftime('%d/%m/%Y %H:%M'),
        'owner': owner,
        'tn': app.config.get("AZURE_BLOB") + '/thumbs/' + str(media_id) + '_50.jpg',
        'img': app.config.get("AZURE_BLOB") + '/thumbs/' + str(media_id) + '_400.jpg',
        }
    return photoJson

def create_video_json(media_id, media_topic, create_time, owner):
    videoJson = {
        'media_id': media_id,
        'media_topic': media_topic,
        'create_time': create_time.strftime('%d/%m/%Y %H:%M'),
        'owner': owner,
        'tn': app.config.get("AZURE_BLOB") + '/thumbs/' + str(media_id) + '_50.jpg',
        'video': app.config.get("AZURE_BLOB") + '/flv/' + str(media_id) + '.flv'
        }
    return videoJson

def query_result_to_json(cursor, result):
    json = [dict((cursor.description[i][0], value)
        for i, value in enumerate(row)) for row in result]
    return jsonify(json)

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
