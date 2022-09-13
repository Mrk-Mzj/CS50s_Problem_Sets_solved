import requests

band = "Metallica"
songs = "5"

# pobieramy surowy plik tekstowy JSON
# i konwertujemy do obiektu - słownika Pythona
server_JSON = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=" + songs + "&term=" + band
)
python_JSON_dict = server_JSON.json()


# wypiszmy najlepsze piosenki wykonawcy
print("\nThe Best of " + band + ":\n")

for element in python_JSON_dict["results"]:
    print("-", element["trackName"])

print()
