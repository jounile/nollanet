from requests import get
from urllib.parse import urljoin

# Requires google API keys to work.
# Use testing configuration

def test_youtube_page(wait_for_api):
    request_session, api_url = wait_for_api
    response = request_session.get(urljoin(api_url, '/youtube/playlists'))
    assert response.status_code == 200
    assert "<h1>Playlists</h1>" in response.text
