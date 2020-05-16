from datetime import datetime

from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify
from app import app, db, utils
from app.models import User

mod_users = Blueprint('users', __name__, url_prefix='/users')

@mod_users.route('/user/<username>', methods=['GET'])
def user(username):
    user = User.query.filter_by(username=username).first()
    return render_template('users/user.html', user=user)
