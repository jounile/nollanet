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
