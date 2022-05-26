import pytest
import requests

def test_get_all_comments():
    # step 1: authenticate
    payload = {"username": "admin", "password": "admin"}
    response = requests.post("http://localhost:8080/auth/login", data=payload)
    assert response.status_code == 200

    
    #step 2: get all comments
    access_token = response.json()['access_token']
    request_headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
    response = requests.get("http://localhost:8080/comments", headers=request_headers)
    assert response.status_code == 200