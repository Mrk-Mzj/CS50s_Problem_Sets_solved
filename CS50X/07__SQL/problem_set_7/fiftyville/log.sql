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

SELECT * FROM bakery_security_logs WHERE 
year = 2021 AND
month = 7 AND
day = 28 AND
hour = 10
-- XX:XX  exit	license_plate: XXX

SELECT * FROM people WHERE license_plate = "XXX"
-- id	    name	 phone_number	 passport_number  license_plate
