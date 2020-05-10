import io
import pytest
from requests import get
from urllib.parse import urljoin

def test_my_uploads_page(wait_for_api, login_user):
    """
    GIVEN a user has logged in (login_user)
    WHEN the '/my/uploads' page is navigated to (GET)
    THEN check the response is valid and page title is correct
    """
    request_session, api_url = wait_for_api
    response = request_session.get(urljoin(api_url, '/my/uploads'))
    assert response.status_code == 200
    assert '<h1>My uploads</h1>' in response.text

def test_valid_new_upload_page(wait_for_api, login_user):
    """
    GIVEN a user has logged in (login_user)
    WHEN the '/media/newupload' page is navigated to (GET)
    THEN check the response is valid and page title is correct
    """
    request_session, api_url = wait_for_api
    response = request_session.get(urljoin(api_url, '/media/newupload'))
    assert response.status_code == 200
    assert '<h1>New upload</h1>' in response.text

def test_invalid_new_upload_page(wait_for_api):
    """
    GIVEN a user has not logged in
    WHEN the '/media/newupload' page is navigated to (GET)
    THEN check the response is valid and page title is correct
    """
    request_session, api_url = wait_for_api
    response = request_session.get(urljoin(api_url, '/media/newupload'))
    assert response.status_code == 200
    assert '<div class="flash">Please login first</div>' in response.text

def test_new_upload(wait_for_api, login_user):
    """
    GIVEN a user has logged in (login_user)
    WHEN the '/media/newupload' page is posted an example image (POST)
    THEN check the response is valid and the page title is correct
    """
    example_file=open("./app/static/gfx/example.png","rb")
    files = { 'file': example_file }
    request_session, api_url = wait_for_api
    response = request_session.post(urljoin(api_url, '/media/newupload'), files=files, allow_redirects=True)
    assert response.status_code == 200
    assert '<h1>My uploads</h1>' in response.text

#def test_remove_upload(wait_for_api, login_user):
#    """
#    GIVEN a user has logged in (login_user)
#    WHEN the '/blob/delete' page is posted (POST)
#    THEN check the response is valid and the user is logged in
#    """
#    valid_blob = dict(blob_path='images/*example.png', upload_id=2)
#    request_session, api_url = wait_for_api
#    response = request_session.post(urljoin(api_url, '/blob/delete'), data=valid_blob, allow_redirects=True)
#    assert response.status_code == 200  
#    assert 'example.png was deleted successfully' in response.text

    