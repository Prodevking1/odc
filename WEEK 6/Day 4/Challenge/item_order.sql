CREATE TABLE customer (
    id SERIAL NOT NULL,
    name VARCHAR(30),
    creat_date DATETIME NOT NULL DEFAULT GETDATE(),
    PRIMARY KEY (id),
);

INSERT INTO customer (name) VALUES
    ('Adam'),
    ('Betsalel'),
    ('Cohen'),
    ('David'),
    ('Eve');

CREATE TABLE orders (
    id SERIAL NOT NULL,
    ord_date DATE DEFAULT '2021-05-10',
    cust_id INTEGER NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (cust_id) REFERENCES customer (id) ON DELETE CASCADE
);

INSERT INTO orders (cust_id) VALUES
    (1),
    (2),
    (1),
    (1),
    (2),
    (2);

CREATE TABLE item (
    id SERIAL NOT NULL,
    label VARCHAR(30),
    price INTEGER DEFAULT 0,
    ord_id INTEGER NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (ord_id) REFERENCES orders (id) ON DELETE CASCADE
);

INSERT INTO item (label, price, ord_id) VALUES
    ('Tomato', 5, 1),
    ('Cucumber', 6, 1),
    ('Carrot', 3, 1),
    ('Grape', 10, 1),
    ('Tomato', 4, 2),
    ('Banana', 7, 2);

--  RETURN TOTAL PRICE OF ORDERS
SELECT o.id AS Order, ord_date, c.name AS Date, SUM(price) AS "Total price" FROM item i
INNER JOIN orders o ON o.id = i.ord_id
INNER JOIN customer c ON c.id = o.cust_id
GROUP BY o.id, ord_date, c.name
ORDER BY o.id;