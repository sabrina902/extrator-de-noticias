import requests
from bs4 import BeautifulSoup

URL = "https://g1.globo.com"
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

# Ajuste o seletor conforme o site
titulos = [titulo.get_text() for titulo in soup.find_all("a", class_="feed-post-link")]

print(titulos)  # Verifique os títulos extraídos
