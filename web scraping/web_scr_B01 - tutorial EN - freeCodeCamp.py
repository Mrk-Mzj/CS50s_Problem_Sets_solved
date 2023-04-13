# https://www.freecodecamp.org/news/how-to-scrape-multiple-web-pages-using-python/

# pip install beautifulsoup4
# pip install requests
# pip install lxml

import requests
from bs4 import BeautifulSoup


website = "https://subslikescript.com/movie/Titanic-120338"

result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, "lxml")

# drukowanie całej strony internetowej:
# print(soup.prettify())


# Chcemy pobrać tytuł i opis filmu.
# Cała istotna część strony www mieści się w tagu "article", o klasie "main-article":
# <article class="main-article"> ... </article>
# wyszukajmy go metodą find:
box = soup.find("article", class_="main-article")


# Tytuł mieści się w tagu <h1>. Znajdźmy go wewnątrz obiektu box i pobierzmy tekst:
title = box.find("h1").get_text()  # type: ignore  (Pylance podkreśla błędy bo nie sprawdziliśmy czy box istnieje)


# Opis filmu mieści się w divie o klasie "full-script".
transcript = box.find("div", class_="full-script")  # type: ignore


# Wyczyścimy opis. Strip usunie wszystkie nadmiarowe spacje. Zastąpimy je pojedynczą spacją:
transcript = transcript.get_text(strip=True, separator=" ")  # type: ignore


# Pozyskany tytuł i opis filmu możemy wrzucić do CSV, JSONa lub pliku TXT:
with open(f"web scraping/scrapped/web_scr_B01_{title}.txt", "w", encoding="utf-8") as file:
    file.write(transcript)
