from requests import get
from urllib.parse import urljoin

def test_register_page(wait_for_api):
    request_session, api_url = wait_for_api
    response = request_session.get(urljoin(api_url, '/auth/register'))
    assert response.status_code == 200
    assert "<h2>Register</h2>" in response.text