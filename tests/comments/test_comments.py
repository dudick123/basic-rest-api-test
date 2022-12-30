import requests
from lib.utils import build_requests_headers

def test_get_all_comments(login_as_admin):
    url = 'http://localhost:8080/comments'
    headers = build_requests_headers(login_as_admin)
    response = requests.get(url, headers = headers)
    assert response.status_code == 200
