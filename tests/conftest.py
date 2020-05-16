import pytest
import requests
from urllib.parse import urljoin
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

pytest_plugins = ["docker_compose"]

from selenium import webdriver

###################################
######## Selenium fixtures ########
###################################

@pytest.fixture(scope="class")
def setup_chromedriver(request):
    # Setup ChromeDriver
    print("initiating chrome driver")
    driver = webdriver.Chrome("/Users/jouni.leino/chromedriver") #if not added in PATH
    driver.get("http://localhost:8000")
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.close()


###################################
###### Non-selenium fixtures ######
###################################

# Invoking this fixture: 'function_scoped_container_getter' starts all services
@pytest.fixture(scope="function")
def wait_for_api(function_scoped_container_getter):
    """Wait for the api from site to become responsive"""
    request_session = requests.Session()
    retries = Retry(total=5,
                    backoff_factor=0.1,
                    status_forcelist=[500, 502, 503, 504])
    request_session.mount('http://', HTTPAdapter(max_retries=retries))

    service = function_scoped_container_getter.get("site").network_info[0]
    api_url = "http://%s:%s" % (service.hostname, service.host_port)
    assert request_session.get(api_url)
    return request_session, api_url

@pytest.fixture(scope="function")
def login_user(wait_for_api):
    """
    GIVEN a running site container
    WHEN the '/auth/login' page is posted user credentials (POST)
    THEN check the response is valid and the user is logged in and the Logout link is available
    """
    valid_user = dict(username='tester', password='tester')

    request_session, api_url = wait_for_api
    response = request_session.post(urljoin(api_url, '/auth/login'), data=valid_user, allow_redirects=True)
    assert response.status_code == 200
    assert '<div class="flash">Welcome tester!</div>' in response.text
    assert '<a class="nav-link" href="/auth/logout">Logout</a>' in response.text

@pytest.fixture(scope="function")
def login_admin(wait_for_api):
    """
    GIVEN a running site container
    WHEN the '/auth/login' page is posted admin credentials (POST)
    THEN check the response is valid and the user is logged in and the Logout link is available
    """
    valid_user = dict(username='admin', password='admin')

    request_session, api_url = wait_for_api
    response = request_session.post(urljoin(api_url, '/auth/login'), data=valid_user, allow_redirects=True)
    assert response.status_code == 200
    assert '<div class="flash">Welcome admin!</div>' in response.text
    assert '<a class="nav-link" href="/auth/admin">Admin</a>' in response.text
    assert '<a class="nav-link" href="/auth/logout">Logout</a>' in response.text

