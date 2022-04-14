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
order_id INT AUTO_INCREMENT,
time_of_sale DATE,
customer_id INT,
PRIMARY KEY (order_id),
FOREIGN KEY (customer_id) REFERENCES customer(customer_id));

CREATE TABLE order_details(
order_detail_id INT AUTO_INCREMENT,
order_id INT NOT NULL,
product_id INT NOT NULL,
quantity INT,
PRIMARY KEY (order_detail_id, order_id),
FOREIGN KEY (order_id) REFERENCES orders(order_id),
FOREIGN KEY (product_id) REFERENCES products(product_id));

CREATE TABLE invoice(
invoice_id INT NOT NULL AUTO_INCREMENT,
order_id INT NOT NULL,
time_of_sale DATE,
customer_id INT,
PRIMARY KEY (invoice_id, order_id),
FOREIGN KEY (customer_id) REFERENCES orders(customer_id),
FOREIGN KEY (order_id) REFERENCES orders(order_id));

/* KEEP THIS WE NEED THIS */
select invoice.order_id, orders.customer_id, invoice.time_of_sale, order_details.product_id, order_details.quantity
from invoice
inner join order_details
	on invoice.order_id = order_details.order_id
inner join orders
	on invoice.customer_id = orders.customer_id;

select customer.customer_id, customer.cust_name
from customer
inner join invoice
 on customer.customer_id = invoice.customer_id
where invoice.customer_id = 3;
/* KEEP THIS WE NEED THIS */


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
INSERT INTO generic_vehicle_merchant.customer (cust_name, cust_email, cust_address, cust_phone, cust_license)
VALUES ('billy jean', 'bjillaf11@gnmail.com', '155 ocol', 1441556, 111111);
select * from customer;

INSERT INTO store(user_name, u_password)
VALUES ("administrator", "gvmadmin2022");
select * from store;

INSERT INTO vendor(vendor_name, vendor_email, vendor_phone)
VALUES ("Auto-Parts Incorporated", "management@autoparts.inc", 13444777);
INSERT INTO vendor(vendor_name, vendor_email, vendor_phone)
VALUES ("Bord Vehicles", "gregmerc@bordvehicles.com", 14764331);
select * from vendor;

INSERT INTO products(product_name, vehicle, cost, vendor_id, quantity)
VALUES ("bord_t502", "Bord T502", 65000.00, 2, 5);
INSERT INTO products(product_name, vehicle, cost, vendor_id, quantity)
VALUES ("bord_t501", "Bord T501", 48000.00, 2, 5);
INSERT INTO products(product_name, vehicle, cost, vendor_id, quantity)
VALUES ("bord_t1100", "Bord T1101", 83500.00, 2, 5);
INSERT INTO products(product_name, vehicle, cost, vendor_id, quantity)
VALUES ("bord_t1100_engine", "BT1101 Engine", 2400.00, 2, 5);
INSERT INTO products(product_name, vehicle, cost, vendor_id, quantity)
VALUES ("auto_tire01", "TruckWinterTire", 700.00, 1, 5);
INSERT INTO products(product_name, vehicle, cost, vendor_id, quantity)
VALUES ("auto_tire02", "TruckSummerTire", 550.00, 1, 5);
INSERT INTO products(product_name, vehicle, cost, vendor_id, quantity)
VALUES ("auto_tire03", "CarWinterTire", 610.00, 1, 5);
INSERT INTO products(product_name, vehicle, cost, vendor_id, quantity)
VALUES ("auto_air_pump", "WheelPump", 75.00, 1, 5);
select * from products;

insert into orders(time_of_sale, customer_id)
values ("2022-01-03", 1);
insert into orders(time_of_sale, customer_id)
values ("2022-02-08", 2);
insert into orders(time_of_sale, customer_id)
values ("2022-02-09", 3);
insert into orders(time_of_sale, customer_id)
values ("2022-02-13", 4);
insert into orders(time_of_sale, customer_id)
values ("2022-01-03", 5);
select * from orders;

insert into order_details(order_id, product_id, quantity)
values (1, 3, 2);
insert into order_details(order_id, product_id, quantity)
values (1, 4, 3);
insert into order_details(order_id, product_id, quantity)
values (2, 1, 3);
insert into order_details(order_id, product_id, quantity)
values (2, 2, 4);
insert into order_details(order_id, product_id, quantity)
values (3, 2, 4);
insert into order_details(order_id, product_id, quantity)
values (4, 3, 1);
insert into order_details(order_id, product_id, quantity)
values (5, 7, 1);
insert into order_details(order_id, product_id, quantity)
values (5, 8, 1);
insert into order_details(order_id, product_id, quantity)
values (5, 6, 1);
insert into order_details(order_id, product_id, quantity)
values (5, 5, 2);
select * from order_details;

insert into invoice(order_id, time_of_sale, customer_id)
values (1, "2022-04-03", 1);
insert into invoice(order_id, time_of_sale, customer_id)
values (2, "2022-04-12", 2);
insert into invoice(order_id, time_of_sale, customer_id)
values (3, "2022-04-13", 3);
insert into invoice(order_id, time_of_sale, customer_id)
values (4, "2022-04-18", 4);
insert into invoice(order_id, time_of_sale, customer_id)
values (5, "2022-01-03", 5);
select * from invoice;

SELECT * FROM generic_vehicle_merchant.products
WHERE quantity = 10;

SELECT  DATE_FORMAT(time_of_sale, '%m/%d/%Y')
FROM    invoice
WHERE   time_of_sale BETWEEN NOW() - INTERVAL 31 DAY AND NOW();

select invoice.invoice_id, invoice.time_of_sale, invoice.customer_id, order_details.product_id, order_details.quantity
                                    from invoice inner join order_details
                                    on invoice.order_id = order_details.order_id
                                    where order_details.order_id = 1;

select * from invoice where invoice_id = 2;
select * from order_details where order_id = 2;

select cust_name from customer where customer_id = 1;
