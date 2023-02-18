CREATE TABLE students
(
id SERIAL PRIMARY KEY NOT NULL,
first_name character varchar(50) NOT NULL,
last_name character varchar(50) NOT NULL,
birth_date DATE NOT NULL
)
INSERT INTO students (first_name, last_name, birth_date)
VALUES
('Marc','Benichou', TO_DATE('02/11/1998','DD/MM/YYYY')),
('Yoan','Cohen', TO_DATE('03/12/2010','DD/MM/YYYY')),
('Lea','Benichou', TO_DATE('27/07/1987','DD/MM/YYYY')),
('Amelia','Dux', TO_DATE('07/04/1996','DD/MM/YYYY')),
('David','Grez', TO_DATE('14/06/2003','DD/MM/YYYY')),
('Omer','Simpson', TO_DATE('03/10/1980','DD/MM/YYYY'));

INSERT INTO students (first_name, last_name, birth_date)
VALUES ('Lien' , 'Duong', '1965-08-13');

SELECT * FROM students;
SELECT * FROM students WHERE last_name = 'Benichou' AND first_name = 'Marc';
SELECT * FROM students WHERE last_name = 'Benichou' OR first_name = 'Marc';
SELECT * FROM students WHERE first_name LIKE '%a%';
SELECT * FROM students WHERE first_name ILIKE 'a%';
SELECT * FROM students WHERE first_name ILIKE '%a';
SELECT * FROM students WHERE first_name ILIKE '%a_';
SELECT * FROM students WHERE id IN (1,3);
SELECT * FROM students WHERE birth_date > '2000-01-01';