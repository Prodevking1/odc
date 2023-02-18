CREATE TABLE
    public.items (
        prod_id SERIAL PRIMARY KEY NOT NULL,
        prod_name character varchar(50) NOT NULL,
        prod_price INTEGER NOT NULL
    )
CREATE TABLE
    public.customers (
        cust_id SERIAL PRIMARY KEY NOT NULL,
        cust_first_name character varchar(50) NOT NULL,
        cust_last_name character varchar(50) NOT NULL
    )
INSERT INTO
    items (prod_name, prod_price)
VALUES ('Small Desk', 100), ('Large desk', 300), ('Fan', 80);

INSERT INTO
    customers (
        cust_first_name,
        cust_last_name
    )
VALUES ('Greg', 'Jones'), ('Sandra', 'Jones'), ('Scott', 'Scott'), ('Trevor', 'Green'), ('Melanie', 'Johnson');

SELECT * FROM items;

SELECT * FROM items WHERE prod_price > 80;

SELECT * FROM items WHERE prod_price <= 300;

SELECT * FROM customers WHERE cust_last_name = 'Smith';

SELECT * FROM customers WHERE cust_last_name = 'Jones';

SELECT * FROM customers WHERE cust_first_name != 'Scott';