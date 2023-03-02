# tutorial long  EN: https://www.youtube.com/watch?v=XVv6mJpFOb0

# pip install beautifulsoup4
# pip install lxml


import requests
from bs4 import BeautifulSoup


request = requests.get("http://quotes.toscrape.com/")

soup = BeautifulSoup(request.text, "lxml")
print(soup.prettify())
