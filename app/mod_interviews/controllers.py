from datetime import datetime

from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify
from app import app, db, utils
from app.models import User, Page, Media, Country, StoryType, MediaType, Genre

mod_interviews = Blueprint('interviews', __name__, url_prefix='/interviews')

@mod_interviews.route('/all')
def all():
    interviews = db.session.query(Media.mediatype_id.in_((4,5,))).join(Genre).join(MediaType).join(StoryType).join(Country).add_columns(Media.id,
            (Genre.type_name).label("genre"),
            (MediaType.type_name).label("mediatype_name"),
            (StoryType.type_name).label("storytype_name"),
            (Country.country_code).label("country_code"),
            Media.media_topic,
            Media.create_time,
            Media.owner).filter(Media.storytype_id==utils.get_storytype_id('interviews')).order_by(Media.create_time.desc())
    return render_template("interviews/interviews.html", interviews=interviews)

@mod_interviews.route('/interview/<id>')
def interview(id):
    interview = Media.query.filter_by(id=id).first()
    return render_template('interviews/interview.html', interview=interview)
