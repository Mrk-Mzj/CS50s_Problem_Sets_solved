-- tabelę utworzyłem z terminala SQLite
-- plik EXE leży w: GitHub-Private-Projects\CS50X\07__SQL\cs50x__07_02__z_wykladu_z_uzyciem_SQLite_exe\sqlite3.exe
-- Urzuchamiam go i wpisuję (uwaga na / zamiast \):

.cd "C:/_Marek - projekty/Programowanie/GitHub-Private-Projects/CS50X/09__Flask/09_07__zapisy__i_usuwanie_z_SQLite/"
.open zapisani.db
CREATE TABLE zapisani (id INTEGER, name TEXT NOT NULL, sport TEXT NOT NULL, PRIMARY KEY(id));

-- Gdyby SQLite nie chce wyjść z trybu wpisywania zapytania (wyświetla ciągle kolejne linie ...>), znaczy to,
-- że zabrakło średnika na końcu linii. 