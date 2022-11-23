
-- Tak stworzono oryginalną tabelę do kursu:

-- CREATE TABLE users (
--     id          INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL  
--     username    TEXT NOT NULL  
--     hash        TEXT NOT NULL  
--     cash        NUMERIC NOT NULL DEFAULT 10000.00);
-- CREATE TABLE sqlite_sequence(name seq);
-- CREATE UNIQUE INDEX username ON users (username);

-- Stworzenie unikalnego indeksu dla kolumny username w tabeli users
-- posłużyło autorom do zagwarantowania integralności dancyh; 
-- Tu nawet baza danych troszczy się o brak powtarzających się loginów.

-- Indeksowanie dzieje się automatycznie dla kolumn Primary Key
-- ale trzeba je zrobić ręcznie w kolumnie Foreign Key 


-- TWORZĘ TABELĘ:

CREATE TABLE purchases (
    when_did    NUMERIC NOT NULL,
    person_id   INTEGER NOT NULL,
    did_what    TEXT NOT NULL,
    how_many    INTEGER NOT NULL,
    for_price   NUMERIC NOT NULL,
    of_company     TEXT NOT NULL,
    PRIMARY KEY (when_did),
    FOREIGN KEY (person_id) REFERENCES users(id)
);
CREATE UNIQUE INDEX person_id ON purchases (person_id);
CREATE INDEX searchable ON purchases (did_what, how_many, for_price, of_company);

.schema;
SELECT * FROM purchases;


-- W RAZIE PROBLEMÓW:
-- DROP TABLE purchases;
