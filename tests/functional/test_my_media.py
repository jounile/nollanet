import pytest
from requests import get
from urllib.parse import urljoin

def test_my_media_page(wait_for_api, login_user):
    """
    GIVEN a user has logged in (login_user)
    WHEN the '/user/media' page is navigated to (GET)
    THEN check the response is valid and page title is correct
    """
    request_session, api_url = wait_for_api
    response = request_session.get(urljoin(api_url, '/user/media'))
    assert response.status_code == 200
    assert '<h1>My media</h1>' in response.text

