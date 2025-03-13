import pytest
import os
import sys

# Add the project root directory to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from app.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_endpoint(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, CI/CD World!' in response.data

def test_health_endpoint(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert b'Service is healthy!' in response.data

def test_404_endpoint(client):
    response = client.get('/nonexistent')
    assert response.status_code == 404

def test_health_endpoint_post(client):
    response = client.post('/health')
    assert response.status_code == 405  # Method Not Allowed

def test_hello_endpoint_post(client):
    response = client.post('/')
    assert response.status_code == 405  # Method Not Allowed

def test_health_endpoint_put(client):
    response = client.put('/health')
    assert response.status_code == 405  # Method Not Allowed

def test_health_endpoint_delete(client):
    response = client.delete('/health')
    assert response.status_code == 405  # Method Not Allowed 