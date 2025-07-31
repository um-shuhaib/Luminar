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