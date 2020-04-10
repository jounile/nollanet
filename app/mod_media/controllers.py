import datetime
from urllib.parse import urljoin # Python 3

from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify
from werkzeug import secure_filename

from app import app, db, utils
from app.models import Uploads, User, Comment, Media, Country, Genre, MediaType, StoryType

mod_media = Blueprint('media', __name__, url_prefix='/media')


@mod_media.route('/all')
def all():

    selected_media_genre = 1 # skateboarding by default
    if(request.args.get('media_genre')):
        selected_media_genre = request.args.get('media_genre')

    selected_media_type = 1 # photos by default
    if(request.args.get('media_type')):
        selected_media_type = request.args.get('media_type')

    total = utils.get_count_by_genre_and_type(selected_media_genre, selected_media_type)
    page, per_page, offset = utils.get_page_args(page_parameter='page', per_page_parameter='per_page')
    media = db.session.query(
            Media
        ).join(Country
        ).add_columns(
            Media.media_id,
            (Country.country_code).label("country_code"),
            Media.media_topic,
            Media.create_time,
            Media.owner
        ).filter(
            Media.media_type==selected_media_type
        ).filter(
            Media.media_genre==selected_media_genre
        ).filter(
            Media.hidden==0
        ).order_by(
            Media.create_time.desc()
        ).offset(
            offset
        ).limit(per_page)
    pagination = utils.get_pagination(page=page, per_page=per_page, total=total, record_name=' media', format_total=True, format_number=True,)                                 
    return render_template('media/media.html', media=media, pagination=pagination, selected_media_genre=selected_media_genre, selected_media_type=selected_media_type)

@mod_media.route('/photo/<media_id>')
def photo(media_id):
    photo = db.session.query(Media).join(Country).add_columns(Media.media_id,
        (Country.country_code).label("country_code"),
        Media.media_topic,
        Media.media_text,
        Media.create_time,
        Media.owner).filter(Media.media_id==media_id).first()
    comments = Comment.query.filter_by(media_id=media_id).filter(Comment.user_id == User.user_id).order_by(Comment.id.desc()).limit(100)
    return render_template('media/photo.html', photo=photo, comments=comments)

@mod_media.route('/video/<string:media_id>')
def video(media_id):
    video = Media.query.filter_by(media_id=media_id).first()
    return render_template('media/video.html', video=video)


@mod_media.route("/latest")
def latest():
    if(session and session['logged_in'] and session['user_level'] == 1):
        latest = db.session.query(
                Media
            ).join(Genre
            ).join(MediaType
            ).join(StoryType
            ).join(Country
            ).add_columns(
                Media.media_id,
                (Genre.type_name).label("genre"),
                (MediaType.type_name).label("mediatype_name"),
                (StoryType.type_name).label("storytype_name"),
                (Country.country_code).label("country_code"),
                Media.media_topic,
                Media.media_desc,
                Media.create_time,
                Media.owner,
                Media.hidden
            ).order_by(
                Media.create_time.desc()
            ).limit(10)
        return render_template("media/latest_media.html", latest=latest)
    else:
        flash("Please login first")
    return redirect(url_for("home"))

@mod_media.route('/delete', methods = ['POST'])
def delete():
    if(session and session['logged_in'] and session['user_level'] == 1):
        if request.method == 'POST':
            media_id = request.form.get('media_id')
            Media.query.filter_by(media_id=media_id).delete()
            db.session.commit()
            flash("Record " + media_id + " was deleted succesfully by " + session['username'] + ".")
    else:
        flash("Please login first")
    return redirect(url_for("home"))

@mod_media.route('/<path:filename>', methods=['GET'])
def filename(filename):
    static_url = app.config.get('AZURE_BLOB_URI')
    if static_url:
        return redirect(urljoin(static_url, filename))
    return app.send_static_file(filename)

@mod_media.route("/update/<media_id>", methods = ['POST', 'GET'])
def update(media_id):
    if request.method == 'POST':

        media = { 'media_id': request.form.get('media_id'),
                'media_genre': request.form.get('media_genre'),
                'media_type': request.form.get('media_type'),
                'story_type': request.form.get('story_type'),
                'media_topic': request.form.get('media_topic'),
                'media_text': request.form.get('media_text'),
                'media_desc': request.form.get('media_desc'),
                'country_id': request.form.get('country_id'),
                'hidden': request.form.get('hidden') }

        if(session and session['logged_in'] and session['user_level'] == 1):
            Media.query.filter_by(media_id=media_id).update(media)
            db.session.commit()
            flash("Record " + media_id + " was updated by user " + session['username'])
            return redirect(url_for("home"))
        else:
            flash("Please login first")
            return redirect(url_for("home"))
    else:
        if(session and session['logged_in'] and session['user_level'] == 1):
            result = Media.query.filter_by(media_id=media_id).first()
            return render_template("views/user/update_media.html", result=result)
        else:
            flash("Please login first")
            return redirect(url_for("home"))

@app.route("/newupload", methods=['POST','GET'])
def new_upload():
    if request.method == 'POST':

        # Crea a blob container with the users name
        blob_service = utils.get_azure_blob_service()
        container = ''
        file_to_upload = request.files['file']
        filename = secure_filename(file_to_upload.filename)

        if(session and session['logged_in']):
            container = session['username']
            if not blob_service.exists(container):
                blob_service.create_container(container)
                blob_service.set_container_acl(container, public_access=PublicAccess.Blob)
        else:
            flash("Please login first")
            return redirect(url_for("home"))

        # Create Blob from stream
        try:
            blob_service.create_blob_from_stream(container, filename, file_to_upload)
            flash("File " + filename + " was uploaded successfully")
        except:
            print("Something went wrong while uploading the files %s"%filename)
            flash("Something went wrong while uploading the files %s"%filename)
            pass

        blob = app.config.get('AZURE_BLOB_URI')
        path =  blob + '/' + container + '/' + filename

        # Create a record in database
        upload = Uploads(
            user_id=session['user_id'],
            create_time=datetime.datetime.now(),
            path=path)
        db.session.add(upload)
        db.session.commit()
        #print("Upload was inserted to database by user " + session['username'])

        return redirect(url_for("my_uploads"))
    return render_template("views/user/new_upload.html")
