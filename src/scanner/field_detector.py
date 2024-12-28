import requests
from bs4 import BeautifulSoup

def detect_input_fields(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    input_fields = [tag.get('name') for tag in soup.find_all('input') if tag.get('name')]
    return input_fields
