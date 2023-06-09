-- write a SQL query to list the
-- titles of the five highest rated movies (in order) 
-- that Chadwick Boseman starred in, starting with the highest rated.

SELECT title FROM movies WHERE id IN 
(SELECT movie_id FROM stars WHERE person_id = 
(SELECT id FROM people WHERE name = 'Chadwick Boseman'));

-- Chadwick Boseman id: 1569276

SELECT title, rating FROM movies, ratings 
WHERE movies.id = ratings.movie_id 
AND id IN 
(SELECT movie_id FROM stars WHERE person_id = 
 (SELECT id FROM people WHERE name = 'Chadwick Boseman')
) ORDER BY rating DESC
LIMIT 5;