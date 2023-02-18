-- 1.

CREATE TABLE student (
    id SERIAL NOT NULL,
    lname CHAR(30) NOT NULL,
    fname CHAR(30) NOT NULL,
    birthdate DATE NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO student (lname, fname, birthdate) VALUES
    ('Alex', 'Angstrom', '2001-10-20'),
    ('Bess', 'Bizmuth', '2002-11-21'),
    ('Carla', 'Curie', '2001-12-22'),
    ('Driss', 'Dalton', '2001-01-31'),
    ('Emma', 'Einstein', '2002-02-22');

CREATE TABLE subject (
    id SERIAL NOT NULL,
    name CHAR(30) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO subject (name) VALUES
    ('Mathematics'),
    ('Physics'),
    ('Litterature'),
    ('Philosophy'),
    ('Linguistic'),
    ('Arts'),
    ('Law'),
    ('Biology'),
    ('Medicine'),
    ('Computing'),
    ('Architecture');

CREATE TABLE grade (
    id SERIAL NOT NULL,
    exam_date DATE NOT NULL,
    student_id SMALLINT,
    subject_id SMALLINT,
    score SMALLINT,
    CHECK (score >= 0 AND score <= 100),
    PRIMARY KEY (id),
    FOREIGN KEY (student_id) REFERENCES student (id) ON DELETE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subject (id) ON DELETE CASCADE
);

INSERT INTO grade (exam_date, student_id, subject_id, score) VALUES
    ('2021-06-16', 1, 1, 80),
    ('2021-05-15', 1, 2, 85),
    ('2021-06-16', 2, 1, 60),
    ('2021-05-15', 3, 2, 77),
    ('2021-07-17', 4, 7, 68),
    ('2021-08-18', 4, 8, 88);

-- 2.
SELECT s.lname, s.fname, s.birthdate, su.name, g.exam_date, g.score FROM grade g
INNER JOIN student s ON s.id = g.student_id
INNER JOIN subject su ON su.id = g.subject_id;

-- Display all students including those without grades and all subjects including those without grades:
SELECT s.lname, s.fname, s.birthdate, su.name, g.exam_date, g.score FROM grade g
FULL JOIN student s ON s.id = g.student_id
FULL JOIN subject su ON su.id = g.subject_id;

-- Display students who have no grades:
SELECT s.lname, s.fname, s.birthdate  FROM student s
LEFT JOIN grade g ON s.id = g.student_id
WHERE g.student_id IS NULL;

-- Display unused subjects:
SELECT su.name FROM subject su
LEFT JOIN grade g ON su.id = g.subject_id
WHERE g.subject_id IS NULL;

-- Display average score by subject:
SELECT su.name AS subject, round(avg(g.score)) AS avg_score FROM subject su
INNER JOIN grade g ON g.subject_id = su.id
GROUP BY su.name;