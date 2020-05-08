from requests import get
from urllib.parse import urljoin

def test_login_page(wait_for_api):
    """
    GIVEN a running site container
    WHEN the '/auth/login' page is navigated to (GET)
    THEN check the response is valid and the Login link is available
    """
    request_session, api_url = wait_for_api
    response = request_session.get(urljoin(api_url, '/auth/login'))
    assert response.status_code == 200
    assert "<h2>Login</h2>" in response.text
    assert '<a class="nav-link" href="/auth/login">Login</a>' in response.text

def test_valid_user_login(wait_for_api, login_user):
    pass

def test_valid_admin_login(wait_for_api, login_admin):
    pass

def test_invalid_user_login(wait_for_api):
    """
    GIVEN a running site container
    WHEN the '/auth/login' page is posted user credentials (POST)
    THEN check the response is valid and the user is logged in
    """
    invalid_user = dict(username='tester',
                    password='wrongpassword')

    request_session, api_url = wait_for_api
    response = request_session.post(urljoin(api_url, '/auth/login'), data=invalid_user, allow_redirects=True)
    assert response.status_code == 200  
    assert '<div class="flash">Wrong credentials!</div>' in response.text





