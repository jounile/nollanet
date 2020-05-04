from requests import get
from urllib.parse import urljoin

def test_login_page(wait_for_api):
    request_session, api_url = wait_for_api
    response = request_session.get(urljoin(api_url, '/auth/login'))
    assert response.status_code == 200
    assert "<h2>Login</h2>" in response.text