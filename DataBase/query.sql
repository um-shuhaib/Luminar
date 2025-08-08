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


/*
ORDER BY - deafult asc, asc, desc 
GROUP BY - 
*/



/* NESTED QUARY */

SELECT * from salesman where commission in (select max(commission) from salesman);

/* KEYS
	UNIQUE KEY
	SUPER KEYS
	PRIMARY KEY
    FOREIGN KEY
    CANDIDATE KEY
    COMPOSITE KEY
    ALTERNATE KEY
    
*/

/* STRING METHODS */

SELECT upper("Structured Quary Language");
SELECT lower("Structured Quary Language");
SELECT length("  Python");
SELECT trim("  Python");  -- delete space from both end --like strip in python
SELECT ltrim("  Python ");
SELECT rtrim("  Python ");
SELECT length(trim("  python"));
SELECT concat("abc"," ","xyz"); -- concatination


/* DATE FORMATE */

SELECT current_date(); -- 2025-08-07
SELECT now(); -- 2025-08-07 12:25:04
SELECT current_time();
SELECT current_timestamp();
SELECT curtime();
SELECT curdate();

/* FORMATING DATE */

SELECT date_format("2025-08-07","%D"); -- 7th
SELECT date_format("2025-08-07","%d"); -- 07
SELECT date_format("2025-08-07","%M"); -- August
SELECT date_format("2025-08-07","%m"); -- 08
SELECT date_format("2025-08-07","%Y"); -- 2025
SELECT date_format("2025-08-07","%y"); -- 25

SELECT adddate("2025-08-07",INTERVAL 10 DAY); -- 2025-08-17
SELECT adddate("2025-08-07",INTERVAL 10 MONTH); -- 2026-06-07

SELECT datediff("2025-04-07","2025-08-07"); -- -122
SELECT datediff("2026-04-07","2025-04-07"); -- 365

/* STORED PROCEDURES */

-- delimeter
delimiter &&
CREATE PROCEDURE select_detail()
begin
SELECT * FROM customer;
end
&& delimiter ; 

CALL select_detail();

delimiter &&
CREATE PROCEDURE select_cust(IN var1 varchar(20))
begin
SELECT * FROM employee WHERE state=var1;
end
&& delimiter ; 

CALL select_cust("kerala");

drop procedure select_cust;

/* NORMALISATION */
/*anomalies, data redendency*/
-- 1NF,2NF,3NF,BCNF,5NF,6NF

-- functional dependacy
/*
a b c
a-b 
b-c then
a-c
*/
-- and partial dependency -- pk alland verey oru col vach mattoru col fetch cheyyan pattaruth
