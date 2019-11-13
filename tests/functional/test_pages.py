import pytest
from flask import Flask

from app import app

@pytest.fixture
def client():
  client = app.test_client()
  return client

def test_assert():
    assert True

def test_frontpage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Latest news" in response.data
    assert b"Skateboarding" in response.data
    assert b"Snowboarding" in response.data
    assert b"Login" in response.data

