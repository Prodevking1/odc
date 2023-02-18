SELECT * FROM customers;
SELECT * FROM items ORDER BY prod_price;
SELECT * FROM items WHERE prod_price >= 80 ORDER BY prod_price DESC;
SELECT * FROM items WHERE prod_price >= 80 ORDER BY prod_price DESC;
SELECT cust_first_name, cust_last_name FROM customers ORDER BY cust_last_name LIMIT 3;
SELECT cust_last_name FROM customers ORDER BY cust_last_name DESC;
CREATE TABLE purchases(
purch_id SERIAL,
cust_id INTEGER,
prod_id INTEGER,
PRIMARY KEY (purch_id),
FOREIGN KEY (cust_id) REFERENCES customers (cust_id),
FOREIGN KEY (prod_id) REFERENCES items (prod_id)
);
INSERT INTO purchases (cust_id) VALUES (1);
SELECT * FROM purchases;
INSERT INTO purchases (cust_id, prod_id) VALUES 
(1, 1),
(1, 2),
(2, 1),
(2, 2),
(2, 3),
(1, 2),
(3, 2);
INSERT INTO purchases (cust_id, prod_id) VALUES (4, 1);
SELECT * FROM purchases;
SELECT *
FROM purchases
INNER JOIN customers
ON purchases.cust_id = customers.cust_id;
SELECT *
FROM purchases
INNER JOIN customers
ON purchases.cust_id = customers.cust_id
WHERE purchases.cust_id = 4;
SELECT * FROM customers;
SELECT * FROM items;
SELECT purch_id, cust_last_name, prod_name
FROM purchases
INNER JOIN customers
ON purchases.cust_id = customers.cust_id
INNER JOIN items
ON purchases.prod_id = items.prod_id
WHERE purchases.prod_id IN (1,2);
INSERT INTO items (prod_name, prod_price) VALUES ('Hard drive', 90); 
INSERT INTO purchases (cust_id, prod_id) VALUES (3,4);
SELECT cust_first_name, cust_last_name, prod_name 
FROM purchases 
INNER JOIN customers
ON purchases.cust_id = customers.cust_id
INNER JOIN items
ON purchases.prod_id = items.prod_id
GROUP BY cust_first_name, cust_last_name, prod_name;