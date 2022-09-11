# pip install requests - instalujemy pakiet który pozwala korzystać z API, jakby nasz program był przeglądarką
# uruchamiamy np tak: python kurs CS50 - 06 - modules 03 - API.py Queen

#importujemy też obsługę przekazywnia parametrów podczas uruchamiania programu
import requests
import sys

#gdy program zostanie uruchomiony bez pojedynczego argumentu, opuść go
if len(sys.argv) =! 2:
    sys.exit()

# łączymy się z itunes. Pobieramy info o piosence (entity), numer 1 (song), z zespołu Queen (term)
# https://itunes.apple.com/search?entity=song&limit=1&term=queen
# wbicie tego w przeglądarkę zwraca plik JSON.

# Pobierzmy to programem tak, by user mógł sam wybrać zespół:
server_says = requests.get('https://itunes.apple.com/search?entity=song&limit=1&term=' +sys.argv[1])

# wydrukujmy odpowiedź serwera sformatowaną do kodu JSONa
print(server_says.json)

