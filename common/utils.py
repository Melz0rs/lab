import requests


def fetch_html(url):
    html = None

    response = requests.get(url)

    if response.status_code == 200:
        html = response.text

    return html.strip()
