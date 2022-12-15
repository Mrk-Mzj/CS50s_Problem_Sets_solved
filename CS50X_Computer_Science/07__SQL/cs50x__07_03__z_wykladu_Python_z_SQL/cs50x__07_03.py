# https://cs50.harvard.edu/x/2022/notes/7/
#
# # favorites.csv to plik z wynikiem ankiety na ulubiony serial uczestników kursu.
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

# Tworzymy w niej 2 tablice: shows i genres.
# id w tablicy shows zostaje przepisane do show_id w tablicy genres.
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

        # ...tytuł zmieniamy na wielkie litery dla łatwiejszej pracy...
        title = row["title"].strip().upper()

        # i wstawiamy do tablicy shows, w miejsce znaku zapytania:
        show_id = db.execute("INSERT INTO shows (title) VALUES(?)", title)

        # Uwaga: SQLite domyślnie tworzy kolumnę rowid z autoinkrementacją. Jeśli jednak zadeklarujemy
        # kolumnę integer typu Primary Key, to ona będzie autoinkrementowana.
        # Dlatego uzupełniamy 'title' i nie martwimy się o 'id'.

        # db.execute to komenda z biblioteki cs50.SQL
        # W przypadku komendy INSERT i tabeli z autonumerowanym Primary Key
        # zwraca numer Primary Key tego nowo utworzonego rzędu
        # https://docs.cs50.net/2018/x/psets/7/finance/finance.html#hints

        # Każdy gatunek oddzielony przecinkiem rozdzielamy i wstawiamy do tablicy genres:
        for genre in row["genres"].split(", "):
            db.execute(
                "INSERT INTO genres (show_id, genre) VALUES(?, ?)", show_id, genre
            )

# Utworzyliśmy bazę danych z tablicą tytułów i tablicą z ładnie wydzielonymi gatunkami.
# Możemy łatwo znaleźć komedie zapytaniem:

# SELECT title FROM shows WHERE id IN (SELECT show_id FROM genres WHERE genre = "Comedy");
# czyt. znajdź tytuły, których id są w puli (znajdź id filmów, które są komedią)

# Możemy usunąć powtórzone tytuły i posortować wyniki:
# SELECT DISTINCT(title) FROM shows WHERE id IN (SELECT show_id FROM genres WHERE genre = "Comedy") ORDER BY title;
