from bs4 import BeautifulSoup
import re

with open("index.html","r") as f:
    doc = BeautifulSoup(f,"html.parser")

tag = doc.find("option")
# print(tag)
tag['value'] = 'new value'
tag['color'] = 'blue'
print(tag.attrs)
print(tag)

print()

# tags = doc.find_all(["p","div","li"])
# print(tags)

# tags = doc.find_all(["option"],text="Undergraduate",value="undergraduate")
# print(tags)

# tags = doc.find_all(class_="btn-item")
# print(tags)

# tags = doc.find_all(text=re.compile("\$.*"),limit=1)

tags = doc.find_all(text=re.compile("\$.*"))
# print(tags)
for tag in tags:
    print(tag.strip())

tags = doc.find_all("input",type="text")
for tag in tags:
    tag['placeholder'] = "I changed you!"

with open("changed.html","w") as file:
    file.write(str(doc))        