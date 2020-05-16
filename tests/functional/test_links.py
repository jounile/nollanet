import pytest
from requests import get
from urllib.parse import urljoin

def test_valid_new_link_page(wait_for_api, login_user):
    """
    GIVEN a user has logged in (login_user)
    WHEN the '/links/new' page is navigated to (GET)
    THEN check the response is valid and page title is correct
    """
    request_session, api_url = wait_for_api
    response = request_session.get(urljoin(api_url, '/links/new'))
    assert response.status_code == 200
    assert '<h1>New link</h1>' in response.text

def test_invalid_new_link_page(wait_for_api):
    """
    GIVEN a user has not logged in
    WHEN the '/links/new' page is navigated to (GET)
    THEN check the response is valid and page title is correct
    """
    request_session, api_url = wait_for_api
    response = request_session.get(urljoin(api_url, '/links/new'))
    assert response.status_code == 200
    assert '<div class="flash">Please login first</div>' in response.text

def test_valid_link_categories_page(wait_for_api, login_user):
    """
    GIVEN a user has logged in (login_user)
    WHEN the '/links/categories' page is navigated to (GET)
    THEN check the response is valid and page title is correct
    """
    request_session, api_url = wait_for_api
    response = request_session.get(urljoin(api_url, '/links/categories'))
    assert response.status_code == 200
    assert '<h1>Link categories</h1>' in response.text

def test_invalid_link_categories_page(wait_for_api):
    """
    GIVEN a user has not logged in
    WHEN the '/links/categories' page is navigated to (GET)
    THEN check user is redirected to homepage because not authorized and flash message is correct
    """
    request_session, api_url = wait_for_api
    response = request_session.get(urljoin(api_url, '/links/categories'))
    assert response.status_code == 200
    assert '<div class="flash">Please login first</div>' in response.text

def test_valid_new_link_category_page(wait_for_api, login_user):
    """
    GIVEN a user has logged in (login_user)
    WHEN the '/links/category/new' page is navigated to (GET)
    THEN check check the response is valid and page title is correct
    """
    request_session, api_url = wait_for_api
    response = request_session.get(urljoin(api_url, '/links/category/new'))
    assert response.status_code == 200
    assert '<h1>New link category</h1>' in response.text

def test_invalid_new_link_category_page(wait_for_api):
    """
    GIVEN a user has not logged
    WHEN the '/links/category/new' page is navigated to (GET)
    THEN check check the response is valid and page title is correct
    """
    request_session, api_url = wait_for_api
    response = request_session.get(urljoin(api_url, '/links/category/new'))
    assert response.status_code == 200
    assert '<div class="flash">Please login first</div>' in response.text

def test_valid_new_link(wait_for_api, login_user):
    """
    GIVEN a user has logged in
    WHEN the '/links/new' page is navigated to (POST)
    THEN check check the response is valid and flash message is correct
    """
    new_link = dict(category=1, name='Test link', url='http://www.example.com')
    request_session, api_url = wait_for_api
    response = request_session.post(urljoin(api_url, '/links/new'), data=new_link, allow_redirects=True)
    assert response.status_code == 200
    assert '<div class="flash">New link created</div>' in response.text

def test_valid_new_link_category(wait_for_api, login_user):
    """
    GIVEN a user has logged in
    WHEN the '/links/category/new' page is navigated to (POST)
    THEN check check the response is valid and flash message is correct
    """
    new_category = dict(category_name='Test category')
    request_session, api_url = wait_for_api
    response = request_session.post(urljoin(api_url, '/links/category/new'), data=new_category, allow_redirects=True)
    assert response.status_code == 200
    assert '<div class="flash">New link category created</div>' in response.text
