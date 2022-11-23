
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

.schema;
SELECT * FROM purchases;


-- W RAZIE PROBLEMÓW:
-- DROP TABLE purchases;
