import os, uuid
import datetime
from flask import Flask, request, flash, g, render_template, jsonify, session, redirect, url_for, escape
import requests, json
from urllib.parse import urljoin # Python 3
from flask_paginate import Pagination, get_page_args

from azure.storage import CloudStorageAccount
from azure.storage.blob import BlockBlobService, PublicAccess

from app.models import Uploads, Media, Story, Page, User, LoggedInUser, StoryType, Genre, MediaType, Country
from app.models import Links, LinkCategories
from app.models import MapSpot, MapCountry, MapTown, MapType

from . import app, db, utils, auto

@app.route('/')
def home():

    #app.logger.warning('A warning occurred (%d apples)', 42)
    #app.logger.error('An error occurred')
    #app.logger.info('Navigated to home() route')

    interviews = Story.query.filter_by(storytype_id=utils.get_storytype_id('interviews')).filter_by(hidden=0).order_by(Story.create_time.desc()).limit(10)
    news = Story.query.filter_by(storytype_id=utils.get_storytype_id('news')).filter_by(hidden=0).order_by(Story.create_time.desc()).limit(10)
    reviews = Story.query.filter_by(storytype_id=utils.get_storytype_id('reviews')).filter_by(hidden=0).order_by(Story.create_time.desc()).limit(10)
    spots = MapSpot.query.order_by(MapSpot.paivays.desc()).limit(10)
    links = db.session.query(Links).join(
            LinkCategories, Links.category == LinkCategories.id
        ).add_columns(
            (LinkCategories.name).label("category_name"),
            (Links.name).label("name"),
            (Links.url).label("url")
        ).order_by(
            Links.create_time.desc()
        ).limit(10)

    page, per_page, offset = utils.get_page_args(page_parameter='page', per_page_parameter='per_page')

    photos_skateboarding = Media.query.filter_by(mediatype_id=1).filter_by(genre_id=utils.get_genre_id('skateboarding')).filter_by(hidden=0).order_by(Media.create_time.desc()).limit(offset).limit(per_page)
    photos_snowboarding = Media.query.filter_by(mediatype_id=1).filter_by(genre_id=utils.get_genre_id('snowboarding')).filter_by(hidden=0).order_by(Media.create_time.desc()).limit(offset).limit(per_page)
     
    return render_template('index.html', 
        interviews=interviews, 
        news=news, 
        reviews=reviews,
        spots=spots,
        links=links,
        photos_skateboarding=photos_skateboarding,
        photos_snowboarding=photos_snowboarding,
        #spotchecks=spotchecks,
        #photos_nollagang=photos_nollagang,
        #photos_snowskate=photos_snowskate
        )

@app.route("/online")
def online():
    logged_in_users = LoggedInUser.query.count()
    return render_template("views/online.html", loggend_in_users=logged_in_users)

@app.route("/support")
def support():
    return render_template("views/support.html")

@app.route("/my/stories")
def my_stories():
    if(session and session['logged_in']):
        username = session['username']
        stories = db.session.query(
                Story
            ).join(Genre
            ).join(StoryType
            ).join(Country
            ).add_columns(
                Story.id,
                (Genre.type_name).label("genre"),
                (StoryType.type_name).label("storytype_name"),
                (Country.country_code).label("country_code"),
                Story.media_topic,
                Story.create_time,
                Story.owner,
                Story.hidden
            ).filter(
                Story.owner==username
            ).order_by(
                Story.create_time.desc()
            ).limit(10)
        return render_template("user/my_stories.html", stories=stories)
    else:
        flash("Please login first")
        return redirect(url_for("home"))

@app.route("/my/uploads")
def my_uploads():
    if(session and session['logged_in']):
        # Get records from database
        my_uploads = db.session.query(Uploads).filter(Uploads.user_id==session['user_id']).order_by(Uploads.create_time.desc())
        blobs = []
        for blob in my_uploads:
            blobs.append(blob)
        return render_template("user/my_uploads.html", blobs=blobs)
    else:
        flash("Please login first")
        return redirect(url_for("home"))

@app.route('/blob/delete', methods = ['POST'])
def delete_blob():
    if(session and session['logged_in']):
        if request.method == 'POST':
            # Remove blob
            blob_service = utils.get_azure_blob_service()
            images_container = "images"
            videos_container = "videos"
            blob_path = request.form.get('blob_path')
            blob_name = os.path.basename(blob_path)
            if utils.isImage(blob_name):
                blob_service.delete_blob(images_container, blob_name)
            if utils.isVideo(blob_name):
                blob_service.delete_blob(videos_container, blob_name)
            # Delete a record from database
            upload_id = request.form.get('upload_id')
            Uploads.query.filter_by(id=upload_id).delete()
            db.session.commit()
            flash("File " + blob_name + " was deleted successfully")
    else:
        flash("Please login first")
        return redirect(url_for("home"))
    return redirect(url_for("my_uploads"))