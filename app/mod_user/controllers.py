import datetime

from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify

from app import app, db, utils
from app.models import User, Comment, Media, Country, Genre, MediaType

mod_user = Blueprint('user', __name__, url_prefix='/user')


@mod_user.route("/media")
def my_media():
    if(session and session['logged_in']):
        username = session['username']
        media = db.session.query(
                Media
            ).join(Genre
            ).join(MediaType
            ).join(Country
            ).add_columns(
                Media.id,
                (Genre.type_name).label("genre"),
                (MediaType.type_name).label("mediatype"),
                (Country.country_code).label("country_code"),
                Media.media_topic,
                Media.create_time,
                Media.owner,
                Media.hidden
            ).filter(
                Media.owner==username
            ).order_by(
                Media.create_time.desc()
            )

        return render_template("user/my_media.html", media=media)
    else:
        flash("Please login first")
        return redirect(url_for("home"))


