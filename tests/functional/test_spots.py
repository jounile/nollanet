from requests import get
from urllib.parse import urljoin

def test_spots_page(wait_for_api):
    """
    GIVEN a running site container
    WHEN the '/spots/all' page is navigated to (GET)
    THEN check the response is valid and the page title is correct
    """
    request_session, api_url = wait_for_api
    response = request_session.get(urljoin(api_url, '/spots/all'))
    assert response.status_code == 200
    assert "<h1>Spots</h1>" in response.text

def test_spot_filter(wait_for_api):
    """
    GIVEN a running site container
    WHEN the '/spots/all' page is navigated with filter params type_id=1&maa_id=1&paikkakunta_id=1 (GET)
    THEN check the response is valid and there is a link to spot
    """
    request_session, api_url = wait_for_api
    response = request_session.get(urljoin(api_url, '/spots/all?type_id=1&maa_id=1&paikkakunta_id=1&keyword='))
    assert response.status_code == 200
    assert '1 spots' in response.text
    assert '<a href="/spots/spot/1">Micropolis</a>' in response.text

def test_spot_search(wait_for_api):
    """
    GIVEN a running site container
    WHEN the '/spots/all' page is navigated with filter param keyword=Micropolis (GET)
    THEN check the response is valid, spot count is 1 and there is a link to spot
    """
    request_session, api_url = wait_for_api
    response = request_session.get(urljoin(api_url, '/spots/all?keyword=Micropolis'))
    assert response.status_code == 200
    assert '1 spots' in response.text
    assert '<a href="/spots/spot/1">Micropolis</a>' in response.text

def test_spot_page(wait_for_api):
    """
    GIVEN a running site container
    WHEN the '/spots/spot/1' page is navigated (GET)
    THEN check the response is valid and spot shows rating
    """
    request_session, api_url = wait_for_api
    response = request_session.get(urljoin(api_url, '/spots/spot/1'))
    assert response.status_code == 200
    assert '<h1>Micropolis</h1>' in response.text
    assert '<div id="stars">' in response.text









