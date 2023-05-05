import json
from bs4 import BeautifulSoup
import requests

# Récupérer le code HTML de la page de produits
page = requests.get("https://www.amazon.com/s?k=gaming&i=electronics-intl-ship&crid=2Y2L14SKA4NJM&sprefix=gaming%2Celectronics-intl-ship%2C240&ref=nb_sb_noss")
soup = BeautifulSoup(page.content, 'html.parser')
data = []

# Extraire les informations de chaque produit sur la page
products = soup.find_all("div", {"class": "s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col sg-col-12-of-16"})
for product in products:
    price = product.find("span", {"class": "a-price-whole"}).text.strip()
    description = product.find("span", {"class": "a-size-base-plus a-color-base a-text-normal"}).text.strip()
    image = product.find("img", {"class": "s-image"})["src"]
    data.append({'link': image, 'description': description, 'price': price})

# Write the data to a JSON file
with open('data2.json', 'w') as f:
    json.dump(data, f)

