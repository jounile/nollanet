from datetime import datetime

from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify
from app import app, db, utils
from app.models import User, Page

mod_admin = Blueprint('admin', __name__, url_prefix='/admin')

@mod_admin.route('/stories')
def stories():
    if session.get('logged_in') and session.get('user_level') == 1:    
        return render_template("admin/stories.html")
    else:
        flash('You are not logged in as administrator')
        return redirect(url_for('home'))

@mod_admin.route('/media')
def media():
    if session.get('logged_in') and session.get('user_level') == 1:    
        return render_template("admin/media.html")
    else:
        flash('You are not logged in as administrator')
        return redirect(url_for('home')) 

@mod_admin.route('/users')
def users():
    if session.get('logged_in') and session.get('user_level') == 1:    
        return render_template("admin/users.html")
    else:
        flash('You are not logged in as administrator')
        return redirect(url_for('home'))

@mod_admin.route("/users/newest")
def users_newest():
    if(session and session['logged_in'] and session['user_level'] == 1):
        newest_users = db.session.query(User).order_by(User.date.desc()).limit(20)
        return render_template("admin/newest_users.html", newest_users=newest_users)
    else:
        flash("Please login first")
    return redirect(url_for("home"))

@mod_admin.route("/logins/latest")
def logins_latest():
    if(session and session['logged_in'] and session['user_level'] == 1):
        latest_logins = db.session.query(User).order_by(User.last_login.desc()).limit(20)
        return render_template("admin/latest_logins.html", latest_logins=latest_logins)
    else:
        flash("Please login first")
    return redirect(url_for("home"))

@mod_admin.route('/promote', methods=['GET','POST'])
def promote():
    if session.get('logged_in') and session.get('user_level') == 1:
        if request.method == 'GET':
            return render_template('admin/promote.html')
        if request.method == 'POST':
            username = request.form.get('username')
            level = request.form.get('level')
            User.query.filter_by(username=username).update({"level": level})
            db.session.commit()
            flash('User '+ username + ' is now updated to level ' + level + '.')
            return redirect(url_for('home'))
    else:
        flash('You are not logged in as administrator')
        return redirect(url_for('home'))

@mod_admin.route('/spots')
def spots():
    if session.get('logged_in') and session.get('user_level') == 1:    
        return render_template("admin/spots.html")
    else:
        flash('You are not logged in as administrator')
        return redirect(url_for('home'))

@mod_admin.route('/links')
def links():
    if session.get('logged_in') and session.get('user_level') == 1:    
        return render_template("admin/links.html")
    else:
        flash('You are not logged in as administrator')
        return redirect(url_for('home'))
    
