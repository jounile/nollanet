from datetime import datetime

from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify
from app import app, dba, utils
from app.models import User, Media, Genre, MediaType, StoryType, Country

mod_reviews = Blueprint('reviews', __name__, url_prefix='/reviews')

@mod_reviews.route('/all')
def all():
    reviews = dba.session.query(
            Media.media_type.in_((4,5,))
        ).join(Genre
        ).join(MediaType
        ).join(StoryType
        ).join(Country
        ).add_columns(
            Media.media_id,
            (Genre.type_name).label("genre"),
            (MediaType.type_name).label("mediatype_name"),
            (StoryType.type_name).label("storytype_name"),
            (Country.country_code).label("country_code"),
            Media.media_topic,
            Media.create_time,
            Media.owner
        ).filter(
            Media.story_type==utils.get_story_type('reviews')
        ).filter(
            Media.hidden==0
        ).order_by(
            Media.create_time.desc()
        )
    return render_template("reviews/reviews.html", reviews=reviews)


@mod_reviews.route('/review/<media_id>')
def review(media_id):
    review = Media.query.filter_by(media_id=media_id).first()
    return render_template('reviews/review.html', review=review)
