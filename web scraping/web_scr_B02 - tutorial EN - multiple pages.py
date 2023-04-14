# Part 2: Pobieranie linków do wielu filmów
# https://www.freecodecamp.org/news/how-to-scrape-multiple-web-pages-using-python/

# pip install beautifulsoup4
# pip install requests
# pip install lxml

import requests
from bs4 import BeautifulSoup


root = "https://subslikescript.com"
website = f"{root}/movies"

result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, "lxml")


# Podobnie, jak na podstronie z filmem, i tu
# cała istotna część strony www mieści się w tagu "article", o klasie "main-article":
# <article class="main-article"> ... </article>
# wyszukajmy go metodą find:
box = soup.find("article", class_="main-article")


# Chcemy pobrać wszystkie linki do filmów, jakie są na tej stronie.
# Używamy metody box.find_all('a', href=True) do utworzenia listy tagów <a>. Wygląda ona tak:

# [<a href="movie/Blind_Detective-2332707" title="Read transcript of Movie 'Blind Detective'"><li>Blind Detective (2013)</li></a>,
#  <a href="movie/Killer_Workout-91339" title="Read transcript of Movie 'Killer Workout'"><li>Killer Workout (1987)</li></a>,...]

# Aby uzyskać listę czystych linków piszemy:

links = [link["href"] for link in box.find_all("a", href=True)]  # type: ignore
print(links)


# Mając listę linków, dla każdego możemy puścić scrapping. Używamy kodu z pliku B01:

for link in links:
    result = requests.get(f"{root}/{link}")
    content = result.text
    soup = BeautifulSoup(content, "lxml")
    box = ...
    title = ...
    transcript = ...
