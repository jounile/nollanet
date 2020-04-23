from datetime import datetime

from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify
from app import app, db, utils
from app.models import User, Story, Genre, StoryType, MediaType, Country

mod_news = Blueprint('news', __name__, url_prefix='/news')

@mod_news.route('/all')
def all():
    selected_genre = 1 # skateboarding by default
    if(request.args.get('genre')):
        selected_genre = request.args.get('genre')

    total = utils.get_total_news_count(selected_genre)
    page, per_page, offset = utils.get_page_args(page_parameter='page', per_page_parameter='per_page')
    news = db.session.query(
            Story
        ).join(Genre
        ).join(StoryType
        ).join(Country
        ).add_columns(
            Story.id,
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

    return render_template("news/news.html", news=news, pagination=pagination, selected_genre=selected_genre)

@mod_news.route('/item/<id>')
def item(id):
    news_item = Story.query.filter_by(id=id).first()
    return render_template('news/news_item.html', news_item=news_item)

@mod_news.route("/latest")
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
        return render_template("news/latest_news.html", latest=latest)
    else:
        flash("Please login first")
    return redirect(url_for("home"))