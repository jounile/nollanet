import os
from flask import Flask, request, flash, g, render_template, jsonify, session, redirect, url_for, escape
import requests, json

try:
    from urllib.parse import urljoin # Python 3.6
except ImportError:
    from urlparse import urljoin # Python 2.7

from . import app, db, utils, auto

@app.route('/media/<path:filename>', methods=['GET'])
def media(filename):
    static_url = app.config.get('AZURE_BLOB')
    if static_url:
        return redirect(urljoin(static_url, filename))
    return app.send_static_file(filename)

@app.route('/api/user/<string:username>/', methods=['GET'])
@auto.doc()
def get_user(username):
    cursor = db.connection.cursor()
    cursor.execute("SELECT user_id, username, name, email, location, address, postnumber, bornyear, email2, homepage, info, date, hobbies, extrainfo, sukupuoli, icq, apulainen, last_login, chat, oikeus, lang_id, login_count, lastloginip, lastloginclient, emails, puhelin, kantaasiakasnro, lamina_lisatieto, blogs, user_showid, messenger, myspace, rss, youtube, ircgalleria, last_profile_update, avatar, flickr_username FROM users WHERE username=%s", (username, ))
    result = cursor.fetchall()
    return utils.query_result_to_json(cursor, result)

@app.route('/api/users')
@auto.doc()
def get_users():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    return utils.query_result_to_json(cursor, result)

@app.route('/api/guides')
@auto.doc()
def get_guides():
    cursor = db.connection.cursor()
    cursor.execute("SELECT id, page_id, header FROM general WHERE lang_id=2")
    result = cursor.fetchall()
    return utils.query_result_to_json(cursor, result)

@app.route('/api/stories/<type>/')
@auto.doc()
def get_stories(type):
    page, per_page, offset = utils.get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    story_type = utils.get_story_type(type)
    cursor = db.connection.cursor()
    if (request.args.get('newest')):
        cursor.execute("SELECT media_id, media_topic, story_type, media_text, media_desc, create_time, owner FROM media_table WHERE media_type IN (4,5) AND story_type=%s AND lang_id=2 ORDER BY create_time desc LIMIT 10", (story_type, ))
    else:
        cursor.execute("SELECT media_id, media_topic, story_type, media_text, media_desc, create_time, owner FROM media_table WHERE media_type IN (4,5) AND story_type=%s AND lang_id=2 ORDER BY create_time DESC limit %s, %s", (story_type, offset, per_page))
    result = cursor.fetchall()
    stories = []

    for item in result:
        media_id = item[0]
        media_topic = item[1]
        story_type = item[2]
        media_text = item[3]
        media_desc = item[4]
        create_time = item[5]
        owner = item[6]
        storyJson = utils.create_story_json(media_id, media_topic, media_text, media_desc, create_time, owner)
        stories.append(storyJson)
    return jsonify(stories)


@app.route('/api/news/<media_id>/')
@auto.doc()
def get_news_item(media_id):
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM media_table WHERE media_id=%s", (media_id, ))
    result = cursor.fetchall()
    return utils.query_result_to_json(cursor, result)

@app.route('/api/photos/newest')
@auto.doc()
def get_photos_newest():
    cursor = db.connection.cursor()
    cursor.execute("SELECT media_id, media_topic FROM media_table WHERE media_type=1 AND media_genre < 9 AND media_file_size > 20000 AND lang_id=2 ORDER BY create_time desc LIMIT 0,10")
    result = cursor.fetchall()
    return utils.query_result_to_json(cursor, result)

@app.route('/api/videos/newest')
@auto.doc()
def get_videos_newest():
    cursor = db.connection.cursor()
    cursor.execute("SELECT media_id, media_topic FROM media_table WHERE media_type=3 AND media_file_size > 30000 AND lang_id=2 ORDER BY create_time desc LIMIT 0,10")
    result = cursor.fetchall()
    return utils.query_result_to_json(cursor, result)

@app.route('/api/movies/newest')
@auto.doc()
def get_movies_newest():
    cursor = db.connection.cursor()
    cursor.execute("SELECT media_id, media_topic, media_text FROM media_table WHERE media_type=6 AND lang_id=2 ORDER BY create_time desc LIMIT 0,10")
    result = cursor.fetchall()
    return utils.query_result_to_json(cursor, result)

