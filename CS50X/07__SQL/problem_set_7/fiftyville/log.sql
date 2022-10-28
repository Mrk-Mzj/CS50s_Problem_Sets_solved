-- All you know is that the theft took place on 
-- July 28, 2021 and that it took place on 
-- Humphrey Street.

.schema

SELECT description FROM crime_scene_reports WHERE
street = "Humphrey Street" AND
year = 2021 AND
month = 7 AND
day = 28;
-- Theft of the CS50 duck took place 
-- at 10:15am at the Humphrey Street bakery. 
-- Interviews were conducted today with three witnesses 
-- who were present at the time – each of their interview 
-- transcripts mentions the bakery.

SELECT * FROM interviews WHERE
year = 2021 AND
month = 7 AND
day = 28 AND
transcript LIKE "%baker%";
-- Ruth - Sometime within ten minutes of the theft, 
-- I saw the thief get into a car in the bakery parking lot and drive away. 
-- If you have security footage from the bakery parking lot, you might want to look 
-- for cars that left the parking lot in that time frame.

-- Eugene - I don't know the thief's name, but it was someone I recognized. 
-- Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM 
-- on Leggett Street and saw the thief there withdrawing some money.

-- Raymond - As the thief was leaving the bakery, they called someone who talked to them 
-- for less than a minute. In the call, I heard the thief say that they were planning 
-- to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person 
-- on the other end of the phone to purchase the flight ticket.


-- Wskazówka Ruth:
SELECT * FROM bakery_security_logs WHERE 
year = 2021 AND month = 7 AND day = 28 AND hour = 10;
-- 10	23	exit	license_plate: 322W7JE
-- 10	23	exit	license_plate: 0NTHK55

SELECT * FROM people WHERE license_plate = "322W7JE" OR license_plate = "0NTHK55";
-- id	    name	phone_number	    passport_number	    license_plate
-- 514354	Diana	(770) 555-1861	    3592750733	        322W7JE
-- 560886	Kelsey	(499) 555-9472	    8294398571	        0NTHK55


-- Wskazówka Eugene:
SELECT * FROM atm_transactions WHERE atm_location = "Leggett Street" AND
transaction_type = "withdraw" AND
year = 2021 AND month = 7 AND day = 28; -- konta korzystające z bankomatu

SELECT person_id FROM bank_accounts WHERE account_number IN
(SELECT account_number FROM atm_transactions WHERE atm_location = "Leggett Street" AND
transaction_type = "withdraw" AND
year = 2021 AND month = 7 AND day = 28
); -- id korzystające z bankomatu

SELECT * FROM people WHERE id IN
(
    SELECT person_id FROM bank_accounts WHERE account_number IN
    (SELECT account_number FROM atm_transactions WHERE atm_location = "Leggett Street" AND
    transaction_type = "withdraw" AND
    year = 2021 AND month = 7 AND day = 28
    )
); -- osoby korzystające z bankomatu

-- ZŁODZIEJEM JEST DIANA, bo była w bankomacie i wyjechała ok. 10 min po kradzieży.
-- id	    name	phone_number	    passport_number	    license_plate
-- 514354	Diana	(770) 555-1861	    3592750733	        322W7JE


-- Wskazówka Raymonda:
SELECT * FROM phone_calls WHERE caller = "(770) 555-1861" AND
year = 2021 AND month = 7 AND day = 28 AND duration < 60; -- telefon rozmówcy złodziejki

SELECT * FROM people WHERE phone_number IN 
(SELECT receiver FROM phone_calls WHERE caller = "(770) 555-1861" AND
year = 2021 AND month = 7 AND day = 28 AND duration < 60
); -- dane rozmówcy złodziejki:

-- id	    name	phone_number	    passport_number	    license_plate
-- 847116	Philip	(725) 555-3243	    3391710505	        GW362R6

SELECT id, origin_airport_id, destination_airport_id, hour, minute FROM flights WHERE 
year = 2021 AND month = 7 AND day = 29 
AND origin_airport_id IN
(SELECT id FROM airports WHERE city = "Fiftyville"
) ORDER BY hour LIMIT 1; -- najwcześniejszy lot nazajutrz z Fiftyville:

-- id   origin_airport_id	destination_airport_id	    hour	minute
-- 36   8	                4	                        8	    20

SELECT * FROM passengers WHERE flight_id = 36 ORDER BY seat; -- paszporty pasażerów lotu

SELECT * FROM people WHERE passport_number IN 
(SELECT passport_number FROM passengers WHERE flight_id = 36
); -- nazwiska pasażerów lotu