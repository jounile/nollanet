import os
from datetime import datetime

from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from app import app, db, utils
from app.models import User, MapSpot, MapCountry, MapTown, MapType

from app.mod_spots.form import NewSpotForm, UpdateSpotForm, CountryForm, TownForm, NewTypeForm

mod_spots = Blueprint('spots', __name__, url_prefix='/spots')

key = app.config.get('GOOGLE_API_KEY')
GoogleMaps(app, key=key)

@mod_spots.route('/all')
def all():

    selected_maa_id = 0
    if(request.args.get('maa_id')):
        selected_maa_id = int(request.args.get('maa_id'))

    selected_paikkakunta_id = 0
    if(request.args.get('paikkakunta_id')):
        selected_paikkakunta_id = int(request.args.get('paikkakunta_id'))

    selected_type_id = 0
    if(request.args.get('type_id')):
        selected_type_id = int(request.args.get('type_id'))

    countries = MapCountry.query.order_by(MapCountry.maa.asc())
    towns = MapTown.query.filter(MapTown.maa_id==selected_maa_id).order_by(MapTown.paikkakunta.asc())
    types = MapType.query.order_by(MapType.name.asc())
    spots = MapSpot.query.filter_by(maa_id=selected_maa_id).order_by(MapSpot.paivays.desc())

    map_center_lat = 60.186427
    map_center_lon = 24.934886
    map_zoom_level = 5

    if selected_maa_id != 0:
        country = MapCountry.query.filter_by(id=selected_maa_id).first()
        map_center_lat = country.lat
        map_center_lon = country.lon
        map_zoom_level = 3
        spots = spots.filter_by(maa_id=selected_maa_id)

    if selected_paikkakunta_id != 0:
        town = MapTown.query.filter_by(id=selected_paikkakunta_id).first()
        map_center_lat = town.lat
        map_center_lon = town.lon
        map_zoom_level = 11
        spots = spots.filter_by(paikkakunta_id=selected_paikkakunta_id)

    if selected_type_id != 0:
        spots = spots.filter_by(tyyppi=selected_type_id)

    # spot markers
    markers = []
    for spot in spots:
        if(spot.latlon):
            lat_lon = (spot.latlon).split(",")
            marker = (lat_lon[0], lat_lon[1], spot.nimi)
            markers.append(marker)

    # creating a map in the view
    mymap = Map(
        identifier="view-side",
        style="height:400px;width:1170px;margin:0;",
        zoom=map_zoom_level,
        lat=map_center_lat,
        lng=map_center_lon,
        markers=markers
    )

    return render_template("spots/spots.html", mymap=mymap, spots=spots, countries=countries, towns=towns, types=types, selected_maa_id=selected_maa_id, selected_paikkakunta_id=selected_paikkakunta_id, selected_type_id=selected_type_id)

@mod_spots.route('/spot/<kartta_id>')
def spot(kartta_id):

    spot = db.session.query(
            MapSpot
        ).filter_by(
            kartta_id=kartta_id
        ).join(
            User, MapSpot.user_id == User.user_id
        ).join(
            MapCountry, MapSpot.maa_id == MapCountry.id
        ).join(
            MapTown, MapSpot.paikkakunta_id == MapTown.id
        ).join(
            MapType, MapSpot.tyyppi == MapType.id
        ).add_columns(
            (User.username).label("username"),
            (MapSpot.nimi).label("name"),
            (MapSpot.user_id).label("user_id"),
            (MapCountry.maa).label("maa"),
            (MapTown.paikkakunta).label("paikkakunta"),
            (MapType.name).label("type"),
            (MapSpot.info).label("info"),
            (MapSpot.paivays).label("paivays"),
            (MapSpot.karttalinkki).label("link"),
            (MapSpot.temp).label("temp"),
            (MapSpot.latlon).label("latlon"),
        ).first()

    return render_template('spots/spot.html', spot=spot, key=key)

@mod_spots.route("/spot/new", methods = ['POST', 'GET'])
def new_spot():
    if(session and session['logged_in']):
        form = NewSpotForm()
        if request.method == 'GET':
            form.country.choices = [(country.id, country.maa) for country in MapCountry.query.order_by(MapCountry.maa.asc())]
            form.town.choices = [(town.id, town.paikkakunta) for town in MapTown.query.filter_by(maa_id=1).order_by(MapTown.paikkakunta.asc())]
            form.tyyppi.choices = [(tyyppi.id, tyyppi.name) for tyyppi in MapType.query.order_by(MapType.name.asc())]
            return render_template("spots/new_spot.html", form=form, key=key)
        if request.method == 'POST':
            spot = MapSpot(maa_id = request.form.get('country'),
                    paikkakunta_id = request.form.get('town'),
                    tyyppi = request.form.get('tyyppi'),
                    nimi = request.form.get('name'),
                    info = request.form.get('description'),
                    karttalinkki = request.form.get('link'),
                    latlon = request.form.get('latlon'),
                    temp = 0,
                    paivays = datetime.now(),
                    user_id = session['user_id']
                )

            db.session.add(spot)
            db.session.commit()
            flash("New spot created succesfully")
            return redirect(url_for("spots.all"))
    else:
        flash("Please login first")
        return redirect(url_for("home"))

