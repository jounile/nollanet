from requests import get
from urllib.parse import urljoin

def test_register_page(wait_for_api):
    request_session, api_url = wait_for_api
    response = request_session.get(urljoin(api_url, '/auth/register'))
    assert response.status_code == 200
    assert "<h2>Register</h2>" in response.text

def test_valid_registration(wait_for_api):
    """
    GIVEN a Flask application
    WHEN the '/auth/register' page is posted to (POST)
    THEN check the response is valid and the user is logged in
    """
    request_session, api_url = wait_for_api
    response = request_session.post(urljoin(api_url, '/auth/register'),
                                    data=dict(name='Pat Kennedy',
                                        username='patkennedy79',
                                        password='secretpassword',
                                        email='patkennedy79@yahoo.com',
                                        bornyear='1979',
                                        location='asdf',
                                        address='asdf',
                                        postnumber='20200')
                                    )
    assert response.status_code == 200