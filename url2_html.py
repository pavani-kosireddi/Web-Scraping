import requests
from bs4 import BeautifulSoup
url = "https://uww.org/athletes-results"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.get_text())
