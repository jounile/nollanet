import pytest
from requests import get
from urllib.parse import urljoin

def test_new_spot_page(wait_for_api, login_user):
    """
    GIVEN a user has logged in (login_user)
    WHEN the '/spots/spot/new' page is navigated to (GET)
    THEN check the response is valid and page title is correct
    """
    request_session, api_url = wait_for_api
    response = request_session.get(urljoin(api_url, '/spots/spot/new'))
    assert response.status_code == 200
    assert '<h1>New spot</h1>' in response.text


