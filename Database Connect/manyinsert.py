import mysql.connector

mydb = mysql.connector.connect(host='localhost',
                               user='root',
                               password='12345',
                               database='db1')

cur = mydb.cursor()

s="insert into school values(%s,%s,%s)"

s1=[(5,'jk',78787),(3,'jsfsk',7),(4,'jkefef',87)]

cur.executemany(s,s1)

mydb.commit()

print("Inserted Succesfully .....")