from requests import get
from urllib.parse import urljoin

# Dummy test
def test_assert():
    assert True

def test_frontpage(wait_for_api):
    request_session, api_url = wait_for_api
    response = request_session.get(api_url)
    assert response.status_code == 200
    # Sections
    assert "<span>Latest news</span>" in response.text
    assert "<span>Skateboarding</span>" in response.text
    assert "<span>Snowboarding</span>" in response.text
    assert "<span>Interviews</span>" in response.text
    assert "<span>Reviews</span>" in response.text
    assert "<span>Spots</span>" in response.text
    assert "<span>Links</span>" in response.text
    # Login link exists
    assert "Login" in response.text










