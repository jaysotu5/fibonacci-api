import pytest
import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from run import app  # Import the Flask app object

# This is the test client provided by Flask for testing
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Test the Fibonacci API for valid input
def test_fibonacci_valid_input(client):
    # Test known Fibonacci numbers
    response = client.get('/fibonacci/0')
    assert response.status_code == 200
    assert response.json == {f"fibonacci({0})": 0}

    response = client.get('/fibonacci/1')
    assert response.status_code == 200
    assert response.json == {f"fibonacci({1})": 1}

    response = client.get('/fibonacci/10')
    assert response.status_code == 200
    assert response.json == {f"fibonacci({10})": 55}

# Test the Fibonacci API for invalid input
def test_fibonacci_invalid_input(client):
    response = client.get('/fibonacci/-1')
    assert response.status_code == 400
    assert response.json == {'error': 'Input must be a non-negative integer'}
