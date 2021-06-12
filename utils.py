import requests


def web_request():
    resp = requests.get("http://localhost")
    return resp.text
