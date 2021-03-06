from datetime import datetime

from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify
from app import app, db, utils
from app.models import User, Media, Genre, MediaType, StoryType, Country

mod_spotchecks = Blueprint('spotchecks', __name__, url_prefix='/spotchecks')

@mod_spotchecks.route('/spot/<id>')
def spot(id):
    spotcheck = Media.query.filter_by(id=id).first()
    return render_template('spotchecks/spotcheck.html', spotcheck=spotcheck)

@mod_spotchecks.route('/all')
def all():
    spotchecks = Media.query.filter_by(
            mediatype_id=5
        ).join(Genre
        ).join(MediaType
        ).join(StoryType
        ).join(Country
        ).add_columns(
            Media.id,
            (Genre.type_name).label("genre"),
            (MediaType.type_name).label("mediatype_name"),
            (StoryType.type_name).label("storytype_name"),
            (Country.country_code).label("country_code"),
            Media.media_topic,
            Media.create_time,
            Media.owner
        ).filter(
            Media.storytype_id==utils.get_storytype_id('spotchecks')
        ).filter(
            Media.hidden==0
        ).order_by(
            Media.create_time.desc()
        )

    return render_template("spotchecks/spotchecks.html", spotchecks=spotchecks)
