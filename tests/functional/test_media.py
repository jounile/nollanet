import pytest
from requests import get
from urllib.parse import urljoin

def test_new_photo_page(wait_for_api, login_user):
    """
    GIVEN a user has logged in (login_user)
    WHEN the '/media/newphoto' page is navigated to (GET)
    THEN check the response is valid and page title is correct
    """
    request_session, api_url = wait_for_api
    response = request_session.get(urljoin(api_url, '/media/newphoto'))
    assert response.status_code == 200
    assert '<h1>New photo</h1>' in response.text

def test_hidden_photo(wait_for_api, login_user):
    """
    GIVEN a user has logged in (login_user)
    WHEN the '/media/newphoto' is submitted to creat a story (POST)
    THEN check the response is valid and flash message is correct
    """
    new_hidden_photo = dict(genre_id=1, storytype_id=2, country_id=1, media_topic='New topic', media_desc='description', media_text='Text content', hidden=1)
    request_session, api_url = wait_for_api
    response = request_session.post(urljoin(api_url, '/media/newphoto'), data=new_hidden_photo, allow_redirects=True)
    assert response.status_code == 200
    assert '<div class="flash">New photo added</div>' in response.text

def test_valid_photo(wait_for_api, login_user):
    """
    GIVEN a user has logged in (login_user)
    WHEN the '/media/newphoto' is submitted to creat a story (POST)
    THEN check the response is valid and flash message is correct
    """
    new_photo = dict(genre_id=1, storytype_id=4, country_id=1, media_topic='New photo topic', media_desc='Description', media_text='Text content', hidden=None)
    request_session, api_url = wait_for_api
    response = request_session.post(urljoin(api_url, '/media/newphoto'), data=new_photo, allow_redirects=True)
    assert response.status_code == 200
    assert '<div class="flash">New photo added</div>' in response.text
