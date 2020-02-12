from flask import Blueprint, render_template
from apiclient.discovery import build 

from app import app

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# creating Youtube Resource Object
def youtube():
	return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey = app.config.get("GOOGLE_API_KEY"))

mod_youtube = Blueprint('youtube', __name__, url_prefix='/youtube')

@mod_youtube.route('/playlists')
def youtube_playlists():
	search = youtube().channels().list(
		part = "snippet,contentDetails,statistics",
        forUsername = "n0llanet",
		maxResults = 10).execute()
	results = search.get("items", [])
	
	for result in results:

		channelId = result['id']
		#print(channelId)

	playlists = get_youtube_playlists(channelId)

	return render_template('youtube/playlists.html', channelId=channelId, playlists=playlists)

def get_youtube_playlists(channel_id):
	search = youtube().playlists().list(
		part = "snippet,contentDetails",
		channelId = channel_id,
		maxResults = 25).execute()
	results = search.get("items", [])

	playlists = []
	
	for result in results:
		playlist_id = result['id']
		playlist_title = result['snippet']['title']
		playlist_thumbnail = result['snippet']['thumbnails']['default']['url']

		playlist = {
			'id': playlist_id,
			'title': playlist_title,
			'thumbnail': playlist_thumbnail
		}
		playlists.append(playlist)

	return playlists

@mod_youtube.route('/playlist/<playlist_id>')
def youtube_playlistItems(playlist_id):

	# Get playlist title
	playlist = youtube().playlists().list(part = "snippet,contentDetails",
        id = playlist_id
    ).execute()
	playlist_title = playlist['items'][0]['snippet']['title']

	# Get playlist items
	search = youtube().playlistItems().list(part = "snippet,contentDetails",
		maxResults = 25,
		playlistId = playlist_id).execute()
	results = search.get("items", [])
	
	playlistItems = []

	for result in results:
		
		playlistItem_id = result['snippet']['resourceId']['videoId']
		playlistItem_title = result['snippet']['title']

		playlistItem = {
			'id': playlistItem_id,
			'title': playlistItem_title
		}
		playlistItems.append(playlistItem)

	return render_template('youtube/playlist.html', playlist_title=playlist_title, playlistItems=playlistItems)


