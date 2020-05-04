from requests import get
from urllib.parse import urljoin

def test_news_page(wait_for_api):
    request_session, api_url = wait_for_api
    response = request_session.get(urljoin(api_url, '/news/all'))
    assert response.status_code == 200
    assert "<h1>News</h1>" in response.text