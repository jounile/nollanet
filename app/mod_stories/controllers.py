from datetime import datetime

from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify
from app import app, db, utils
from app.models import User, Story, Genre, StoryType, MediaType, Country, Uploads

mod_stories = Blueprint('stories', __name__, url_prefix='/stories')

@mod_stories.route("/latest")
def latest():
    if(session and session['logged_in'] and session['user_level'] == 1):
        latest = db.session.query(
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
                Story.media_desc,
                Story.create_time,
                Story.owner,
                Story.hidden
            ).order_by(
                Story.create_time.desc()
            ).limit(10)
        return render_template("stories/latest_stories.html", latest=latest)
    else:
        flash("Please login first")
    return redirect(url_for("home"))

@mod_stories.route("/newstory", methods = ['POST', 'GET'])
def new_story():
    if(session and session['logged_in']):
        if request.method == 'POST':

            story = Story(genre_id = request.form.get('genre_id'),
                        country_id = request.form.get('country_id'),
                        storytype_id = request.form.get('storytype_id'),
                        media_topic = request.form.get('media_topic'),
                        media_text = request.form.get('media_text'),
                        media_desc = request.form.get('media_desc'),
                        hidden = request.form.get('hidden') != None,
                        owner = session['username'],
                        create_time = utils.get_now(),
                        lang_id = 2)

            db.session.add(story)
            db.session.commit()
            flash("New story created")
            return redirect(url_for("home"))
        else:
            my_uploads = db.session.query(Uploads).filter(Uploads.user_id==session['user_id']).order_by(Uploads.create_time.desc())
            blobs = []
            for blob in my_uploads:
                blobs.append(blob)
            return render_template("views/user/new_story.html", blobs=blobs)
    else:
        flash("Please login first")
        return redirect(url_for("home"))

@mod_stories.route('/delete', methods = ['POST'])
def delete():
    if(session and session['logged_in'] and session['user_level'] == 1):
        if request.method == 'POST':
            id = request.form.get('id')
            Story.query.filter_by(id=id).delete()
            db.session.commit()
            flash("Record " + id + " was deleted succesfully by " + session['username'] + ".")
    else:
        flash("Please login first")
    return redirect(url_for("home"))

@mod_stories.route("/update/<id>", methods = ['POST', 'GET'])
def update(id):
    if request.method == 'POST':

        story = { 'id': request.form.get('id'),
                'genre_id': request.form.get('genre_id'),
                'storytype_id': request.form.get('storytype_id'),
                'media_topic': request.form.get('media_topic'),
                'media_text': request.form.get('media_text'),
                'media_desc': request.form.get('media_desc'),
                'country_id': request.form.get('country_id'),
                'hidden': request.form.get('hidden') != None }

        if(session and session['logged_in']):
            Story.query.filter_by(id=id).update(story)
            db.session.commit()
            flash("Record " + id + " was updated by user " + session['username'])
            return redirect(url_for("home"))
        else:
            flash("Please login first")
            return redirect(url_for("home"))
    else:
        if(session and session['logged_in']):
            result = Story.query.filter_by(id=id).first()
            return render_template("views/user/update_story.html", result=result)
        else:
            flash("Please login first")
            return redirect(url_for("home"))
