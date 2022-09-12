
# uruchamiamy np tak: python "kurs CS50 - 06 - modules 04 - API cleaned.py" Metallica
import requests
import sys

# zabezpieczenie przed uruchomieniem bez argumentu
if len(sys.argv) != 2:
    sys.exit()

# pobieramy surowy plik JSON i konwertujemy do formatu w stylu Pythona
server_JSON_raw = requests.get('https://itunes.apple.com/search?entity=song&limit=1&term=' + sys.argv[1])
python_JSON_clean = server_JSON_raw.json()


# Wynik drukowania server_JSON_clean to niestety lany tekst. Możemy ładniej sformatować te wyniki.
# Zróbmy to z użyciem biblioteki JSON. Użyjemy funkcji dump string (dumps), z wcięciem na 2 spacje (indent=2)
import json
print('\n', json.dumps(server_JSON_raw.json(), indent=2))

# Widzimy teraz wyraźnie strukturę pliku od iTunes.
# Odebrany słownik ma 2 pary kluczy i wartości {'resultCount': 1, 'results': [...lista pythona...]}
# Uprzedzają one, ile będzie wyników i wypisują te wyniki.
# Wyniki to jednoelementowa lista pythona (bo o tyle piosenek prosiliśmy). Lista może mieć dowolną ilość elementów.
# Ten jedyny element to zagnieżdżony słownik, pełen informacji o piosence, podanych jako pary.


# Wyciągnijmy nazwę piosenki. Napiszemy pętlę, która wyjmie kilka nazw, nawet jeśli w URL wpiszemy liczbę większą, niż początkowe 1.
for element in python_JSON_clean["results"]:
    print('utwór:', element["trackName"],'\n')

