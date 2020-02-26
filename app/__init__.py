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
from app.mod_spots.controllers import mod_spots as spots_module
from app.mod_youtube.controllers import mod_youtube as youtube_module
from app.mod_soundcloud.controllers import mod_soundcloud as soundcloud_module
from app.mod_facebook.controllers import mod_facebook as facebook_module

# Register blueprint(s)
app.register_blueprint(auth_module)
app.register_blueprint(spots_module)
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
    nav.Item('Media', 'view_media'),
    nav.Item('Interviews', 'interviews'),
    nav.Item('Reviews', 'reviews'),
    #nav.Item('Spotchecks', 'spotchecks'),
    nav.Item('Spots', 'spots.all'),
    nav.Item('Links', 'links'),
])

nav.Bar('user', [
    nav.Item('My', 'auth.profile', items=[
        nav.Item('Profile', 'auth.profile'),
        nav.Item('Password', 'auth.pwdreset'),
        nav.Item('Uploads', 'my_uploads'),
        nav.Item('Posts', 'my_posts'),
        nav.Item('New spot', 'spots.new_spot'),
    ])
])

from . import views

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500

