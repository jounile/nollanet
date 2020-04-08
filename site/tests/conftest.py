from app import app
from flask import Flask
import pytest

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    return app

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('flask_test.cfg')
    testing_client = flask_app.test_client()
 
    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()
 
    yield testing_client  # this is where the testing happens!
 
    ctx.pop()