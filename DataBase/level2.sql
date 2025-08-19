CREATE DATABASE company;
USE company;
CREATE TABLE Employeeinfo (emp_id int,first_name varchar(20),last_name varchar(20),gender varchar(20),primary key (emp_id));
SELECT * from employeeinfo;
CREATE TABLE employee_position (pos_id int,emp_id int,emp_psition varchar(20),primary key(pos_id),foreign key(emp_id) references employeeinfo(emp_id));
SELECT * from employee_position;

INSERT into Employeeinfo values (1,"manu","kumar","Male"),(2,"Shilpa","Das","Female"),(3,"Muhammed","Sahal","Male"),(4,"megha","udayakumar","Female"),(5,"stephin","devasia","Male");
INSERT into employee_position values (1,2,"HR"),(2,1,"Trainer"),(3,3,"Team lead"),(4,4,"HR"),(5,5,"Counilor");

/* QN 5*/

 -- 1
 SELECT emp_psition,count(emp_psition) as count from employee_position GROUP BY emp_psition;
 -- 2
 SELECT concat(first_name," ",last_name) as Full_name from employeeinfo;
-- 3
SELECT * from employeeinfo JOIN employee_position on employeeinfo.emp_id=employee_position.emp_id where employee_position.emp_psition = "HR" and employeeinfo.gender = "Female" ;  



/*  QN5 END*/
CREATE table worker (id int,first_name varchar(20),second_name varchar(20),department varchar(20));
SELECT * from worker;
INSERT into worker values (1,"megha","udayakumar","HR"),(2,"geerge","devasia","Developer"),(3,"Shilpa","das","anlytics"),(4,"Muhammed","sahal","HR"),(5,"Manu","mohan","Training");

CREATE table bonus (bon_id int,worker_id int,bonus int);
SELECT * from bonus;
INSERT into bonus values (1,4,100),(2,1,100),(3,2,150),(4,3,50),(5,5,45);

CREATE table Title (t_id int, title varchar(20));
SELECT * from title;
INSERT into title values (1,"BEST worker"),(2,"performer"),(3,"top fresher"),(4,"targer achiever"),(5,"performer");


/* QN 6 */

-- 1
SELECT upper(first_name ) from worker;
-- 2
SELECT distinct(department) from worker;
