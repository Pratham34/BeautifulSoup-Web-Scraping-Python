from bs4 import BeautifulSoup 

with open("index.html","r") as f:
    doc = BeautifulSoup(f,"html.parser")

# print(doc)
# print(doc.prettify())

tag = doc.title
# print(tag)
print(tag.string)

tag.string="hello"
print(tag.string)
print()
print(doc)

print()

# tags = doc.find("p")
# tags = doc.find_all("p")
# print(tags)


tags = doc.find_all("p")[0]
print(tags.find_all("b"))