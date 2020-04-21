import os
from flask import Flask, request, flash, g, render_template, jsonify, session, redirect, url_for, escape
from flask_session import Session
from flask_login import LoginManager, login_user , logout_user , current_user , login_required, UserMixin
from flask_selfdoc import Autodoc
from flask_navigation import Navigation
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from applicationinsights.flask.ext import AppInsights

from .config import DefaultConfig

# Define the WSGI application object
app = Flask(__name__, instance_relative_config=True)

# DefaultConfig
app.config.from_object(DefaultConfig)

# Azure Application Insights
appinsights = AppInsights(app)

# Database connection
db = SQLAlchemy(app)

# Database migration
migrate = Migrate(app, db)

# Login
sess = Session()

# Import a module / component using its blueprint handler variable (mod_auth)
from app.mod_auth.controllers import mod_auth as auth_module
from app.mod_spots.controllers import mod_spots as spots_module
from app.mod_links.controllers import mod_links as links_module
from app.mod_media.controllers import mod_media as media_module
from app.mod_spotchecks.controllers import mod_spotchecks as spotchecks_module
from app.mod_guides.controllers import mod_guides as guides_module
from app.mod_interviews.controllers import mod_interviews as interviews_module
from app.mod_reviews.controllers import mod_reviews as reviews_module
from app.mod_news.controllers import mod_news as news_module
from app.mod_users.controllers import mod_users as users_module

from app.mod_youtube.controllers import mod_youtube as youtube_module
from app.mod_facebook.controllers import mod_facebook as facebook_module

# Register blueprint(s)
app.register_blueprint(auth_module)
app.register_blueprint(spots_module)
app.register_blueprint(links_module)
app.register_blueprint(media_module)
app.register_blueprint(spotchecks_module)
app.register_blueprint(guides_module)
app.register_blueprint(interviews_module)
app.register_blueprint(reviews_module)
app.register_blueprint(news_module)
app.register_blueprint(users_module)

app.register_blueprint(youtube_module)
app.register_blueprint(facebook_module)

# Flask-Selfdoc
auto = Autodoc(app)

# Flask-Navigation
nav = Navigation(app)

nav.Bar('top', [
    nav.Item('Home', 'home'),
    nav.Item('News', 'news.all'),
    nav.Item('Youtube', 'youtube.youtube_playlists'),
    nav.Item('Media', 'media.all'),
    nav.Item('Interviews', 'interviews.all'),
    nav.Item('Reviews', 'reviews.all'),
    nav.Item('Spots', 'spots.all'),
    nav.Item('Links', 'links.all'),
])

nav.Bar('user', [
    nav.Item('My', 'auth.profile', items=[
        nav.Item('Profile', 'auth.profile'),
        nav.Item('Password', 'auth.pwdreset'),
        nav.Item('My Uploads', 'my_uploads'),
        nav.Item('My Posts', 'my_posts'),
        nav.Item('New upload', 'media.new_upload'),
        nav.Item('New post', 'new_post'),
        nav.Item('New spot', 'spots.new_spot'),
        nav.Item('New link', 'links.new_link'),
    ])
])

from . import views

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500

