from urllib import response
import pytest
import requests

def test_health_endpoints_status_code():
    """
    Test health endpoints status code
    """
    url = 'http://localhost:8080/health'
    response = requests.get(url)
    assert response.status_code == 200

def test_health_endpoint_message():
    """
    Test health endpoint message
    """
    url = 'http://localhost:8080/health'
    response = requests.get(url)
    assert "All Systems On!!!" in response.text
