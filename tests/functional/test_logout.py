from requests import get
from urllib.parse import urljoin

def test_logout_page(wait_for_api):
    request_session, api_url = wait_for_api
    response = request_session.get(urljoin(api_url, '/auth/logout'))
    assert response.status_code == 200
    assert "<span>Latest news</span>" in response.text