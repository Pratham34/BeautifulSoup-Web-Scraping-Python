from bs4 import BeautifulSoup
import requests

url = f"https://www.newegg.ca/gigabyte-geforce-rtx-4080-gv-n4080gaming-oc-16gd/p/N82E16814932561?Description=GIGABYTE%20Gaming%20GeForce%20R&cm_re=GIGABYTE_Gaming%20GeForce%20R-_-14-932-561-_-Product"

result = requests.get(url)

doc = BeautifulSoup(result.text,"html.parser")
# print(doc.prettify())

prices = doc.find_all(text="$")
print(prices)
parent = prices[0].parent
# print(parent)
strong = parent.find("strong")
# print(strong)
print(strong.string)