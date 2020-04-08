from flask import Blueprint, render_template
from apiclient.discovery import build 
#import soundcloud

from app import app

#SOUNDCLOUD_CLIENT_ID = "2t9loNQH90kzJcsFCODdigxfp325aq4z" #TODO: update client_id 

mod_soundcloud = Blueprint('soundcloud', __name__, url_prefix='/soundcloud')

@mod_soundcloud.route('/playlists')
def soundcloud_playlists():

	#client = soundcloud.Client(client_id=SOUNDCLOUD_CLIENT_ID)
	#playlist = client.get('/playlists/2050462')
	#for track in playlist.tracks:
	#	print track['title']

	pods = []
	pod = {
		'id': "1",
		'title': "pod 1"
	}
	pods.append(pod)
	return render_template('soundcloud/playlists.html', pods=pods)