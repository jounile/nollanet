import datetime
from flask import Flask, request, flash, g, render_template, jsonify, session, redirect, url_for, escape
import requests, json
from flask_paginate import Pagination, get_page_args

from . import app, db, utils, auto

@app.route('/documentation')
def get_documentation():
	return auto.html()

@app.route('/stories')
def stories():
    interviews = requests.get(url=request.url_root + "api/stories/interviews").json()
    news = requests.get(url=request.url_root + "api/stories/news").json()
    reviews = requests.get(url=request.url_root + "api/stories/reviews").json()
    return render_template("views/stories.html", 
                                interviews=interviews,
                                news=news,
                                reviews=reviews)

@app.route('/interviews')
def interviews():
    interviews = requests.get(url=request.url_root + "api/stories/interviews").json()
    return render_template("views/interviews.html", interviews=interviews)

@app.route('/news')
def news():
    news = requests.get(url=request.url_root + "api/stories/news").json()
    return render_template("views/news.html", news=news)

@app.route('/reviews')
def reviews():
    reviews = requests.get(url=request.url_root + "api/stories/reviews").json()
    return render_template("views/reviews.html", reviews=reviews)

@app.route('/general')
def general():
    general = requests.get(url=request.url_root + "api/stories/general").json()
    return render_template("views/general.html", general=general)

@app.route('/other')
def other():
    other = requests.get(url=request.url_root + "api/stories/other").json()
    return render_template("views/other.html", other=other)

@app.route('/')
def home():
    interviews = requests.get(url=request.url_root + "api/stories/interviews?newest=10").json()
    news = requests.get(url=request.url_root + "api/stories/news?newest=10").json()
    reviews = requests.get(url=request.url_root + "api/stories/reviews?newest=10").json()
    general = requests.get(url=request.url_root + "api/stories/general?newest=10").json()
    other = requests.get(url=request.url_root + "api/stories/other?newest=10").json()
    photos_skateboarding = requests.get(url=request.url_root + "api/photos/skateboarding").json()
    photos_snowboarding = requests.get(url=request.url_root + "api/photos/snowboarding").json()
    photos_nollagang = requests.get(url=request.url_root + "api/photos/nollagang").json()
    photos_snowskate = requests.get(url=request.url_root + "api/photos/snowskate").json()    
    return render_template('index.html', 
        interviews=interviews, 
        news=news, 
        reviews=reviews,
        general=general,
        other=other,
        photos_skateboarding=photos_skateboarding,
        photos_snowboarding=photos_snowboarding,
        photos_nollagang=photos_nollagang,
        photos_snowskate=photos_snowskate)

@app.route('/guides')
def guides():
    guides = requests.get(url=request.url_root + "api/guides").json()
    return render_template("views/guides.html", guides=guides)

@app.route("/support")
def support():
    return render_template("views/support.html")

@app.route("/about")
def about():
    return render_template("views/about.html")

@app.route('/user/<user_id>/')
def view_user(user_id):
    user = requests.get(url=request.url_root + "api/user/" + user_id).json()
    return render_template('views/user.html', user=user)   

@app.route('/guide/<guide_id>/')
def view_guide(guide_id):
    guide = requests.get(url=request.url_root + "api/guide/" + guide_id).json()
    print(guide)
    return render_template('views/guide.html', guide=guide)

@app.route('/interview/<interview_id>/')
def view_interviews_item(interview_id):
    interview = requests.get(url=request.url_root + "api/story/" + interview_id).json()
    return render_template('views/interview.html', interview=interview)

@app.route('/news/<news_id>/')
def view_news_item(news_id):
    news_item = requests.get(url=request.url_root + "api/story/" + news_id).json()
    return render_template('views/news_item.html', news_item=news_item)

@app.route('/general/<general_id>/')
def view_general_item(general_id):
    general_item = requests.get(url=request.url_root + "api/story/" + general_id).json()
    return render_template('views/general.html', general_item=general_item)

@app.route('/reviews/<review_id>/')
def view_reviews_item(review_id):
    reviews_item = requests.get(url=request.url_root + "api/story/" + review_id).json()
    return render_template('views/review.html', reviews_item=reviews_item)

@app.route('/other/<other_id>/')
def view_other_item(other_id):
    other_item = requests.get(url=request.url_root + "api/story/" + other_id).json()
    return render_template('views/other.html', other_item=other_item)

@app.route('/videos/')
def view_videos():
    videos = requests.get(url=request.url_root + "api/videos").json()
    return render_template('views/videos.html', videos=videos)



