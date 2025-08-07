SHOW DATABASES;
USE classicmodels;
SHOW TABLES;
SELECT * FROM customers;
SELECT * FROM customers WHERE customerNumber = 103;
SELECT * FROM customers WHERE country="France";

SELECT * FROM customers LIMIT 5;  /*only return 5 results*/
SELECT * FROM customers LIMIT 5 OFFSET 2;  /* skips first 2 record*/
SELECT distinct(country) FROM customers ;  /* distinct - no duplicate values */
SELECT * FROM customers WHERE country = "France" AND city = "nantes";
SELECT * FROM customers WHERE creditLimit < 50000;
SELECT customername,creditlimit FROM customers WHERE creditLimit < 50000;

SELECT customername,creditlimit FROM customers WHERE creditLimit > 50000 AND creditlimit < 100000; /* not included the 50k and 1L*/
SELECT customername,creditlimit FROM customers WHERE creditlimit BETWEEN 50000 AND 100000; /*includes the 50k and 1L*/

SELECT customername,country FROM customers WHERE country = "france" OR country = "usa";
SELECT customername,country FROM customers WHERE country = "france" OR country = "usa" OR country = "spain";
SELECT customername,country FROM customers WHERE country IN ("france","use","spain");

SELECT customername FROM customers WHERE customername LIKE("a%"); /* stat with a */
SELECT customername,contactfirstname FROM customers WHERE contactfirstname LIKE("%a"); /* end with a*/
SELECT customername FROM customers WHERE customername LIKE("_a%"); /* second charector a*/
SELECT customername FROM customers WHERE customername LIKE("__a%"); /* 3rd char a*/

SELECT customername,country FROM customers WHERE NOT country = "france";
SELECT customername,country FROM customers WHERE country != "france";
SELECT customername,country FROM customers WHERE country NOT IN ("france","usa");


/* Aggregate Functions 
 avg(),min(),max(),sum(),count() */

SELECT max(creditlimit) FROM customers;
SELECT max(creditlimit) as maximum_credit_limit FROM customers;  /* as - custom name  */
SELECT count(creditlimit) as count from customers;
SELECT sum(creditlimit) as sum_credit from customers;
SELECT avg(creditlimit) as avg_credit from customers;

/* delete items */


SELECT min(creditlimit) as max_credit from customers;
SELECT customername FROM customers ORDER BY customername;


SELECT customernumber,max(amount) FROM payments GROUP BY customernumber;


/* JOIN -      INNER JOIN
                OUTER JOIN - left and right join
				FULL JOIN
				SELF JOIN
*/


