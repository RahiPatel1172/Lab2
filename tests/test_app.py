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