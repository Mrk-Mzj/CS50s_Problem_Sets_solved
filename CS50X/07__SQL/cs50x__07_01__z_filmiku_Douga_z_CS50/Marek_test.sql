-- SQLite

-- Zaznacz wybrany fragment kodu, kliknij prawym, 
-- i wybierz Run Selected Querry.

-- Podgląd tabeli (w ramach tej wtyczki) uzyskasz dzięki 
-- poleceniu SELECT. Podgląd możliwy jest też dzięki wtyczce 
-- SQLite Viewer; wystarczy kliknąć plik *.db.

-- Szybkie wykomentowanie tekstu: CTRL + /

CREATE TABLE users (
    idnum INTEGER NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    fullname TEXT,
    PRIMARY KEY (idnum)
    );

INSERT INTO users VALUES 
(10, 'jerry', 'fus!ll!', 'Jerry Seinfeld'),
(11, 'gcostanza', 'b0sc0', 'George Costanza'),
(12, 'newman', 'USMAIL', 'Newman')
;

-- sprawdzanie nazw tabel w bazie:
.tables
.schema

SELECT * FROM users;

SELECT username FROM users WHERE idnum > 10;

DELETE 
FROM users WHERE idnum = '10';

CREATE TABLE moms (
    username TEXT PRIMARY KEY NOT NULL,
    mother TEXT
);

INSERT INTO moms VALUES
('jerry','Helen Seinfeld'),
('gcostanza', 'Estelle Costanza'),
('kramer', 'Babs Kramer')
;

SELECT * FROM moms;

SELECT users.fullname, moms.mother 
FROM users JOIN moms 
ON users.username = moms.username;

UPDATE users SET idnum = 10 WHERE username = 'jerry';