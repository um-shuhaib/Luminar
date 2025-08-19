/* KEYS

SUPER KEY
CANDIDATE KEY
ALTERNATE KEY
COMPOSITE KEY
PRIMARY KEY
FOREIGN KEY
UNIQUE KEY

 */
 
 CREATE TABLE demo_table(id int primary key auto_increment,name varchar(20));
 INSERT INTO demo_table (name) VALUES ("a"),("b");
 INSERT INTO demo_table (name) VALUES ("x"),("y");
 SELECT * FROM demo_table;
 DROP TABLE demo_table;
 DELETE FROM demo_table WHERE id=4;
 TRUNCATE TABLE demo_table;
 
 -- copy a table 
 
 CREATE TABLE copytable LIKE demo_table;
 SELECT * from copytable;
 SHOW COLUMNS FROM copytable;
INSERT INTO copytable SELECT * FROM demo_table;
 
 
 /*
 DROP - complete table
 TRUNCATE - complete data in the table
 DELETE - only data , only clears data but not the row.
 */