@app.route('/video/<string:media_id>')
def view_video(media_id):
    video = requests.get(url=request.url_root + "api/video/" + media_id).json()
    return render_template('views/video.html', video=video)

@app.route('/youtube/')
def youtube():
    return redirect('playlists')

@app.route('/photos/')
def view_photos_default():
    return redirect('skateboarding')

@app.route('/photos/<string:genre>/')
def view_photos_by_genre(genre):
    media_genre = utils.get_media_genre_id(genre)
    total = utils.get_total_photos_count_by_genre(media_genre)

    page, per_page, offset = utils.get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')

    photos = requests.get(url=request.url_root + "api/photos/" + genre + "/?page=" + str(page)).json()

    pagination = utils.get_pagination(page=page,
                                per_page=per_page,
                                total=total,
                                record_name=' photos',
                                format_total=True,
                                format_number=True,
                                )
                                              
    return render_template('views/photos.html', photos=photos, pagination=pagination)

@app.route('/videos/<string:genre>/')
def view_videos_by_genre(genre):
    media_genre = utils.get_media_genre_id(genre)
    total = utils.get_total_videos_count_by_genre(media_genre)

    page, per_page, offset = utils.get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')

    videos = requests.get(url=request.url_root + "api/videos/" + genre + "/?page=" + str(page)).json()

    pagination = utils.get_pagination(page=page,
                                per_page=per_page,
                                total=total,
                                record_name=' videos',
                                format_total=True,
                                format_number=True,
                                )
                                              
    return render_template('views/videos.html', videos=videos, pagination=pagination)

@app.route('/photo/<media_id>')
def view_photo(media_id):
    result = requests.get(url=request.url_root + "api/photo/" + media_id).json()
    item = result[0]
    photo = {
        'media_id': item['media_id'],
        'media_topic': item['media_topic'],
        'media_text': item['media_text'],
        'media_desc': item['media_desc'],
        'owner': item['owner'],
        'create_time': utils.convertDateTime(item['create_time'])
    }

    # Get comments
    comments = requests.get(url=request.url_root + "api/comments/"+ media_id).json()
    return render_template('views/photo.html', photo=photo, comments=comments)


@app.route("/media/update/<media_id>", methods = ['POST', 'GET'])
@auto.doc()
def update_media_without_file(media_id):
    if request.method == 'POST':
        media_type = request.form.get('media_type')
        media_genre = request.form.get('media_genre')
        story_type = request.form.get('story_type')
        media_topic = request.form.get('media_topic')
        media_text = request.form.get('media_text')
        media_desc = request.form.get('media_desc')
        owner = 'owner'
        create_time = get_now()
        lang_id = 2
        owner = "owner"

        sql = "UPDATE media_table SET media_type=%s, media_genre=%s, story_type=%s, media_topic=%s, media_text=%s, media_desc=%s, owner=%s, create_time=%s, lang_id=%s WHERE media_id=%s AND owner=%s"
        cursor = db.connection.cursor()
        cursor.execute(sql, (media_type, media_genre, story_type, media_topic, media_text, media_desc, owner, create_time, lang_id, media_id, owner))
        if(media_type == "1"):
            return redirect(url_for("view_photo", media_id=media_id)) 
        elif(media_type == "2"):
            return redirect(url_for("view_video", media_id=media_id))
        else:
            return redirect(url_for("home"))
    else:
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM media_table WHERE media_id=%s", (media_id, ))
        result = cursor.fetchone()
        return render_template("views/update_media.html", result=result)

@app.route("/media/insert", methods = ['POST', 'GET'])
@auto.doc()
def insert_media_without_file():
    if request.method == 'POST':
        media_type = request.form.get('media_type')
        media_genre = request.form.get('media_genre')
        story_type = request.form.get('story_type')
        media_topic = request.form.get('media_topic')
        media_text = request.form.get('media_text')
        media_desc = request.form.get('media_desc')
        owner = 'owner'
        create_time = get_now()
        lang_id = 2
        
        sql = "INSERT INTO media_table (media_type, media_genre, story_type, media_topic, media_text, media_desc, owner, create_time, lang_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor = db.connection.cursor()
        cursor.execute(sql, (media_type, media_genre, story_type, media_topic, media_text, media_desc, owner, create_time, lang_id))
        media_id = cursor.lastrowid
        if(media_type == "1"):
            return redirect(url_for("view_photo", media_id=media_id)) 
        elif(media_type == "2"):
            return redirect(url_for("view_video", media_id=media_id))
        else:
            return redirect(url_for("home"))
    else:
        return render_template("views/add_media.html")