@app.route('/api/guide/<string:guide_id>/')
@auto.doc()
def get_page(guide_id):
    cursor = db.connection.cursor()
    cursor.execute("SELECT id, page_id, header, text, info FROM general WHERE page_id=%s AND lang_id=2", (guide_id, ))
    result = cursor.fetchall()
    return utils.query_result_to_json(cursor, result)

@app.route('/api/story/<string:media_id>/')
@auto.doc()
def get_story(media_id):
    cursor = db.connection.cursor()
    cursor.execute("SELECT media_id, media_topic, story_type, media_desc, media_text, create_time, owner FROM media_table WHERE media_id=%s", (media_id, ))
    result = cursor.fetchall()
    stories = []

    for item in result:
        media_id = item[0]
        media_topic = item[1]
        story_type = item[2]
        media_desc = item[3]
        media_text = item[4]
        create_time = item[5]
        owner = item[6]
        storyJson = utils.create_story_json(media_id, media_topic, media_text, media_desc, create_time, owner)
        stories.append(storyJson)
    return jsonify(stories)

@app.route('/api/photos/<string:genre>/')
@auto.doc()
def get_photos_by_genre(genre):
    media_genre = utils.get_media_genre_id(genre)

    page, per_page, offset = utils.get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    cursor = db.connection.cursor()
    cursor.execute("SELECT media_id, media_topic, create_time, owner FROM media_table WHERE media_type=1 AND media_genre=%s AND lang_id=2 ORDER BY create_time DESC limit %s, %s", (media_genre, offset, per_page))
    result = cursor.fetchall()
    photos = []

    for item in result:
        photoJson = utils.create_photo_json(item[0], item[1], item[2], item[3])
        photos.append(photoJson)
    return jsonify(photos)

@app.route('/api/videos/<string:genre>/')
@auto.doc()
def get_videos_by_genre(genre):
    media_genre = utils.get_media_genre_id(genre)

    page, per_page, offset = utils.get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')

    cursor = db.connection.cursor()
    cursor.execute("SELECT media_id, media_topic, create_time, owner FROM media_table WHERE media_type=6 AND media_genre=%s AND lang_id=2 ORDER BY create_time DESC limit %s, %s", (media_genre, offset, per_page))
    result = cursor.fetchall()

    videos = []

    for item in result:
        media_id = item[0]
        media_topic = item[1].encode('utf-8')
        create_time = item[2]
        owner = item[3]
        videoJson = utils.create_video_json(media_id, media_topic, create_time, owner)
        videos.append(videoJson)
    return jsonify(videos)

@app.route('/api/photo/<media_id>')
@auto.doc()
def get_photo(media_id):
    cursor = db.connection.cursor()
    cursor.execute("SELECT media_id, media_topic, media_text, media_desc, owner, create_time FROM media_table WHERE media_id=%s", (media_id, ))
    result = cursor.fetchall()
    return utils.query_result_to_json(cursor, result)

@app.route('/api/comments/<int:media_id>')
@auto.doc()
def api_comments(media_id):
    cursor = db.connection.cursor()
    cursor.execute("SELECT k.user_id, u.username, k.header, k.comment, k.timestamp, k.media_id, k.comment_user_id, k.youtube_id, k.tapahtuma_id, k.diary_id FROM kommentti k, users u WHERE k.user_id = u.user_id AND media_id = %s ORDER BY k.id desc LIMIT 0, 100", (media_id, ))
    result = cursor.fetchall()
    return utils.query_result_to_json(cursor, result)

@app.route('/api/videos')
@auto.doc()
def api_videos():
    cursor = db.connection.cursor()
    cursor.execute("SELECT media_id, media_topic, owner, create_time FROM media_table WHERE media_type=6 AND lang_id=2 ORDER BY create_time DESC")
    result = cursor.fetchall()
    return utils.query_result_to_json(cursor, result)

@app.route('/api/video/<int:media_id>')
@auto.doc()
def api_video(media_id):
    cursor = db.connection.cursor()
    cursor.execute("SELECT media_id, media_topic, media_text, media_genre, media_desc, owner, create_time FROM media_table WHERE media_type=6 AND media_id=%s AND lang_id=2", (media_id, ))
    result = cursor.fetchall()
    return utils.query_result_to_json(cursor, result)

@app.route('/api/latest')
@auto.doc()
def api_latest():
    cursor = db.connection.cursor()
    cursor.execute("SELECT media_id, media_type, story_type, media_topic, media_text, media_desc, owner, create_time FROM media_table ORDER BY create_time DESC LIMIT 10")
    result = cursor.fetchall()
    return utils.query_result_to_json(cursor, result)
