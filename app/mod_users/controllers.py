from datetime import datetime

from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify
from app import app, db, utils
from app.models import User

mod_users = Blueprint('users', __name__, url_prefix='/users')

@mod_users.route('/user/<username>', methods=['GET'])
def user(username):
    user = User.query.filter_by(username=username).first()
    return render_template('users/user.html', user=user)

@mod_users.route("/newest")
def newest():
    if(session and session['logged_in'] and session['user_level'] == 1):
        newest_users = db.session.query(User).order_by(User.date.desc()).limit(20)
        return render_template("users/newest_users.html", newest_users=newest_users)
    else:
        flash("Please login first")
    return redirect(url_for("home"))

@mod_users.route("/logins/latest")
def latest_logins():
    if(session and session['logged_in'] and session['user_level'] == 1):
        latest_logins = db.session.query(User).order_by(User.last_login.desc()).limit(20)
        return render_template("users/latest_logins.html", latest_logins=latest_logins)
    else:
        flash("Please login first")
    return redirect(url_for("home"))

