# tutorial short PL: https://www.youtube.com/watch?v=2ySohVXvnHI
# tutorial long  EN: https://www.youtube.com/watch?v=XVv6mJpFOb0

# pip install beautifulsoup4
# pip install lxml

import requests
from bs4 import BeautifulSoup


request = requests.get(
    "https://www.funduszeeuropejskie.gov.pl/wyszukiwarka/mikro-male-i-srednie-przedsiebiorstwa/#/3756=Mikro,%20ma%C5%82e%20i%20%C5%9Brednie%20przedsi%C4%99biorstwa"
)

soup = BeautifulSoup(request.text, "lxml")
print(soup.prettify())
