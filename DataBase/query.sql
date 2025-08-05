-- comment

/* multi
line comment
*/

SHOW DATABASES;
CREATE DATABASE python_june; 
USE python_june;
SHOW TABLES;
DROP DATABASE python_june;
CREATE TABLE student (Id int,Name varchar(20),Place varchar(20));
DROP TABLE student;
SELECT id,name from student;
SELECT * FROM student;


INSERT INTO student VALUES (3,"Jafar","Malappuram");
INSERT INTO student (id,name) VALUES (2,"Manu");
SELECT * FROM student WHERE id=2;

USE python_june;
DELETE FROM student WHERE id=3;
SELECT * FROM student;

UPDATE student SET place = "Idukki" WHERE id = 3;  /* WHERE is manditory, else everything will be updated. */

/* ALTER */

/* ALTER TABLE tablename ADD/MODIFY/DROP cols */

ALTER TABLE student ADD email varchar(20);
SHOW COLUMNS FROM student;

/* bigint */

ALTER TABLE student ADD phone int;
UPDATE student SET phone=9999999999 WHERE id = 1; /* in int datat type max value 2147483647  for change use bigint */

ALTER TABLE student MODIFY phone bigint;

ALTER TABLE student DROP email;

/* ALTER TABLE tablename RENAME TO newname; */   /* TO RENAME A TABLE */

ALTER TABLE student RENAME TO python;
ALTER TABLE python RENAME TO student;

/* ALTER TABLE tablename CHANGE COLUMN oldcolm newcolumn datatype; */  /* To change COLUM NMAE */

ALTER TABLE student CHANGE COLUMN phone phone_no bigint;  

/* DEfault column value */

ALTER TABLE student ALTER COLUMN place SET DEFAULT " CALICUT "; /* settting default value */

INSERT INTO studen VALUES(5,"Mathyu"); /* there will be error because 3 field must be there - missing one */
INSERT INTO student (id,name) VALUES (4,"Mathyu"); /* not mentioned place but by default calicut is set */

/* SQL CONSTRAINS 

NOT NULL
UNIQUE
AUTO_INCREMENT
CHECK( condition )
DEFAULT "value"
PRIMARY KEY
FOREIGN KEY
*/

CREATE TABLE employee (
emp_id INT NOT NULL UNIQUE ,
employee_name VARCHAR(20) NOT NULL ,
age INT CHECK(age>=18) ,
state VARCHAR(20) DEFAULT "Kerala"
);

SELECT * FROM employee;
INSERT INTO employee ( emp_id,employee_name,age ) VALUES ( 1,"Shuhaib",24 ); /* default kerela will be there */
INSERT INTO employee ( emp_id,employee_name,age ) VALUES ( 2,"Shilpa",23 ); /* <18 error */
INSERT INTO employee ( emp_id,employee_name,age,state ) VALUES ( 3,"Shuhaib",24,"Tamilnadu" );
DROP TABLE employee;

CREATE TABLE employee (
emp_id INT NOT NULL UNIQUE AUTO_INCREMENT,
employee_name VARCHAR(20) NOT NULL ,
age INT CHECK(age>=18) ,
state VARCHAR(20) DEFAULT "Kerala"
);

INSERT INTO employee ( employee_name,age,state ) VALUES ( "Shilpa",23,"Tamilnadu" ),( "Aromal",22,"Bangluru" ); 

SHOW COLUMNS FROM employee;

CREATE TABLE salesman (
salesman_id int,
name varchar(20),
city varchar(20),
commission float,
PRIMARY KEY(salesman_id)
);

INSERT INTO salesman VALUES (5001,"James Hoog","New York",0.15),
(5002,"Nail Knite","Paris",0.13),
(5005,"Pit Alex","London",0.11),
(5006,"Mc Lyon","Paris",0.14),
(5003,"Lauson Hen",null,0.12),
(5007,"Paul Adam","Rome",0.13);

SELECT * FROM salesman;

CREATE TABLE customer(
customer_id int,
cust_name varchar(20),
city varchar(20),
grade int,
salesman_id int,
PRIMARY KEY(customer_id),
FOREIGN KEY(salesman_id) REFERENCES salesman(salesman_id)
);

INSERT INTO customer VALUES (3002,"Nick Rimando","New York",100,5001),
(3005,"Graham Zusi","California",200,5002),
(3001,"Brad Guzan","London",null,5005),
(3004,"Fabian Johns","Paris",300,5006),
(3007,"Brad Davis","New York",200,5001),
(3009,"Geoff Camero","Berlin",100,5003),
(3008,"Julian Green","London",300,5002),
(3003,"Jozy Alitidor","Moscow",200,5007);

SELECT * FROM customer;

CREATE TABLE orders (
ord_id int,
purch_amt float,
ord_date date,
customer_id int,
salesman_id int,
PRIMARY KEY (ord_id),
FOREIGN KEY(customer_id) REFERENCES customer(customer_id),
FOREIGN KEY(salesman_id) REFERENCES salesman(salesman_id)
);

INSERT INTO orders VALUES
(70001,150.5,"2012-10-05",3005,5002),
(70009,270.65,"2012-09-10",3001,5005),
(70002,65.26,"2012-10-05",3002,5001),
(70004,110.5,"2012-08-17",3009,5003),
(70007,948.5,"2012-09-10",3005,5002),
(70005,2400.6,"2012-07-27",3007,5001),
(70008,5760,"2012-09-10",3007,5001),
(70010,1983.43,"2012-10-10",3004,5006),
(70003,2480.4,"2012-10-10",3009,5003),
(70012,250.45,"2012-06-27",3008,5002),
(70011,75.29,"2012-08-17",3003,5007),
(70013,3045.6,"2012-04-25",3002,5001);

SELECT * FROM orders;

/*
MODEL RELATIONSHIP

one to one
one to many - fk
many to one - fk
many to many

*/

/* BASIC */
SELECT name,city FROM salesman WHERE city = "Paris";
SELECT * FROM customer WHERE grade = 200;
SELECT ord_id,ord_date,purch_amt FROM orders WHERE salesman_id = 5001;
SELECT * FROM salesman WHERE city IN ("Paris","Rome");
SELECT salesman_id,name,city,commission FROM salesman WHERE city NOT IN ("Paris","Rome");
SELECT * FROM customer WHERE customer_id IN (3007,3008,3009);
SELECT * FROM salesman WHERE commission BETWEEN 0.11 AND 0.15;   /* 0.12 - 0.14 */
SELECT * FROM orders WHERE purch_amt BETWEEN 500 AND 4000 AND purch_amt NOT IN (948.50,1983.43); /* below 0.5 not count in sql - its an issue in sql */     
SELECT * FROM salesman;
SELECT * FROM salesman WHERE name BETWEEN "a" AND "k"; /* or we need nested quarry */
SELECT * FROM customer WHERE cust_name LIKE ("b%");
SELECT * FROM salesman WHERE name LIKE ("n__l%");

/* AGGREGATE FUNCTIONS  */