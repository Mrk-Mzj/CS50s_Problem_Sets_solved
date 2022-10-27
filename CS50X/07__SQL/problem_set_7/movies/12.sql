-- write a SQL query to list the titles of all movies 
-- in which both Johnny Depp and Helena Bonham Carter starred


--  0,2s
-- wersja najszybsza: przekazuje sobie obiekty w nawiasach:

.timer on
SELECT title FROM movies WHERE id IN
  (SELECT movie_id FROM stars WHERE person_id =
    (SELECT id FROM people WHERE name = "Johnny Depp")
  )
AND title IN
(SELECT title FROM movies WHERE id IN
  (SELECT movie_id FROM stars WHERE person_id =
    (SELECT id FROM people WHERE name = "Helena Bonham Carter")
  )
);

-- 7,5s
-- niżej dwie równie wolne wersje, 
-- różnią się zapisem, ale obie tworzą wielką tablicę w której muszą szukać:

.timer on
SELECT title 
FROM movies, stars, people 
WHERE movies.id = stars.movie_id
AND stars.person_id = people.id
AND people.name = "Johnny Depp"
AND title IN
(SELECT movies.title
FROM movies
JOIN stars ON movies.id = stars.movie_id
JOIN people ON stars.person_id = people.id
WHERE name = "Helena Bonham Carter");

.timer on
SELECT title
FROM movies 
JOIN stars ON movies.id = stars.movie_id
JOIN people ON stars.person_id = people.id
WHERE name = "Johnny Depp" 
AND title IN
(SELECT movies.title
FROM movies
JOIN stars ON movies.id = stars.movie_id
JOIN people ON stars.person_id = people.id
WHERE name = "Helena Bonham Carter");

-- 12s
-- Niżej podobna wersja, ale jeszcze wolniejsza. 
-- Poprzednia zapewne użyła dużej tablicy ponownie.
-- Ta składa dużą + średnią, co trwa najdłużej:

.timer on
SELECT title
FROM movies 
JOIN stars ON movies.id = stars.movie_id
JOIN people ON stars.person_id = people.id
WHERE name = "Johnny Depp" 
AND stars.movie_id IN
(SELECT stars.movie_id
FROM stars
JOIN people ON stars.person_id = people.id
WHERE name = "Helena Bonham Carter");