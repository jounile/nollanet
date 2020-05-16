import uuid
from requests import get
from urllib.parse import urljoin


def test_register_page(wait_for_api):
    """
    GIVEN a running site container
    WHEN the '/auth/register' page is navigated to (GET)
    THEN check the response is valid and page title is correct
    """
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
    random = uuid.uuid4()
    random_username = str(random)[:8]
    valid_user = dict(name='Test User',
                    username=random_username,
                    password='secretpassword',
                    email='testuser@example.com',
                    bornyear='1979',
                    gender=1,
                    location='test location',
                    address='test address',
                    postnumber='20200')

    request_session, api_url = wait_for_api
    response = request_session.post(urljoin(api_url, '/auth/register'), data=valid_user, allow_redirects=True)
    assert response.status_code == 200
    assert "User " + str(random_username) + " has been registered." in response.text

def test_missing_name(wait_for_api):
    """
    GIVEN a running site container
    WHEN the '/auth/register' page is posted a empty user (POST)
    THEN check the response is valid, there is error message and the new user is not registered
    """
    invalid_user = dict(name='',
                    username='testuser',
                    password='secretpassword',
                    email='testuser@example.com',
                    bornyear='1979',
                    gender=1,
                    location='test location',
                    address='test address',
                    postnumber='20200')

    request_session, api_url = wait_for_api
    response = request_session.post(urljoin(api_url, '/auth/register'), data=invalid_user, allow_redirects=True)
    assert response.status_code == 200
    assert '<div class="flash">Registration failed</div>' in response.text
    assert 'Name is required' in response.text

def test_missing_username(wait_for_api):
    """
    GIVEN a running site container
    WHEN the '/auth/register' page is posted a empty user (POST)
    THEN check the response is valid, there is error message and the new user is not registered
    """
    invalid_user = dict(name='Test User',
                    username='',
                    password='secretpassword',
                    email='testuser@example.com',
                    bornyear='1979',
                    gender=1,
                    location='test location',
                    address='test address',
                    postnumber='20200')

    request_session, api_url = wait_for_api
    response = request_session.post(urljoin(api_url, '/auth/register'), data=invalid_user, allow_redirects=True)
    assert response.status_code == 200
    assert '<div class="flash">Registration failed</div>' in response.text
    assert 'Username is required' in response.text

def test_missing_password(wait_for_api):
    """
    GIVEN a running site container
    WHEN the '/auth/register' page is posted a empty user (POST)
    THEN check the response is valid, there is error message and the new user is not registered
    """
    invalid_user = dict(name='Test User',
                    username='testuser',
                    password='',
                    email='testuser@example.com',
                    bornyear='1979',
                    gender=1,
                    location='test location',
                    address='test address',
                    postnumber='20200')

    request_session, api_url = wait_for_api
    response = request_session.post(urljoin(api_url, '/auth/register'), data=invalid_user, allow_redirects=True)
    assert response.status_code == 200
    assert '<div class="flash">Registration failed</div>' in response.text
    assert 'Password is required' in response.text

def test_missing_email(wait_for_api):
    """
    GIVEN a running site container
    WHEN the '/auth/register' page is posted a empty user (POST)
    THEN check the response is valid, there is error message and the new user is not registered
    """
    invalid_user = dict(name='Test User',
                    username='testuser',
                    password='secretpassword',
                    email='',
                    bornyear='1979',
                    gender=1,
                    location='test location',
                    address='test address',
                    postnumber='20200')

    request_session, api_url = wait_for_api
    response = request_session.post(urljoin(api_url, '/auth/register'), data=invalid_user, allow_redirects=True)
    assert response.status_code == 200
    assert '<div class="flash">Registration failed</div>' in response.text
    assert 'Email is required' in response.text

def test_invalid_email(wait_for_api):
    """
    GIVEN a running site container
    WHEN the '/auth/register' page is posted a empty user (POST)
    THEN check the response is valid, there is error message and the new user is not registered
    """
    invalid_user = dict(name='Test User',
                    username='testuser',
                    password='secretpassword',
                    email='notanemail',
                    bornyear='1979',
                    gender=1,
                    location='test location',
                    address='test address',
                    postnumber='20200')

    request_session, api_url = wait_for_api
    response = request_session.post(urljoin(api_url, '/auth/register'), data=invalid_user, allow_redirects=True)
    assert response.status_code == 200
    assert '<div class="flash">Registration failed</div>' in response.text
    assert 'Invalid E-mail Address' in response.text


def test_missing_bornyear(wait_for_api):
    """
    GIVEN a running site container
    WHEN the '/auth/register' page is posted a empty user (POST)
    THEN check the response is valid, there is error message and the new user is not registered
    """
    invalid_user = dict(name='Test User',
                    username='testuser',
                    password='secretpassword',
                    email='testuser@example.com',
                    bornyear='',
                    gender=1,
                    location='test location',
                    address='test address',
                    postnumber='20200')

    request_session, api_url = wait_for_api
    response = request_session.post(urljoin(api_url, '/auth/register'), data=invalid_user, allow_redirects=True)
    assert response.status_code == 200
    assert '<div class="flash">Registration failed</div>' in response.text
    assert 'Year is required' in response.text

def test_missing_postnumber(wait_for_api):
    """
    GIVEN a running site container
    WHEN the '/auth/register' page is posted a empty user (POST)
    THEN check the response is valid, there is error message and the new user is not registered
    """
    invalid_user = dict(name='Test User',
                    username='testuser',
                    password='secretpassword',
                    email='testuser@example.com',
                    bornyear='1979',
                    gender=1,
                    location='test location',
                    address='test address',
                    postnumber='')

    request_session, api_url = wait_for_api
    response = request_session.post(urljoin(api_url, '/auth/register'), data=invalid_user, allow_redirects=True)
    assert response.status_code == 200
    assert '<div class="flash">Registration failed</div>' in response.text
    assert 'Postnumber is required' in response.text