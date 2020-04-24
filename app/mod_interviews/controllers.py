from datetime import datetime

from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify
from app import app, db, utils
from app.models import User, Page, Story, Country, StoryType, MediaType, Genre

mod_interviews = Blueprint('interviews', __name__, url_prefix='/interviews')

@mod_interviews.route('/all')
def all():
    selected_genre = 1 # skateboarding by default
    if(request.args.get('genre')):
        selected_genre = request.args.get('genre')

    total = utils.get_total_interviews_count(selected_genre)
    page, per_page, offset = utils.get_page_args(page_parameter='page', per_page_parameter='per_page')

    interviews = db.session.query(
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
            Story.owner
        ).filter(
            Story.genre_id==selected_genre
        ).filter(
            Story.storytype_id==utils.get_storytype_id('interviews')
        ).order_by(
            Story.create_time.desc()
        ).offset(offset).limit(per_page)

    pagination = utils.get_pagination(page=page, per_page=per_page, total=total, record_name=' news', format_total=True, format_number=True,)

    return render_template("interviews/interviews.html", interviews=interviews, pagination=pagination, selected_genre=selected_genre)

@mod_interviews.route('/interview/<id>')
def interview(id):
    interview = Story.query.filter_by(id=id).first()
    return render_template('interviews/interview.html', interview=interview)
