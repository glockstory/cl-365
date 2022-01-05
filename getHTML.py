import requests as req


def get_html(url):
    r = req.get(url)
    return r.text