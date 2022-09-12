
# Pomysł na użycie API. łączymy się z iTunes. Pobieramy info o piosence (entity), numer 1 (song), z zespołu Metallica (term)
# https://itunes.apple.com/search?entity=song&limit=1&term=metallica
# wbicie tego w przeglądarkę zwraca surowy plik tekstowy JSON.

# pip install requests - instalujemy z pip pakiet requests, który pozwala korzystać z API, jakby nasz program był przeglądarką
#importujemy też obsługę przekazywnia parametrów (sys) podczas uruchamiania programu
# uruchamiamy np tak: python "kurs CS50 - 06 - modules 03 - API.py" Metallica
import requests
import sys

# Pozwólmy użytkownikowi samemu wybrać zespół, ale zabezpieczmy się;
# jeśli program zostanie uruchomiony bez pojedynczego argumentu, opuść go
if len(sys.argv) != 2:
    sys.exit()

# pobieramy surowy plik JSON
server_JSON_raw = requests.get('https://itunes.apple.com/search?entity=song&limit=1&term=' + sys.argv[1])

# wydrukujmy odpowiedź serwera sformatowaną do JSONa, który zrozumie Python:
python_JSON_clean = server_JSON_raw.json()
print('\n',python_JSON_clean)

