# need to install mysql-connector 
# pip install mysql-connector 
# mysql srever must be in start 

import mysql.connector 
# conn = mysql.connector.connect(host="localhost",user="root",password="")
conn = mysql.connector.connect(host="localhost",user="root",password="",database="classicmodels")
print("connectiom created")

cur = conn.cursor() #to do querry
# cur.execute("SHOW DATABASES") # execute returns nothing but cur returns the results
cur.execute("SHOW TABLES")
# cur.execute("CREATE TABLE table1(id int,name varchar(20))")

''' using execute we can only create structure, we cant add /delete or modify the db'''

# for i in cur:
#     print(i) # as tuple

                  # or

# fetchall(),fetchone(),fetchmany(limit)

print(cur.fetchall()) # tuple in list
# print(cur.fetchone())
# print(cur.fetchmany(4))