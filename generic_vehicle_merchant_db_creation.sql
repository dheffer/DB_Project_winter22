create database generic_vehicle_merchant;
use generic_vehicle_merchant;

CREATE TABLE store(
user_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
user_name CHAR (8) NOT NULL,
u_password VARCHAR (30));

CREATE TABLE customer(
customer_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
cust_name VARCHAR(30),
cust_email LONGTEXT,
cust_address LONGTEXT NULL,
cust_phone INT NOT NULL CHECK(cust_phone between 0 and 9999999999),
cust_license INT);

CREATE TABLE vendor(
vendor_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
vendor_name VARCHAR(30) NOT NULL,
vendor_email LONGTEXT,
vendor_phone INT NOT NULL);

CREATE TABLE products(
product_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
product_name VARCHAR(30) NOT NULL,
vehicle VARCHAR(20),
cost FLOAT NOT NULL,
vendor_id INT,
quantity INT,
FOREIGN KEY (vendor_id) REFERENCES vendor(vendor_id));

CREATE TABLE orders(
order_id INT NOT NULL PRIMARY KEY,
quantity INT,
customer_id INT,
product_id INT,
FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
FOREIGN KEY (product_id) REFERENCES products(product_id));

CREATE TABLE invoice(
invoice_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
order_id INT NOT NULL,
time_of_sale DATE,
customer_id INT,
FOREIGN KEY (order_id) REFERENCES orders(order_id),
FOREIGN KEY (customer_id) REFERENCES customer(customer_id));

/* above is adding the tables to the database */
/* below is adding data to the tables */

INSERT INTO customer(cust_name, cust_email, cust_address, cust_phone, cust_license)
VALUES ("Fred Johnson", "fjohn@hotmail.com", "17 Ridgeway Crescent", 1877643499, 159667414);
INSERT INTO customer(cust_name, cust_email, cust_address, cust_phone, cust_license)
VALUES ("Margaret Pattinson", "margpatt@gmail.com", "74 Longjohn Street", 18776588, 160647681);
INSERT INTO customer(cust_name, cust_email, cust_address, cust_phone, cust_license)
VALUES ("Billy Formean", "billybob123@gmail.com", "2 Sanji Avenue", 15442788, 355548641);
INSERT INTO customer(cust_name, cust_email, cust_address, cust_phone, cust_license)
VALUES ("Jane Way", "thejaneway@houtlook.ca", "55 Striker Crescent", 12555988, 31146686);

INSERT INTO store(user_name, u_password)
VALUES ("AA0001", "greghard0001");

INSERT INTO vendor(vendor_name, vendor_email, vendor_phone)
VALUES ("Auto-Parts Incorporated", "management@autoparts.inc", 13444777);
INSERT INTO vendor(vendor_name, vendor_email, vendor_phone)
VALUES ("Bord Vehicles", "gregmerc@bordvehicles.com", 14764331);

INSERT INTO products(product_name, vehicle, cost, vendor_id, quantity)
VALUES ("bord_t502", "Bord T502", 65000.00, 2, 10);
INSERT INTO products(product_name, vehicle, cost, vendor_id, quantity)
VALUES ("bord_t501", "Bord T501", 48000.00, 2, 10);
INSERT INTO products(product_name, vehicle, cost, vendor_id, quantity)
VALUES ("bord_t1100", "Bord T1101", 83500.00, 2, 10);
INSERT INTO products(product_name, vehicle, cost, vendor_id, quantity)
VALUES ("bord_t1100_engine", "BT1101 Engine", 2400.00, 2, 10);
INSERT INTO products(product_name, vehicle, cost, vendor_id, quantity)
VALUES ("auto_tire01", "TruckWinterTire", 700.00, 1, 10);
INSERT INTO products(product_name, vehicle, cost, vendor_id, quantity)
VALUES ("auto_tire02", "TruckSummerTire", 550.00, 1, 10);
INSERT INTO products(product_name, vehicle, cost, vendor_id, quantity)
VALUES ("auto_tire03", "CarWinterTire", 610.00, 1, 10);
INSERT INTO products(product_name, vehicle, cost, vendor_id, quantity)
VALUES ("auto_air_pump", "WheelPump", 75.00, 1, 10);

select * from customer;
select * from store;
select * from vendor;
select * from products;

INSERT INTO generic_vehicle_merchant.customer (cust_name, cust_email, cust_address, cust_phone, cust_license)
VALUES ('billy jean', 'bjillaf11@gnmail.com', '155 ocol', 1441556, 111111);

SELECT * FROM generic_vehicle_merchant.products
WHERE quantity = 10;

insert into invoice (invoice_id, order_id, time_of_sale, customer_id)
values (1, 1, "2022-04-07", 1);
insert into invoice (invoice_id, order_id, time_of_sale, customer_id)
values (2, 2, "2022-03-29", 2);
insert into invoice (invoice_id, order_id, time_of_sale, customer_id)
values (3, 3, "2022-03-20", 3);
insert into invoice (invoice_id, order_id, time_of_sale, customer_id)
values (4, 4, "2022-03-11", 4);
insert into invoice (invoice_id, order_id, time_of_sale, customer_id)
values (5, 5, "2022-03-02", 5);
insert into invoice (invoice_id, order_id, time_of_sale, customer_id)
values (6, 6, "2022-02-25", 6);
insert into invoice (invoice_id, order_id, time_of_sale, customer_id)
values (7, 7, "2022-02-17", 7);
insert into invoice (invoice_id, order_id, time_of_sale, customer_id)
values (8, 8, "2022-04-01", 8);

select * from invoice;

SELECT  DATE_FORMAT(time_of_sale, '%m/%d/%Y')
FROM    invoice
WHERE   time_of_sale BETWEEN NOW() - INTERVAL 31 DAY AND NOW();

select order_id, quantity, customer_id, product_id from orders;

insert into orders(order_id, quantity, customer_id, product_id)
values (1, 5, 2, 4);
insert into orders(order_id, quantity, customer_id, product_id)
values (2, 1, 2, 2);
insert into orders(order_id, quantity, customer_id, product_id)
values (3, 2, 2, 3);
insert into orders(order_id, quantity, customer_id, product_id)
values (4, 1, 4, 7);
insert into orders(order_id, quantity, customer_id, product_id)
values (5, 4, 4, 1);

select * from invoice;
