import pytest
from flask import Flask

from app import app

@pytest.fixture
def client():
  client = app.test_client()
  return client

def test_assert():
    assert True

def test_front_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Latest news" in response.data
    assert b"Skateboarding" in response.data
    assert b"Snowboarding" in response.data
    assert b"Login" in response.data

def test_news_page(client):
    response = client.get('/news')
    assert response.status_code == 200
    assert b"News" in response.data

def test_youtube_page(client):
    response = client.get('/youtube/playlists')
    assert response.status_code == 200
    assert b"Playlists" in response.data

def test_guides_page(client):
    response = client.get('/guides')
    assert response.status_code == 200
    assert b"Guides" in response.data

def test_login_page(client):
    response = client.get('/auth/login')
    assert response.status_code == 200
    assert b"Guides" in response.data

def test_register_page(client):
    response = client.get('/auth/register')
    assert response.status_code == 200
    assert b"Guides" in response.data

def test_logout_page(client):
    response = client.get('/auth/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b"Latest news" in response.data
