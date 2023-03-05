# tutorial short PL: https://www.youtube.com/watch?v=2ySohVXvnHI

# pip install beautifulsoup4
# pip install lxml
# pip install prettyprint


import requests
from bs4 import BeautifulSoup
import pprint


request = requests.get("http://quotes.toscrape.com/")
soup = BeautifulSoup(request.text, "lxml")
print()

# drukowanie całego HTML:
# print(soup.prettify())


# wybór klasy author:
names = soup.select(".author")


# drukowanie klasy. Wynikiem jest pozioma lista na szerokość strony:
print(names, "\n")


# drukowanie z pretty print. Wynikiem jest pionowa lista podzielona enterami
# (z nawiasem klamrowym i przecinkami):
pprint.pprint(names)
print()


# drukowanie. Wynikiem są pionowo wypisane elementy listy
# (bez nawiasu kwadratowego i przecinków).
# Dodatkowo .text formatuje wynik do samych nazwisk (bez tagów HTML). Niestety są duplikaty:
for _ in names:
    print(_.text)


# Drukowanie bez dupikatów i alfabetycznie.
# Stwórzmy set authors_names i dodajmy do niego każdą linijkę.
# Wydrukujmy posortowane alfabetycznie:
authors_names = set()

for _ in names:
    authors_names.add(_.text)
print()

for author in sorted(authors_names):
    print(author)
