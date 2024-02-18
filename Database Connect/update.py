import mysql.connector

mydb = mysql.connector.connect(host='localhost',
                               user='root',
                               password='12345',
                               database='db1')

cur = mydb.cursor()

s="update school set price=price+10 where price>200"

cur.execute(s)

mydb.commit()

print("Inserted Succesfully .....")