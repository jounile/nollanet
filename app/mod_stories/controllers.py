from datetime import datetime

from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify
from app import app, db, utils
from app.models import User, Story, Genre, StoryType, MediaType, Country, Uploads

mod_stories = Blueprint('stories', __name__, url_prefix='/stories')

@mod_stories.route('/all')
def all():
    selected_genre = 1 # skateboarding by default
    if(request.args.get('genre')):
        selected_genre = request.args.get('genre')

    total = utils.get_total_news_count(selected_genre)
    page, per_page, offset = utils.get_page_args(page_parameter='page', per_page_parameter='per_page')
    news = db.session.query(
            Story.mediatype_id==5
        ).join(Genre
        ).join(MediaType
        ).join(StoryType
        ).join(Country
        ).add_columns(
            Story.id,
            (MediaType.type_name).label("mediatype_name"),
            (StoryType.type_name).label("storytype_name"),
            (Country.country_code).label("country_code"),
            Story.hidden,
            Story.media_topic,
            Story.create_time,
            Story.owner
        ).filter(
            Story.genre_id==selected_genre
        ).filter(
            Story.storytype_id==utils.get_storytype_id('news')
        ).filter(
            Story.hidden==0
        ).order_by(
            Story.create_time.desc()
        ).offset(offset).limit(per_page)

    pagination = utils.get_pagination(page=page, per_page=per_page, total=total, record_name=' news', format_total=True, format_number=True,)

    return render_template("stories/stories.html", news=news, pagination=pagination, selected_genre=selected_genre)

@mod_stories.route("/latest")
def latest():
    if(session and session['logged_in'] and session['user_level'] == 1):
        latest = db.session.query(
                Story
            ).join(Genre
            ).join(MediaType
            ).join(StoryType
            ).join(Country
            ).add_columns(
                Story.id,
                (Genre.type_name).label("genre"),
                (MediaType.type_name).label("mediatype_name"),
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

            story = Story(mediatype_id = request.form.get('mediatype_id'),
                        genre_id = request.form.get('genre_id'),
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

            flash("New story created with ID " + str(media.id))

            if(media.mediatype_id == "1"):
                return redirect(url_for("photo", id=media.id))
            elif(media.mediatype_id == "6"):
                if(media.storytype_id == "0"):
                    return redirect(url_for("video", id=media.id))
            elif(media.mediatype_id == "5"):
                if(media.storytype_id == "2"):
                    return redirect(url_for("view_reviews_item", review_id=media.id))
                elif(media.storytype_id == "3"):
                    return redirect(url_for("view_interviews_item", interview_id=media.id))
                elif(media.storytype_id == "4"):
                    return redirect(url_for("view_news_item", news_id=media.id))
            else:
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
                'mediatype_id': request.form.get('mediatype_id'),
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
