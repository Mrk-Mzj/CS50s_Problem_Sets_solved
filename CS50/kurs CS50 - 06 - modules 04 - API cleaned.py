
"""
python "kurs CS50 - 06 - modules 04 - API cleaned.py" Metallica
"""
import requests
import sys

# zabezpieczenie przed uruchomieniem bez argumentu
if len(sys.argv) != 2:
    sys.exit()

# pobieramy surowy plik tekstowy JSON i konwertujemy do obiektu - słownika Pythona
server_JSON = requests.get('https://itunes.apple.com/search?entity=song&limit=1&term=' + sys.argv[1])
python_JSON_dict = server_JSON.json()


# Wynik drukowania python_JSON to niestety lany tekst. Możemy ładniej sformatować te wyniki. Zróbmy to z użyciem biblioteki JSON.
# Skonwertujemy słownik Pythona do obiektu JSONa. Użyjemy funkcji dump string (dumps), z wcięciem na 2 spacje (indent=2)

import json
python_JSON_obj = json.dumps(python_JSON_dict, indent=2)
print('\n', python_JSON_obj)

# Widzimy teraz wyraźnie strukturę pliku od iTunes.
# Odebrany słownik ma 2 pary kluczy i wartości {'resultCount': 1, 'results': [...lista pythona...]}
# Uprzedzają one, ile będzie wyników i wypisują te wyniki.
# Wyniki to jednoelementowa lista pythona (bo o tyle piosenek prosiliśmy). Lista może mieć dowolną ilość elementów.
# Ten jedyny element to znów słownik, pełen par kluczy i wartości, z informacjami o piosence.


# Wyciągnijmy nazwę piosenki. Napiszemy pętlę, która wyjmie kilka nazw, nawet jeśli w URL wpiszemy liczbę większą, niż początkowe 1.
for element in python_JSON_dict["results"]:
    print('utwór:', element["trackName"],'\n')

