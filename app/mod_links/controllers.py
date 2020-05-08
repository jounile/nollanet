from datetime import datetime

from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify
from app import app, db, utils
from app.models import User, Links, LinkCategories

mod_links = Blueprint('links', __name__, url_prefix='/links')

@mod_links.route('/all')
def all():
    categories = LinkCategories.query.order_by(LinkCategories.create_time.desc())
    links = Links.query.order_by(Links.create_time.desc())
    return render_template("links/links.html", categories=categories, links=links)


@mod_links.route('/edit')
def edit_links():
    if session.get('logged_in'):
        categories = LinkCategories.query.order_by(LinkCategories.create_time.desc())
        links = Links.query.order_by(Links.create_time.desc())
        return render_template("links/edit_links.html", categories=categories, links=links)


@mod_links.route("/new", methods = ['POST', 'GET'])
def new_link():
    if(session and session['logged_in']):
        if request.method == 'GET':
            categories = LinkCategories.query.order_by(LinkCategories.create_time.desc())
            return render_template("links/new_link.html", categories=categories)
        if request.method == 'POST':

            link = Links(category = request.form.get('category'),
                        name = request.form.get('name'),
                        url = request.form.get('url'),
                        user_id = session['user_id'],
                        create_time = utils.get_now()
                    )

            db.session.add(link)
            db.session.commit()

            flash("New link created with ID " + str(link.id))
            return redirect(url_for("links.all"))
    else:
        flash("Please login first")
        return redirect(url_for("home"))

@mod_links.route("/link/update/<link_id>", methods = ['POST', 'GET'])
def update_link(link_id):
    if(session and session['logged_in']):
        if request.method == 'GET':
            link = Links.query.filter_by(id=link_id).first()
            return render_template("links/update_link.html", link=link)
        if request.method == 'POST':
            link = { 'name': request.form.get('name'),
                    'url': request.form.get('url')}
            Links.query.filter_by(id=link_id).update(link)
            db.session.commit()
            flash("Link " + str(link_id) + " was updated by user " + session['username'])
            return redirect(url_for("links.all"))
    else:
        flash("Please login first")
        return redirect(url_for("home"))

@mod_links.route('/link/delete', methods = ['POST'])
def delete_link():
    if(session and session['logged_in'] and session['user_level'] == 1):
        if request.method == 'POST':
            id = request.form.get('id')
            Links.query.filter_by(id=id).delete()
            db.session.commit()
            flash("Link " + id + " was deleted succesfully by " + session['username'] + ".")
            return redirect(url_for("links.all"))
    else:
        flash("Please login first")
        return redirect(url_for("home"))

@mod_links.route("/category/update/<category_id>", methods = ['POST', 'GET'])
def update_category(category_id):
    if(session and session['logged_in'] and session['user_level'] == 1):
        if request.method == 'GET':
            category = LinkCategories.query.filter_by(id=category_id).first()
            return render_template("links/update_category.html", category=category)
        if request.method == 'POST':
            category = { 'name': request.form.get('name') }
            LinkCategories.query.filter_by(id=category_id).update(category)
            db.session.commit()
            flash("Category " + str(category_id) + " was updated by user " + session['username'])
            return redirect(url_for("links.categories"))
    else:
        flash("Please login first")
        return redirect(url_for("home"))

@mod_links.route('/category/delete', methods = ['POST'])
def delete_category():
    if(session and session['logged_in'] and session['user_level'] == 1):
        if request.method == 'POST':
            id = request.form.get('id')
            LinkCategories.query.filter_by(id=id).delete()
            db.session.commit()
            flash("Link category " + id + " was deleted succesfully by " + session['username'] + ".")
            return redirect(url_for("links.all"))
    else:
        flash("Please login first")
        return redirect(url_for("home"))

@mod_links.route("/category/new", methods = ['POST', 'GET'])
def new_category():
    if(session and session['logged_in']):
        if request.method == 'POST':

            category = LinkCategories(name = request.form.get('category_name'),
                        user_id = session['user_id'],
                        create_time = utils.get_now()
                    )

            db.session.add(category)
            db.session.commit()

            flash("New link category created with ID " + str(category.id))
            return redirect(url_for("links.all"))
        if request.method == 'GET':
            return render_template("links/new_category.html")
    else:
        flash("Please login first")
        return redirect(url_for("home"))

@mod_links.route("/latest")
def latest():
    if(session and session['logged_in'] and session['user_level'] == 1):
        links = db.session.query(Links).order_by(Links.create_time.desc()).limit(10)
        return render_template("links/latest_links.html", links=links)
    else:
        flash("Please login first")
    return redirect(url_for("home"))

@mod_links.route("/categories")
def categories():
    if(session and session['logged_in']):
        categories = db.session.query(LinkCategories).order_by(LinkCategories.create_time.desc())
        return render_template("links/categories.html", categories=categories)
    else:
        flash("Please login first")
    return redirect(url_for("home"))