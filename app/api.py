import os
from flask import Flask, request, flash, g, render_template, jsonify, session, redirect, url_for, escape
import requests, json
from urlparse import urljoin # Python 2.7
from werkzeug.utils import secure_filename

from . import app, db, utils, auto

@app.route('/media/<path:filename>', methods=['GET'])
def media(filename):
    static_url = app.config.get('AZURE_BLOB')
    if static_url:
        return redirect(urljoin(static_url, filename))
    return app.send_static_file(filename)

@app.route('/api/comments/<int:media_id>')
def api_comments(media_id):
    cursor = db.connection.cursor()
    cursor.execute("SELECT k.user_id, u.username, k.header, k.comment, k.timestamp, k.media_id, k.comment_user_id, k.youtube_id, k.tapahtuma_id, k.diary_id FROM kommentti k, users u WHERE k.user_id = u.user_id AND media_id = %s ORDER BY k.id desc LIMIT 0, 100", (media_id, ))
    result = cursor.fetchall()
    return utils.query_result_to_json(cursor, result)


""" User """

@app.route('/media/upload', methods=['POST'])
def upload_file():
	if request.method == 'POST':
        # check if the post request has the files part
		if 'files[]' not in request.files:
			flash('No file part')
			return redirect(request.url)
		files = request.files.getlist('files[]')
		for file in files:
			if file and utils.allowed_file(file.filename):
				filename = secure_filename(file.filename)
				file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		flash('File(s) successfully uploaded')
		return redirect('/')
