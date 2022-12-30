import pytest
import requests

<<<<<<< HEAD
@pytest.fixture(scope='session')
def login_as_admin():
    url = 'http://localhost:8080/auth/login'
    payload = {'username': 'admin', 'password': 'admin'}
    response = requests.post(url, data = payload)
    assert response.status_code == 200
    access_token = response.json()['access_token']
    yield access_token
=======
@pytest.fixture(scope="session")
def login_as_admin():
    payload = {"username": "admin", "password": "admin"}
    response = requests.post("http://localhost:8080/auth/login", data=payload)
    assert response.status_code == 200

    access_token = response.json()['access_token']
    yield access_token
>>>>>>> origin/main