@mod_spots.route("/town/<country>")
def town(country):
    towns = MapTown.query.filter_by(maa_id=country).all()
    townArray = []
    for town in towns:
        townObj = {}
        townObj['id'] = town.id
        townObj['paikkakunta'] = town.paikkakunta
        townArray.append(townObj)
    return jsonify({'towns' : townArray})

@mod_spots.route("/update/<spot_id>", methods = ['POST', 'GET'])
def update_spot(spot_id):
    if(session and session['logged_in'] and session['user_level'] == 1):
        form = UpdateSpotForm()
        if request.method == 'GET':
            form.country.choices = [(country.id, country.maa) for country in MapCountry.query.order_by(MapCountry.maa.asc())]
            form.town.choices = [(town.id, town.paikkakunta) for town in MapTown.query.filter_by(maa_id=MapCountry.id).order_by(MapTown.paikkakunta.asc())]
            form.tyyppi.choices = [(tyyppi.id, tyyppi.name) for tyyppi in MapType.query.order_by(MapType.name.asc())]
            spot = MapSpot.query.filter_by(kartta_id=spot_id).first()
            form.country.default = spot.maa_id
            form.town.default = spot.paikkakunta_id
            form.tyyppi.default = spot.tyyppi
            form.name.default = spot.nimi
            form.description.default = spot.info
            form.temp.default = spot.temp
            form.link.default = spot.karttalinkki
            form.latlon.default = spot.latlon
            form.process()
            return render_template("spots/update_spot.html", form=form, spot=spot, key=key)
        if request.method == 'POST':

            spot = {
                    'maa_id': request.form.get('country'),
                    'paikkakunta_id': request.form.get('town'),
                    'tyyppi': request.form.get('tyyppi'),
                    'nimi': request.form.get('name'),
                    'info': request.form.get('description'),
                    'temp': 0,
                    'karttalinkki': request.form.get('link'),
                    'latlon': request.form.get('latlon'),
                    }

            MapSpot.query.filter_by(kartta_id=spot_id).update(spot)
            db.session.commit()

            flash("Updated spot with ID " + str(spot_id))
            return redirect(url_for("spots.all"))
    else:
        flash("Please login first")
        return redirect(url_for("home"))

@mod_spots.route("/delete", methods = ['POST', 'GET'])
def delete_spot():
    if(session and session['logged_in'] and session['user_level'] == 1):
        if request.method == 'POST':
            spot_id = request.form.get('spot_id')
            MapSpot.query.filter_by(kartta_id=spot_id).delete()
            db.session.commit()
            flash("Spot " + spot_id + " was deleted succesfully by " + session['username'] + ".")
            return redirect(url_for("spots.all"))
    else:
        flash("Please login first")
        return redirect(url_for("home"))

@mod_spots.route('/countries')
def countries():
    if(session and session['logged_in']):
        countries = MapCountry.query.order_by(MapCountry.maa.asc())
        return render_template("spots/countries.html", countries=countries)
    else:
        flash("Please login first")
        return redirect(url_for("home"))

@mod_spots.route('/towns')
def towns():
    if(session and session['logged_in']):
        towns = MapTown.query.order_by(MapTown.paikkakunta.asc())
        return render_template("spots/towns.html", towns=towns)
    else:
        flash("Please login first")
        return redirect(url_for("home"))

@mod_spots.route('/types')
def types():
    if(session and session['logged_in']):
        types = MapType.query.order_by(MapType.name.asc())
        return render_template("spots/types.html", types=types)
    else:
        flash("Please login first")
        return redirect(url_for("home"))

@mod_spots.route("/country/new", methods = ['POST', 'GET'])
def new_country():
    if(session and session['logged_in']):
        form = CountryForm()
        if request.method == 'GET':
            return render_template("spots/new_country.html", form=form, key=key)
        if request.method == 'POST':
            country = MapCountry(id = request.form.get('id'),
                    maa = request.form.get('maa'),
                    lat = request.form.get('lat'),
                    lon = request.form.get('lon'),
                    koodi = request.form.get('koodi')
                )
            db.session.add(country)
            db.session.commit()
            flash("New country created succesfully")
            return redirect(url_for("spots.countries"))
    else:
        flash("Please login first")
        return redirect(url_for("home"))

@mod_spots.route("/country/update/<country_id>", methods = ['POST', 'GET'])
def update_country(country_id):
    if(session and session['logged_in'] and session['user_level'] == 1):
        if request.method == 'GET':
            country = MapCountry.query.filter_by(id=country_id).first()
            return render_template("spots/update_country.html", country=country, key=key)
        if request.method == 'POST':
            country = { 
                    'maa': request.form.get('maa'),
                    'lat': request.form.get('lat'),
                    'lon': request.form.get('lon'),
                    'koodi': request.form.get('koodi')
                }
            MapCountry.query.filter_by(id=country_id).update(country)
            db.session.commit()
            flash("Country " + str(country_id) + " was edited succesfully by " + session['username'] + ".")
            return redirect(url_for("spots.countries"))
    else:
        flash("Please login first")
        return redirect(url_for("home"))

