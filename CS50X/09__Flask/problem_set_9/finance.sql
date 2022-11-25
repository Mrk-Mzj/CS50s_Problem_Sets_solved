
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
    when_did    TEXT NOT NULL,
    person_id   INTEGER NOT NULL,
    did_what    TEXT NOT NULL,
    how_many    INTEGER NOT NULL,
    for_price   NUMERIC NOT NULL,
    of_company     TEXT NOT NULL,
    PRIMARY KEY (when_did),
    FOREIGN KEY (person_id) REFERENCES users(id)
);
CREATE INDEX searchable ON purchases (person_id, did_what, how_many, for_price, of_company);


CREATE TABLE ownership (
    person_id   INTEGER NOT NULL,
    how_many    INTEGER NOT NULL,
    of_company     TEXT NOT NULL,
    FOREIGN KEY (person_id) REFERENCES users(id)
);
CREATE INDEX searchable_ownership ON ownership (person_id, of_company);


INSERT INTO ownership (person_id, how_many, of_company) VALUES (1, 112.24,  'META');
INSERT INTO ownership (person_id, how_many, of_company) VALUES (1, 583,     'NFLX');
INSERT INTO ownership (person_id, how_many, of_company) VALUES (1, 453.21,  'AAPL');
INSERT INTO ownership (person_id, how_many, of_company) VALUES (2, 549.6,   'TSLA');
INSERT INTO ownership (person_id, how_many, of_company) VALUES (2, 197.64,  'GOOG');
INSERT INTO ownership (person_id, how_many, of_company) VALUES (3, 470.65,  'AMZN');


.schema;
SELECT * FROM purchases;


-- TEMP:
-- pobieram wartość:
SELECT how_many FROM ownership WHERE person_id=1 AND of_company='AAPL';
-- nastpnie zmieniam ją w kodzie i updejtuję:
UPDATE ownership SET how_many=453.21 WHERE person_id=1 AND of_company='AAPL';


-- W RAZIE PROBLEMÓW:
-- DROP TABLE purchases;
