from datetime import datetime

from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify
from app import app, dba, utils
from app.models import User, Media, Genre, Storytype, Mediatype, Country

mod_news = Blueprint('news', __name__, url_prefix='/news')

@mod_news.route('/all')
def all():
    selected_genre = 1 # skateboarding by default
    if(request.args.get('genre')):
        selected_genre = request.args.get('genre')

    total = utils.get_total_news_count(selected_genre)
    page, per_page, offset = utils.get_page_args(page_parameter='page', per_page_parameter='per_page')
    news = dba.session.query(
            Media.media_type.in_((4,5,))
        ).join(Genre
        ).join(Mediatype
        ).join(Storytype
        ).join(Country
        ).add_columns(
            Media.media_id,
            (Mediatype.type_name).label("mediatype_name"),
            (Storytype.type_name).label("storytype_name"),
            (Country.country_code).label("country_code"),
            Media.hidden,
            Media.media_topic,
            Media.create_time,
            Media.owner
        ).filter(
            Media.media_genre==selected_genre
        ).filter(
            Media.story_type==utils.get_story_type('news')
        ).filter(
            Media.hidden==0
        ).order_by(
            Media.create_time.desc()
        ).offset(offset).limit(per_page)

    pagination = utils.get_pagination(page=page, per_page=per_page, total=total, record_name=' news', format_total=True, format_number=True,)

    return render_template("news/news.html", news=news, pagination=pagination, selected_genre=selected_genre)

@mod_news.route('/item/<media_id>')
def item(media_id):
    news_item = Media.query.filter_by(media_id=media_id).first()
    return render_template('news/news_item.html', news_item=news_item)
