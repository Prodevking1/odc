-- *** EXERCISE 1 ***
--1.
SELECT DISTINCT language.name
FROM film
INNER JOIN language
ON film.language_id = language.language_id;

SELECT title FROM film WHERE language_id IN (2,3,4,5,6);

--2.
SELECT title, description, name
FROM film
INNER JOIN language
ON film.language_id = language.language_id
ORDER BY title LIMIT 50;

SELECT title, description, name
FROM film
FULL JOIN language
ON film.language_id = language.language_id
ORDER BY name;

SELECT title FROM film WHERE language_id != 1;

--3. 
CREATE TABLE new_film (
    id SERIAL,
    name VARCHAR(30),
    PRIMARY KEY (id)
);

INSERT INTO new_film (name)
VALUES ('Rambo 15'), ('Rambo 16'), ('Star Wars 28');

--4.
DROP TABLE IF EXISTS customer_review;
CREATE TABLE customer_review (
    review_id SERIAL NOT NULL,
    film_id  SMALLINT NOT NULL,
    language_id SMALLINT,
    title CHAR(30),
    score SMALLINT,
    CHECK (score > 0 AND score < 11),
    review_text TEXT,
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (review_id),
    FOREIGN KEY (film_id) REFERENCES new_film (id) ON DELETE CASCADE,
    FOREIGN KEY (language_id) REFERENCES language (language_id)
);

INSERT INTO customer_review (film_id, language_id, title, score, review_text) 
VALUES 
(1,3,'A truly moving film', 10, 'What an amazing film. Such a delicate touch.' ),
(2,3,'Crap',1, 'Not worth the time.');

SELECT * FROM customer_review;

--5.
INSERT INTO new_film (id, name)
VALUES (2, 'Rambo 16');

UPDATE customer_review SET film_id = 2 WHERE review_id =2;

DELETE FROM new_film WHERE id = 2;
SELECT * FROM new_film;
SELECT * FROM customer_review;

--*** EXERCISE 2 ***
--1.
UPDATE film SET language_id = 2 WHERE film_id BETWEEN 20 AND 29;
UPDATE film SET language_id = 3 WHERE film_id BETWEEN 30 AND 39;
UPDATE film SET language_id = 4 WHERE film_id BETWEEN 40 AND 49;
SELECT film_id, title, language_id FROM film ORDER BY film_id OFFSET 15 LIMIT 50;

--2.
address_id is the foreign key. Address should be created first in the address table and then referred to in the customer table using the address_key column.

--3.
DROP TABLE IF EXISTS customer_review;

--4. 
SELECT title FROM film LEFT JOIN inventory ON film.film_id = inventory.film_id WHERE inventory.inventory_id IS NULL ORDER BY title;
SELECT * FROM film WHERE title = 'Alice Fantasia';
SELECT * FROM inventory WHERE film_id = 14;

--5.
SELECT title, rental_rate FROM film LEFT JOIN inventory ON film.film_id = inventory.film_id WHERE inventory.inventory_id IS NULL ORDER BY rental_rate DESC LIMIT 30;

--6.1.
SELECT DISTINCT title FROM film f
INNER JOIN film_actor fa ON fa.film_id = f.film_id
INNER JOIN actor a ON a.actor_id = fa.actor_id
WHERE description ILIKE '% sumo %' AND last_name ='Monroe' AND first_name='Penelope'; -> Park Citizen

--6.2.
SELECT title, description, length, rating  FROM film WHERE description ILIKE '%documentary%' AND length < 60 AND rating = 'R'; --> Crossing Divorce

--6.3.
SELECT title, (return_date - rental_date) AS effective_duration, rental_duration, rental_rate FROM rental r
INNER JOIN inventory i ON i.inventory_id = r.inventory_id
INNER JOIN customer c ON c.customer_id = r.customer_id
INNER JOIN film f ON f.film_id = i.film_id
WHERE first_name='Matthew' AND last_name='Mahan' AND return_date > '2005-07-27' AND return_date < '2005-08-02';
-- -> No film seems to match the criterias

--6.4
SELECT title, description, replacement_cost from rental r
INNER JOIN inventory i ON i.inventory_id = r.inventory_id
INNER JOIN customer c ON c.customer_id = r.customer_id
INNER JOIN film f ON f.film_id = i.film_id
WHERE first_name='Matthew' AND last_name='Mahan' AND (title ILIKE '%boat%' OR description ILIKE '%boat%')
ORDER BY replacement_cost DESC
LIMIT 1 ; --> Stone Fire