def build_requests_headers(access_token, content_type="application/json"):
    request_headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": content_type,
        "Accept": "application/json"
    }
    return request_headers