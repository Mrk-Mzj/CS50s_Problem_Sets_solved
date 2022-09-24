# wyciąganie nazwy konta z url użytkownika
# https://twitter.com/davidjmalan/

import re

user_url = input("Podaj URL twojego konta: ").strip()

# 1: username = user_url.replace("https://twitter.com/", "")
# 2: username = user_url.removeprefix("https://twitter.com/")

# 3: re.sub - od: substitute, zamień
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", user_url)
print(f"Nazwa użytkownika #3 to {username}")

# Jest z tym jeden problem. Re.sub czyści zmienną, o ile znajdzie coś do czyszczenia,
# ale przepuści input z czapy, np. www.google.com

# 4: re.search
if matches := re.search(r"^(https?://)?(www\.)?twitter\.com/(.+)$", user_url, re.IGNORECASE):
    username = matches.group(3)
    print(f"Nazwa użytkownika #4 to {username}")

# 5: można też nie przechwytywać nawiasów, które są zastosowane tylko ze względu na logikę (?:  )
# Przy okazji dopuszczam tylko wybrane znaki, tolerowane przez Twitter
# i usuwam "?", żeby nie łapać np. slasha kończącego url, lub kodu śledzącego przekierowania
if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)", user_url, re.IGNORECASE):
    username = matches.group(1)
    print(f"Nazwa użytkownika #5 to {username}")
