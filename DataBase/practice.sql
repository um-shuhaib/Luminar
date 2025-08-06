USE python_june;


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

/*  AGGREGATE FUNCTIONS  */

SELECT sum(purch_amt) as Total_amt FROM orders; 
SELECT avg(purch_amt) as avg_amt FROM orders; 
SELECT count(salesman_id) as Total_slsman FROM salesman;

SELECT count(grade) as gradation FROM customer; /* ?????????????????????????? */
SELECT max(purch_amt) as Big_prchs FROM orders;
SELECT city,max(grade) as bg_grade FROM customer GROUP BY city;                      /* GROUP BY */
SELECT customer_id,max(purch_amt) FROM orders GROUP BY customer_id; /* Table is ultered - input is not currectly done */
SELECT * FROM orders;
SELECT customer_id,ord_date,max(purch_amt) FROM orders GROUP BY customer_id ORDER BY ord_date ;
SELECT customer_id,ord_date,max(purch_amt) FROM orders GROUP BY ord_date ;
SELECT salesman_id,max(purch_amt) as Highest_amt FROM orders WHERE ord_date = " 2012-08-17 ";
SELECT salesman_id,max(purch_amt) as Highest_amt FROM orders WHERE ord_date = " 2012-08-17 " GROUP BY salesman_id;


/* ORDER BY name - by default asc
ORDER BY name asc
ORDER BY name desc
 
 GROUP BY
 */
 
 
 /* JOIN -      INNER JOIN - JOIN
                OUTER JOIN - left join (full data from left and only matching data from right)and right join (full data from right and only matching data from left)
				FULL JOIN
				SELF JOIN
*/

CREATE TABLE table1 (name varchar(20),city varchar(20));
CREATE TABLE table2 (name varchar(20),city varchar(20));
INSERT INTO table1 VALUES("a","calicut"),("b","kochi"),("c","tvm");
INSERT INTO table2 VALUES("x","calicut"),("y","kochi");
SELECT * FROM table1;
SELECT * FROM table2;

/*
SELECT cols FROM table1 INNER JOIN table2 ON table1.col=table2.col
SELECT cols FROM table1 JOIN table2 ON table1.col=table2.col

JOIN and INNER JOIN is same
*/

SELECT table1.name,table1.city,table2.name,table2.city FROM table1 INNER JOIN table2 ON table1.city=table2.city;
SELECT table1.name,table1.city,table2.name,table2.city FROM table1 JOIN table2 ON table1.city=table2.city; -- only matching data
SELECT table1.name,table1.city,table2.name,table2.city FROM table1 LEFT JOIN table2 ON table1.city=table2.city; -- all data from left but only matching data from right
SELECT table1.name,table1.city,table2.name,table2.city FROM table1 RIGHT JOIN table2 ON table1.city=table2.city;

/* Practice */

SELECT salesman.name,customer.cust_name,salesman.city FROM salesman JOIN customer ON salesman.city = customer.city; -- 1
SELECT customer.cust_name,salesman.name FROM customer JOIN salesman ON customer.salesman_id=salesman.salesman_id; -- 3
