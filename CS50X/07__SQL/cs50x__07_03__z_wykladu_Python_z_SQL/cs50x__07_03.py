# favorites.csv to plik z wynikiem ankiety na ulubiony serial uczestników kursu.
# zawiera timestamp, tytuł, gatunki.
#
# Jeśli chcemy odfiltrować same komedie musimy napisać:
# SELECT title FROM favorites WHERE genre = "Comedy";
# ale też ... WHERE genre = "Comedy, Drama"; ... WHERE genre = "Comedy, News"; itd.
# Zamiast znaku równości w tym wypadku lepiej użyć LIKE.
# Ale to słowo pomyli np. "Music" z "Musical". SQL jest szybki, ma jednak ograniczone możliwości,
# np. brak regex. Czasem trzeba użyć Pythona.

# Do spięcia Pythona z SQLite użyjemy uproszczonej biblioteki CS50.


import cs50
import csv

# Tworzymy bazę danych:
open("CS50X/07__SQL/cs50x__07_03__z_wykladu_Python_z_SQL/favorites.db", "w").close()
db = cs50.SQL(
    "sqlite:///CS50X/07__SQL/cs50x__07_03__z_wykladu_Python_z_SQL/favorites.db"
)

# Tworzymy w niej 2 tablice: shows i genres
db.execute("CREATE TABLE shows (id INTEGER, title TEXT NOT NULL, PRIMARY KEY(id))")
db.execute(
    "CREATE TABLE genres (show_id INTEGER, genre TEXT NOT NULL, FOREIGN KEY(show_id) REFERENCES shows(id))"
)

# Otwieramy plik CSV wyeksportowany z ankiety na Google Docs:
with open(
    "CS50X/07__SQL/cs50x__07_03__z_wykladu_Python_z_SQL/favorites.csv", "r"
) as file:

    reader = csv.DictReader(file)

    # Dla każdego rzędu w pliku CSV...
    for row in reader:

        # ...tytuł zmieniamy na wielkie litery dla łatwiejszej pracy, przypisujemy do zmiennej title
        # i wstawiamy do tablicy shows. Zapis: (?) to odpowiednik {title}

        title = row["title"].strip().upper()
        show_id = db.execute("INSERT INTO shows (title) VALUES(?)", title)

        # db.execute to komenda z biblioteki cs50.SQL
        # W przypadku komendy INSERT i tabeli z autonumerowanym Primary Key
        # zwraca numer Primary Key tego nowo utworzonego rzędu.

        # Każdy gatunek wstawiamy do tablicy genres:
        for genre in row["genres"].split(", "):
            db.execute(
                "INSERT INTO genres (show_id, genre) VALUES(?, ?)", show_id, genre
            )
