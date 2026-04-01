import requests
from bs4 import BeautifulSoup

def scrape_url(url: str):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    return soup.get_text()