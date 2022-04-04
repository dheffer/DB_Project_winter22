create database generic_vehicle_merchant;
use generic_vehicle_merchant;

CREATE TABLE store(
user_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
user_name CHAR (8) NOT NULL,
u_password VARCHAR (30));

CREATE TABLE customer(
customer_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
cust_name VARCHAR (30),
cust_email VARCHAR (50),
cust_address VARCHAR (30) NULL,
cust_phone CHAR(11) NOT NULL,
cust_license INT NULL);

CREATE TABLE vendor(
vendor_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
vendor_name VARCHAR(30) NOT NULL,
vendor_email VARCHAR(50),
vendor_phone CHAR(11) NOT NULL);

CREATE TABLE products(
product_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
product_name VARCHAR(30) NOT NULL,
vehicle VARCHAR(20),
cost FLOAT NOT NULL,
vendor_id INT,
quantity INT,
FOREIGN KEY (vendor_id) REFERENCES vendor(vendor_id));

CREATE TABLE orders(
order_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
quantity INT,
customer_id INT,
product_id INT,
FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
FOREIGN KEY (product_id) REFERENCES products(product_id));

CREATE TABLE invoice(
invoice_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
quantity INT,
time_of_sale DATE,
product_id INT,
customer_id INT,
FOREIGN KEY (product_id) REFERENCES products(product_id),
FOREIGN KEY (customer_id) REFERENCES customer(customer_id));

/* above is adding the tables to the database */
/* below is adding data to the tables */

INSERT INTO customer(cust_name, cust_email, cust_address, cust_phone, cust_license)
VALUES ("Fred Johnson", "fjohn@hotmail.com", "17 Ridgeway Crescent", 18776434994, 159667414);
INSERT INTO customer(cust_name, cust_email, cust_address, cust_phone, cust_license)
VALUES ("Margaret Pattinson", "margpatt@gmail.com", "74 Longjohn Street", 18776588144, 160647681);
INSERT INTO customer(cust_name, cust_email, cust_address, cust_phone, cust_license)
VALUES ("Billy Formean", "billybob123@gmail.com", "2 Sanji Avenue", 15442788333, 355548641);
INSERT INTO customer(cust_name, cust_email, cust_address, cust_phone, cust_license)
VALUES ("Jane Way", "thejaneway@houtlook.ca", "55 Striker Crescent", 12555988447, 31146686);

INSERT INTO store(user_name, u_password)
VALUES ("AA0001", "greghard0001");

INSERT INTO vendor(vendor_name, vendor_email, vendor_phone)
VALUES ("Auto-Parts Incorporated", "management@autoparts.inc", 13444777443);
INSERT INTO vendor(vendor_name, vendor_email, vendor_phone)
VALUES ("Bord Vehicles", "gregmerc@bordvehicles.com", 14764331555);

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

