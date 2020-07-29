DROP DATABASE IF EXISTS db_proj;

CREATE DATABASE db_proj;

USE db_proj;

DROP TABLE IF EXISTS contact_table;
CREATE TABLE contact_table(
Contact_id INT,
Fname VARCHAR(210),
Mname VARCHAR(210),
Lname VARCHAR(210),
PRIMARY KEY(Contact_id));

DROP TABLE IF EXISTS address_table;
CREATE TABLE address_table(
Address_id INT AUTO_INCREMENT,
Contact_id INT,
Address_type VARCHAR(100),
Address VARCHAR(100),
City VARCHAR(100),
State VARCHAR(100),
Zip VARCHAR(100),
PRIMARY KEY(Address_id),
FOREIGN KEY(Contact_id) REFERENCES contact_table(Contact_id));

DROP TABLE IF EXISTS phone_table;
CREATE TABLE phone_table(
Phone_id INT AUTO_INCREMENT,
Contact_id INT,
Phone_type VARCHAR(100),
Area_code VARCHAR(100),
NUMBER VARCHAR(100),
PRIMARY KEY(phone_id),
FOREIGN KEY(Contact_id) REFERENCES contact_table(Contact_id));

DROP TABLE IF EXISTS date_table;
CREATE TABLE date_table(
Date_id INT AUTO_INCREMENT,
Contact_id INT,
Date_type VARCHAR(30),
Date VARCHAR(200),
PRIMARY KEY(Date_id),
FOREIGN KEY(Contact_id) REFERENCES contact_table(Contact_id));
