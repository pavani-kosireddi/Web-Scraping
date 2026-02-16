import requests
from bs4 import BeautifulSoup
url = "https://iwf.sport/weightlifting_/athletes-bios/?athlete=alsebaai-yahea-2010-04-17&id=21653"
response = requests.get(url)
soup = BeautifulSoup(response.text)
print(response.status_code)
# print(soup.get_text())
