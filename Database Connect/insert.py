import mysql.connector

mydb = mysql.connector.connect(host='localhost',
                               user='root',
                               password='12345',
                               database='db1')

cur = mydb.cursor()

s="insert into school values(%s,%s,%s)"

s1=(1'abcdefghijk',5643)

cur.execute(s,s1)

mydb.commit()

print("Inserted Succesfully .....")