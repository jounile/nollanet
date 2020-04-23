from datetime import datetime

from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify
from app import app, db, utils
from app.models import User, Story, Genre, MediaType, StoryType, Country

mod_reviews = Blueprint('reviews', __name__, url_prefix='/reviews')

@mod_reviews.route('/all')
def all():
    reviews = db.session.query(
            Story.mediatype_id==5
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
            Story.create_time,
            Story.owner
        ).filter(
            Story.storytype_id==utils.get_storytype_id('reviews')
        ).filter(
            Story.hidden==0
        ).order_by(
            Story.create_time.desc()
        )
    return render_template("reviews/reviews.html", reviews=reviews)


@mod_reviews.route('/review/<id>')
def review(id):
    review = Story.query.filter_by(id=id).first()
    return render_template('reviews/review.html', review=review)
