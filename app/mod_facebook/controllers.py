from flask import Blueprint, render_template
import facebook
import requests
import json
import os

from app import app, utils

mod_facebook = Blueprint('facebook', __name__, url_prefix='/facebook')

@mod_facebook.route('/info')
def facebook_info():
	
	# Creating a permanent facebook page access token
	# https://github.com/DrGabrielA81/medium/tree/master/making-facebook-API-calls
	# 1 Generate Long-Lived Access Token
	# 2 Get User ID
	# 3 Get Permanent Page Access Token

	# read user info
	user_short_token = app.config.get('USER_SHORT_TOKEN')
	user_long_token = app.config.get('USER_LONG_TOKEN')

	# read app info
	app_id = app.config.get('APP_ID')
	app_secret = app.config.get('APP_SECRET')

	# read page info
	page_token = app.config.get('PAGE_TOKEN')
	page_id = app.config.get('FACEBOOK_PAGE_ID')

	host = "https://graph.facebook.com"
	endpoint = "/oauth/access_token"

	oauth_access_token = ""

	# get first long-lived user token
	if user_long_token == 'None':
		params = {
			'client_id': app_id,
			'client_secret': app_secret,
			'grant_type': 'fb_exchange_token',
			'fb_exchange_token': user_short_token
		}
		r = requests.get("https://graph.facebook.com/oauth/access_token", params=params)
		if r.ok:
			oauth_access_token = r.json()['access_token']

			# update value
			app.config.update(USER_LONG_TOKEN=oauth_access_token)

		# get first permanent page token
		graph = facebook.GraphAPI(access_token=oauth_access_token, version="2.10")
		pages_data = graph.get_object("/me/accounts")

		for item in pages_data['data']:
			if item['id'] == page_id:
				page_token = item['access_token']

		# update value
		app.config.update(PAGE_TOKEN=page_token)

	# use stored permanent page token to request a new one
	else:

		page_token = requests.get(
        "{}{}?grant_type=fb_exchange_token&client_id={}&client_secret={}&fb_exchange_token={}".format(
                host, endpoint, app_id, app_secret, page_token)).json()['access_token']

		# update value
		app.config.update(PAGE_TOKEN=page_token)

	# Query page data
	graph = facebook.GraphAPI(access_token=page_token, version="2.10")
	infos = graph.get_object("/me?fields=id,name,about,description,posts{picture,message,permalink_url,created_time,is_published}")

	return render_template('facebook/facebook.html', infos=infos)