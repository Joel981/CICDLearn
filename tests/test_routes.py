import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    return app.test_client()

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Flask App" in response.data

def test_about(client):
    response = client.get('/about')
    assert response.status_code == 200
    assert b"About Page" in response.data
