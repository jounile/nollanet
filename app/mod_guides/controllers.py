from datetime import datetime

from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify
from app import app, dba, utils
from app.models import User, Page

mod_guides = Blueprint('guides', __name__, url_prefix='/guides')

@mod_guides.route('/all')
def all():
    guides = Page.query.filter_by(lang_id=2)
    return render_template("guides/guides.html", guides=guides)

@mod_guides.route('/page/<page_id>')
def page(page_id):
    guide = Page.query.filter_by(lang_id=2, page_id=page_id).first()
    return render_template('guides/guide.html', guide=guide)
