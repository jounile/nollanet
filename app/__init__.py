import os
from flask import Flask, request, flash, g, render_template, jsonify, session, redirect, url_for, escape
from flask_session import Session
from flask_login import LoginManager, login_user , logout_user , current_user , login_required, UserMixin
from flask_selfdoc import Autodoc
from flask_navigation import Navigation
from flask_sqlalchemy import SQLAlchemy

from .config import DefaultConfig

# Define the WSGI application object
app = Flask(__name__, instance_relative_config=True)

# DefaultConfig
app.config.from_object(DefaultConfig)

# Database connection
dba = SQLAlchemy(app)

# Login
sess = Session()

# Import a module / component using its blueprint handler variable (mod_auth)
from app.mod_auth.controllers import mod_auth as auth_module
from app.mod_youtube.controllers import mod_youtube as youtube_module
from app.mod_soundcloud.controllers import mod_soundcloud as soundcloud_module
from app.mod_facebook.controllers import mod_facebook as facebook_module

# Register blueprint(s)
app.register_blueprint(auth_module)
app.register_blueprint(youtube_module)
app.register_blueprint(soundcloud_module)
app.register_blueprint(facebook_module)

# Flask-Selfdoc
auto = Autodoc(app)

# Flask-Navigation
nav = Navigation(app)

nav.Bar('top', [
    nav.Item('Home', 'home'),
    nav.Item('News', 'news'),
    nav.Item('Youtube', 'youtube.youtube_playlists'),
    #nav.Item('Podcast', 'soundcloud.soundcloud_playlists'),
    #nav.Item('Facebook', 'facebook.facebook_info'),
    nav.Item('Photos', 'view_photos_by_genre', {'genre': 'skateboarding'}, items=[
        nav.Item('Skateboarding', 'view_photos_by_genre', {'genre': 'skateboarding'}),
        nav.Item('Snowboarding', 'view_photos_by_genre', {'genre': 'snowboarding'}),
        #nav.Item('Nollagang', 'view_photos_by_genre', {'genre': 'nollagang'}),
        #nav.Item('Snowskate', 'view_photos_by_genre', {'genre': 'snowskate'}),
    ]),
    nav.Item('Videos', 'view_videos_by_genre', {'genre': 'skateboarding'}, items=[
        nav.Item('Skateboarding', 'view_videos_by_genre', {'genre': 'skateboarding'}),
        nav.Item('Snowboarding', 'view_videos_by_genre', {'genre': 'snowboarding'}),
    ]),
    nav.Item('Stories', 'interviews', items=[
        nav.Item('Interviews', 'interviews'),
        nav.Item('Reviews', 'reviews'),
        nav.Item('Spotchecks', 'spotchecks'),
    ]),
    nav.Item('Guides', 'guides'),
])

nav.Bar('user', [
    nav.Item('My', 'auth.profile', items=[
        nav.Item('Profile', 'auth.profile'),
        nav.Item('Uploads', 'my_uploads'),
        nav.Item('Posts', 'my_posts'),
    ])
])

from . import views

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500

