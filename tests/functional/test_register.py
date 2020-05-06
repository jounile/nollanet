from requests import get
from urllib.parse import urljoin

def test_register_page(wait_for_api):
    request_session, api_url = wait_for_api
    response = request_session.get(urljoin(api_url, '/auth/register'))
    assert response.status_code == 200
    assert "<h2>Register</h2>" in response.text

def test_valid_registration(wait_for_api):
    """
    GIVEN a running site container
    WHEN the '/auth/register' page is posted a new user (POST)
    THEN check the response is valid and the new user is registered
    """
    valid_user = dict(name='Pat Kennedy',
                    username='patkennedy79',
                    password='secretpassword',
                    email='patkennedy79@yahoo.com',
                    bornyear='1979',
                    gender=1,
                    location='asdf',
                    address='asdf',
                    postnumber='20200',
                    recaptcha='')

    request_session, api_url = wait_for_api
    response = request_session.post(urljoin(api_url, '/auth/register'), data=valid_user, allow_redirects=True)

    assert response.status_code == 200
    assert "User patkennedy79 has been registered." in response.text

def test_invalid_registration(wait_for_api):
    """
    GIVEN a running site container
    WHEN the '/auth/register' page is posted a empty user (POST)
    THEN check the response is valid, there is error message and the new user is not registered
    """
    invalid_user = dict(name='',
                    username='',
                    password='',
                    email='',
                    bornyear='',
                    gender=0,
                    location='',
                    address='',
                    postnumber='',
                    recaptcha='')

    request_session, api_url = wait_for_api
    response = request_session.post(urljoin(api_url, '/auth/register'), data=invalid_user, allow_redirects=True)

    assert response.status_code == 200
    assert '<div class="flash">Registration failed</div>' in response.text