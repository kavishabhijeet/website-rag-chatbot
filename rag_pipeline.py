from dotenv import load_dotenv
load_dotenv()

import requests
from bs4 import BeautifulSoup


def load_website(url):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    text = soup.get_text()

    return text