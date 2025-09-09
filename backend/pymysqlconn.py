# need to install mysql-connector 
# pip install mysql-connector 
# mysql srever must be in start 

import mysql.connector 
# conn = mysql.connector.connect(host="localhost",user="root",password="")
conn = mysql.connector.connect(host="localhost",user="root",password="",database="classicmodels")
print("connectiom created")

cur = conn.cursor() #to do querry
# cur.execute("SHOW DATABASES") # execute returns nothing but cur returns the results
# cur.execute("SHOW TABLES")
# cur.execute("insert into table1 values (5,'akshay'),(6,'bhaskar')")
# cur.execute("insert into table1 values (%s,%s)",(7,"Madhavan"))   # string formating single data
# values = [(8,"kunjan"),(9,"safaru")]
# cur.executemany("INSERT into table1 values(%s,%s)",values)  # for inserting many data at a time
# conn.commit()                                                       # when modifying the db we must use the commmit(), obj lu ndakm but db lu update akula
# cur.execute("delete from table1 where id = 2")
cur.execute("update table1 set name='sabeel' where id = 7")
conn.commit()
cur.execute("select * from table1")
# cur.execute("CREATE TABLE table1(id int,name varchar(20))")

''' using execute we can only create structure, we cant add /delete or modify the db'''

# for i in cur:
#     print(i) # as tuple

                  # or

# fetchall(),fetchone(),fetchmany(limit)

print(cur.fetchall()) # tuple in list
# print(cur.fetchone())
# print(cur.fetchmany(4))

conn.close()