@mod_spots.route("/country/delete", methods = ['POST'])
def delete_country():
    if(session and session['logged_in'] and session['user_level'] == 1):
        if request.method == 'POST':
            country_id = request.form.get('country_id')
            MapCountry.query.filter_by(id=country_id).delete()
            db.session.commit()
            flash("Country " + country_id + " was deleted succesfully by " + session['username'] + ".")
            return redirect(url_for("spots.countries"))
    else:
        flash("Please login first")
        return redirect(url_for("home"))

@mod_spots.route("/town/new", methods = ['POST', 'GET'])
def new_town():
    if(session and session['logged_in']):
        form = TownForm()
        if request.method == 'GET':
            form.maa_id.choices = [(country.id, country.maa) for country in MapCountry.query.order_by(MapCountry.maa.asc())]
            return render_template("spots/new_town.html", form=form, key=key)
        if request.method == 'POST':
            town = MapTown(id = request.form.get('id'),
                    paikkakunta = request.form.get('paikkakunta'),
                    maa_id = request.form.get('maa_id'),
                    lat = request.form.get('lat'),
                    lon = request.form.get('lon')
                )
            db.session.add(town)
            db.session.commit()
            flash("New town created succesfully")
            return redirect(url_for("spots.towns"))
    else:
        flash("Please login first")
        return redirect(url_for("home"))

@mod_spots.route("/town/update/<town_id>", methods = ['POST', 'GET'])
def update_town(town_id):
    if(session and session['logged_in'] and session['user_level'] == 1):
        if request.method == 'GET':
            town = MapTown.query.filter_by(id=town_id).first()
            return render_template("spots/update_town.html", town=town, key=key)
        if request.method == 'POST':
            town = { 
                    'paikkakunta': request.form.get('paikkakunta'),
                    'maa_id': request.form.get('maa_id'),
                    'lat': request.form.get('lat'),
                    'lon': request.form.get('lon')
                }
            MapTown.query.filter_by(id=town_id).update(town)
            db.session.commit()
            flash("Town " + str(town_id) + " was edited succesfully by " + session['username'] + ".")
            return redirect(url_for("spots.towns"))
    else:
        flash("Please login first")
        return redirect(url_for("home"))

@mod_spots.route("/town/delete", methods = ['POST'])
def delete_town():
    if(session and session['logged_in'] and session['user_level'] == 1):
        if request.method == 'POST':
            id = request.form.get('id')
            MapTown.query.filter_by(id=id).delete()
            db.session.commit()
            flash("Town " + id + " was deleted succesfully by " + session['username'] + ".")
            return redirect(url_for("spots.towns"))
    else:
        flash("Please login first")
        return redirect(url_for("home"))

@mod_spots.route("/type/new", methods = ['POST', 'GET'])
def new_type():
    if(session and session['logged_in']):
        form = NewTypeForm()
        if request.method == 'GET':
            return render_template("spots/new_type.html", form=form)
        if request.method == 'POST':
            maptype = MapType(id = request.form.get('id'),
                    name = request.form.get('name')
                )
            db.session.add(maptype)
            db.session.commit()
            flash("New type created succesfully")
            return redirect(url_for("spots.types"))
    else:
        flash("Please login first")
        return redirect(url_for("home"))

@mod_spots.route("/type/delete", methods = ['POST'])
def delete_type():
    if(session and session['logged_in'] and session['user_level'] == 1):
        if request.method == 'POST':
            id = request.form.get('id')
            MapType.query.filter_by(id=id).delete()
            db.session.commit()
            flash("Town " + id + " was deleted succesfully by " + session['username'] + ".")
            return redirect(url_for("spots.types"))
    else:
        flash("Please login first")
        return redirect(url_for("home"))

@mod_spots.route("/latest")
def latest():
    if(session and session['logged_in'] and session['user_level'] == 1):
        spots = db.session.query(
            MapSpot
        ).filter(
            MapSpot.paivays >= '2020-01-01'
        ).join(
            User, MapSpot.user_id == User.user_id
        ).join(
            MapCountry, MapSpot.maa_id == MapCountry.id
        ).join(
            MapTown, MapSpot.paikkakunta_id == MapTown.id
        ).join(
            MapType, MapSpot.tyyppi == MapType.id
        ).add_columns(
            (User.username).label("username"),
            (MapSpot.kartta_id).label("kartta_id"),
            (MapSpot.nimi).label("name"),
            (MapSpot.user_id).label("user_id"),
            (MapCountry.maa).label("maa"),
            (MapTown.paikkakunta).label("paikkakunta"),
            (MapType.name).label("type"),
            (MapSpot.info).label("info"),
            (MapSpot.paivays).label("paivays"),
            (MapSpot.karttalinkki).label("link"),
            (MapSpot.temp).label("temp"),
            (MapSpot.latlon).label("latlon"),
        ).order_by(
            MapSpot.paivays.desc()
        )

        return render_template("spots/latest_spots.html", spots=spots)
    else:
        flash("Please login first")
    return redirect(url_for("home"))
