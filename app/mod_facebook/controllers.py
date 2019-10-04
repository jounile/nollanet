from flask import Blueprint, render_template
import facebook
import requests
import json
import os

from app import app

# Instance specific configurations
app.config.from_pyfile('config.py')

mod_facebook = Blueprint('facebook', __name__, url_prefix='/facebook')

@mod_facebook.route('/info')
def facebook_info():
	
	# Creating a permanent facebook page access token
	# https://github.com/DrGabrielA81/medium/tree/master/making-facebook-API-calls
	# 1 Generate Long-Lived Access Token
	# 2 Get User ID
	# 3 Get Permanent Page Access Token


	APP_ROOT = os.path.dirname(os.path.abspath(__file__))

	# open json file for reading
	with open(APP_ROOT + '/facebook.json', 'r') as f:
		data = json.load(f)

	# read user info
	user_short_token = data['user']['short_token']
	user_long_token = data['user']['long_token']

	# read app info
	app_id = data['app']['id']
	app_secret = data['app']['secret']

	# read page info
	page_token = data['page']['token']
	page_id = data['page']['id']

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
			#print("oauth_access_token", oauth_access_token)

			# update value
			data['user']['long_token'] = oauth_access_token

		# get first permanent page token
		graph = facebook.GraphAPI(access_token=oauth_access_token, version="2.10")
		pages_data = graph.get_object("/me/accounts")

		for item in pages_data['data']:
			if item['id'] == page_id:
				page_token = item['access_token']

		#print("page_token: ", page_token)

		# update value
		data['page']['token'] = page_token

	# use stored permanent page token to request a new one
	else:

		page_token = requests.get(
        "{}{}?grant_type=fb_exchange_token&client_id={}&client_secret={}&fb_exchange_token={}".format(
                host, endpoint, app_id, app_secret, page_token)).json()['access_token']

		# update value
		data['page']['token'] = page_token

		#print("refreshing page_token: ", page_token)

	# open json file for writing
	with open(APP_ROOT + '/facebook.json', 'w') as f:
		json.dump(data, f, indent=4)

	# Query page data
	graph = facebook.GraphAPI(access_token=page_token, version="2.10")
	infos = graph.get_object("/me?fields=id,name,about,description,posts{picture,message,permalink_url,created_time,is_published}")
	#print(infos)

	return render_template('facebook/facebook.html', infos=infos)