import pytest
from requests import get
from urllib.parse import urljoin

def test_new_story_page(wait_for_api, login_user):
    """
    GIVEN a user has logged in (login_user)
    WHEN the '/stories/newstory' page is navigated to (GET)
    THEN check the response is valid and page title is correct
    """
    request_session, api_url = wait_for_api
    response = request_session.get(urljoin(api_url, '/stories/newstory'))
    assert response.status_code == 200
    assert '<h1>New story</h1>' in response.text

def test_update_story_page(wait_for_api, login_user):
    """
    GIVEN a user has logged in (login_user)
    WHEN the '/stories/update/1' page is navigated to (GET)
    THEN check the response is valid and page title is correct
    """
    request_session, api_url = wait_for_api
    response = request_session.get(urljoin(api_url, '/stories/update/1'))
    assert response.status_code == 200
    assert '<h1>Update story</h1>' in response.text

def test_hidden_story_news(wait_for_api, login_user):
    """
    GIVEN a user has logged in (login_user)
    WHEN the '/stories/newstory' is submitted to creat a story (POST)
    THEN check the response is valid and flash message is correct
    """
    new_hidden_story_news = dict(genre_id=1, storytype_id=2, country_id=1, media_topic='New review topic', media_desc='description', media_text='Text content', hidden=1)
    request_session, api_url = wait_for_api
    response = request_session.post(urljoin(api_url, '/stories/newstory'), data=new_hidden_story_news, allow_redirects=True)
    assert response.status_code == 200
    assert '<div class="flash">New story created</div>' in response.text

def test_valid_story_news(wait_for_api, login_user):
    """
    GIVEN a user has logged in (login_user)
    WHEN the '/stories/newstory' is submitted to creat a story (POST)
    THEN check the response is valid and flash message is correct
    """
    new_story_news = dict(genre_id=1, storytype_id=4, country_id=1, media_topic='New news topic', media_desc='Description', media_text='Text content', hidden=None)
    request_session, api_url = wait_for_api
    response = request_session.post(urljoin(api_url, '/stories/newstory'), data=new_story_news, allow_redirects=True)
    assert response.status_code == 200
    assert '<div class="flash">New story created</div>' in response.text

def test_valid_story_interview(wait_for_api, login_user):
    """
    GIVEN a user has logged in (login_user)
    WHEN the '/stories/newstory' is submitted to creat a story (POST)
    THEN check the response is valid and flash message is correct
    """
    new_story_interview = dict(genre_id=1, storytype_id=3, country_id=1, media_topic='New interview topic', media_desc='Description', media_text='Text content', hidden=None)
    request_session, api_url = wait_for_api
    response = request_session.post(urljoin(api_url, '/stories/newstory'), data=new_story_interview, allow_redirects=True)
    assert response.status_code == 200
    assert '<div class="flash">New story created</div>' in response.text

def test_valid_story_review(wait_for_api, login_user):
    """
    GIVEN a user has logged in (login_user)
    WHEN the '/stories/newstory' is submitted to creat a story (POST)
    THEN check the response is valid and flash message is correct
    """
    new_story_review = dict(genre_id=1, storytype_id=2, country_id=1, media_topic='New review topic', media_desc='description', media_text='Text content', hidden=None)
    request_session, api_url = wait_for_api
    response = request_session.post(urljoin(api_url, '/stories/newstory'), data=new_story_review, allow_redirects=True)
    assert response.status_code == 200
    assert '<div class="flash">New story created</div>' in response.text


