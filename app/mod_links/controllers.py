from datetime import datetime

from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify
from app import app, dba, utils
from app.models import User, Links, LinkCategories

mod_links = Blueprint('links', __name__, url_prefix='/links')

@mod_links.route('/all')
def all():
    categories = LinkCategories.query.order_by(LinkCategories.create_time.desc())
    links = Links.query.order_by(Links.create_time.desc())
    return render_template("links/links.html", categories=categories, links=links)


@mod_links.route('/links/edit')
def edit_links():
    if session.get('logged_in') and session.get('user_level') == 1:
        categories = LinkCategories.query.order_by(LinkCategories.create_time.desc())
        links = Links.query.order_by(Links.create_time.desc())
        return render_template("links/edit_links.html", categories=categories, links=links)


@mod_links.route("/newlink", methods = ['POST', 'GET'])
def new_link():
    if(session and session['logged_in'] and session['user_level'] == 1):
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

            dba.session.add(link)
            dba.session.commit()

            flash("New link created with ID " + str(link.id))
            return redirect(url_for("links.all"))
    else:
        flash("Please login first")
        return redirect(url_for("home"))

@mod_links.route("/link/update/<link_id>", methods = ['POST', 'GET'])
def update_link(link_id):
    if(session and session['logged_in'] and session['user_level'] == 1):
        if request.method == 'GET':
            link = Links.query.filter_by(id=link_id).first()
            return render_template("links/update_link.html", link=link)
        if request.method == 'POST':
            link = { 'name': request.form.get('name'),
                    'url': request.form.get('url')}
            Links.query.filter_by(id=link_id).update(link)
            dba.session.commit()
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
            dba.session.commit()
            flash("Link " + id + " was deleted succesfully by " + session['username'] + ".")
            return redirect(url_for("links.all"))
    else:
        flash("Please login first")
        return redirect(url_for("home"))

@mod_links.route('/linkcategory/delete', methods = ['POST'])
def delete_linkcategory():
    if(session and session['logged_in'] and session['user_level'] == 1):
        if request.method == 'POST':
            id = request.form.get('id')
            LinkCategories.query.filter_by(id=id).delete()
            dba.session.commit()
            flash("Link category " + id + " was deleted succesfully by " + session['username'] + ".")
            return redirect(url_for("links.all"))
    else:
        flash("Please login first")
        return redirect(url_for("home"))

@mod_links.route("/newcategory", methods = ['POST', 'GET'])
def new_category():
    if(session and session['logged_in'] and session['user_level'] == 1):
        if request.method == 'POST':

            category = LinkCategories(name = request.form.get('category_name'),
                        user_id = session['user_id'],
                        create_time = utils.get_now()
                    )

            dba.session.add(category)
            dba.session.commit()

            flash("New link category created with ID " + str(category.id))
            return redirect(url_for("links.all"))
        if request.method == 'GET':
            return render_template("links/new_linkcategory.html")
    else:
        flash("Please login first")
        return redirect(url_for("home"))
