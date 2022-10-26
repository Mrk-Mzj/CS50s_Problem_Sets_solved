-- SQLite
-- Ctrl + Shipt + P  ->  SQLite Open Database
-- zaznaczenie wybranego polecenia, PPM, Run Selected Query

.schema
SELECT * FROM people WHERE name = "Steve Carell";
SELECT * FROM shows WHERE title = "The Office" AND year = 2005;

-- zmierzmy czas szukania:
.timer on 
SELECT * FROM shows WHERE title = "The Office";
-- Run Time: real 0.034 user 0.000000 sys 0.031250

-- zindeksujmy kolumnę title i sprawdźmy teraz czas:
CREATE INDEX "title_index" ON "shows" ("title");
.timer on
SELECT * FROM shows WHERE title = "The Office";
-- Run Time: real 0.001 user 0.000000 sys 0.000000


-- Zaindeksujmy inne ważne kolumny. Kosztem będzie czas indeksowania i miejsce w pamięci.birth
-- Zyskiem błyskawiczny czas działania złożonych zapytań.birth
CREATE INDEX "people_index" ON "people" ("name");
CREATE INDEX person_index ON stars (person_id);
CREATE INDEX show_index ON stars (show_id);

-- możemy robić złożone zapytania:
SELECT title FROM shows WHERE id IN 
(SELECT show_id FROM stars WHERE person_id = 
(SELECT id FROM people WHERE name = "Steve Carell"));

-- Czytajmy nazwy tablic:
-- znajdź 'tytuły', w których 'gwiazdą' jest 'człowiek' o imieniu "Steve Carell".

-- To zapytanie działa, ponieważ tablica 'stars' pośredniczy między 'shows' i 'people'
-- jej 'show_id' to 'id' z shows,
-- jej 'person_id' to 'id' z people.

-- Steve'a łączymy ze 'stars' znakiem równości, bo chodzi nam o tego konkretnego (id=136797).
-- Wynikiem jest zbiór kilkudziesięciu show_id. Trzeba je przełożyć na tytuły.
-- Tytuł show szukamy w tym podzbiorze przy pomocy IN.

-- Czemu IMDB stworzyło pośrednią tablicę 'stars', zamiast połączyć wprost ludzi z filmami?
-- Bo człowiek w filmie to może być gwiazda, albo reżyser, albo scenarzysta, itd. 
-- Tablice pośrednie określają rolę człowieka w filmie.


-- Możemy wirtualnie łączyć tablice przy pomocy ich Primary i Foreign Keys, 
-- i szukać w takim zbiorze. To zajmie chwilę, jeśli nie indeksowaliśmy ważnych kolumn:
SELECT title FROM people 
JOIN stars ON people.id = stars.person_id
JOIN shows ON stars.show_id = shows.id
WHERE name = "Steve Carell";
-- czyt. wybierz tytuły, w których gwiazdą był Steve Carell.

-- To samo polecenie zapisane czytelniej:
SELECT title FROM people, stars, shows
WHERE people.id = stars.person_id
AND stars.show_id = shows.id
AND name = "Steve Carell";


-- NIEBEZPIECZEŃSTWA: SQL INJECTION

-- Logowanie napisane źle:

-- rows = db.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'")
-- if len(rows) == 1:
--     # Log user in

-- To błąd, bo user może wpisać login, który zmieni odpytywanie o hasło w komentarz i je zignoruje:

-- malan@harvard.edu'--
-- rows = db.execute(f"SELECT * FROM users WHERE username = 'malan@harvard.edu'--

-- ...albo wstrzyknie swój kod:

-- malan@harvard.edu'--; DROP database;
-- rows = db.execute(f"SELECT * FROM users WHERE username = malan@harvard.edu'--; DROP database;

-- Poprawna metoda to:

-- rows = db.execute("SELECT * FROM users WHERE username = ? AND password = ?", username, password)
-- if len(rows) == 1:
--     # Log user in


-- NIEBEZPIECZEŃSTWA: RACE CONDITIONS

-- Czyli problemy z nakładającymi się zapytaniami przy dużym ruchu sieciowym. Np. dajemy like. Baza wczytuje
-- liczbę lajków, dodaje 1, zapisuje. W tym samym czasie inny user daje lajk, wczytuje tę samą wartość, 
-- co my, dodaje 1, jak my, i zapisuje to samo. Rozwiązuje się to tzw. transakcjami: 
-- SQL supports transactions, where we can lock rows in a database, such that a particular set of actions are atomic, 
-- or guaranteed to happen together.

-- zapis podatny:

-- rows = db.execute("SELECT likes FROM posts WHERE id = ?", id);
-- likes = rows[0]["likes"]
-- db.execute("UPDATE posts SET likes = ? WHERE id = ?", likes + 1, id);

-- zapis poprawny:

-- db.execute("BEGIN TRANSACTION")
-- rows = db.execute("SELECT likes FROM posts WHERE id = ?", id);
-- likes = rows[0]["likes"]
-- db.execute("UPDATE posts SET likes = ? WHERE id = ?", likes + 1, id);
-- db.execute("COMMIT")