import pytest
import requests
from testlib.utils import build_requests_headers

def test_get_all_comments(login_as_admin):
    #step 2: get all comments
    request_headers = build_requests_headers(login_as_admin)
    response = requests.get("http://localhost:8080/comments", headers=request_headers)
    assert response.status_code == 200