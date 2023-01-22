from bs4 import BeautifulSoup
import requests
import re

gpu = input("What product do you want to search for? ")

url = f"https://www.newegg.com/p/pl?d={gpu}&N=4131"
page = requests.get(url).content
doc = BeautifulSoup(page,"html.parser")
print(doc.prettify())
# soup = BeautifulSoup(page, 'lxml')

page_text = doc.find('span',class_="list-tool-pagination-text")
print(page_text)

# page_text = soup.select_one("span.list-tool-pagination-text")
# print(page_text)