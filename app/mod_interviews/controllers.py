from datetime import datetime

from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify
from app import app, db, utils
from app.models import User, Page, Story, Country, StoryType, MediaType, Genre

mod_interviews = Blueprint('interviews', __name__, url_prefix='/interviews')

@mod_interviews.route('/all')
def all():
    interviews = db.session.query(Story).join(Genre).join(StoryType).join(Country).add_columns(Story.id,
            (Genre.type_name).label("genre"),
            (StoryType.type_name).label("storytype_name"),
            (Country.country_code).label("country_code"),
            Story.media_topic,
            Story.create_time,
            Story.owner).filter(Story.storytype_id==utils.get_storytype_id('interviews')).order_by(Story.create_time.desc())
    return render_template("interviews/interviews.html", interviews=interviews)

@mod_interviews.route('/interview/<id>')
def interview(id):
    interview = Story.query.filter_by(id=id).first()
    return render_template('interviews/interview.html', interview=interview)
