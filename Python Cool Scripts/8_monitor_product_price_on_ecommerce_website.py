import requests
import bs4
import time
from tkinter import messagebox

product_url = "https://www.flipkart.com/apple-2020-macbook-air-m1-8-gb-256-gb-ssd-mac-os-big-sur-mgnd3hn-a/p/itma8a9681af6907"

# while True:
product = requests.get(url=product_url)
# convert to beautiful soup object
soup    = bs4.BeautifulSoup(product.text, "lxml")
# find the price of the product by using class name
print(soup)
price   = soup.find("", {"class": "_30jeq3 _16Jk6d"})
print(price)
print(type(price))
# break
