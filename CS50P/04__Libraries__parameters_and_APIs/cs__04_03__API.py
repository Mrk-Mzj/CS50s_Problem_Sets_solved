# Pomysł na użycie API. łączymy się z iTunes. Pobieramy info o piosence (entity), numer 1 (song), z zespołu Metallica (term)
# https://itunes.apple.com/search?entity=song&limit=1&term=metallica
# wbicie tego w przeglądarkę zwraca surowy plik tekstowy JSON.

# pip install requests - instalujemy z pip pakiet requests, który pozwala korzystać z API, jakby nasz program był przeglądarką
# importujemy też obsługę przekazywnia parametrów (sys) podczas uruchamiania programu
"""
python "cs__04_03__API" Metallica
"""
import requests
import sys

# Pozwólmy użytkownikowi samemu wybrać zespół, ale zabezpieczmy się;
# jeśli program zostanie uruchomiony bez pojedynczego argumentu, opuść go
if len(sys.argv) != 2:
    sys.exit()

# pobieramy surowy plik tekstowy JSON
server_JSON = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]
)

# tego pliku nie da się wprost wydrukować; otrzymalibyśmy cyfrę 200 (komunikat, że serwer jest ok)
# konwertujemy ten plik do obiektu - słownika Pythona:
python_JSON_dict = server_JSON.json()
print("\n", python_JSON_dict)

# BTW: metoda .json() służy do konwersji odpowiedzi z serwera; gdybyśmy mieli w kodzie obiekt JSON, konwertowalibyśmy go na słownik poleceniem:
# import json
# y = json.loads(x)
