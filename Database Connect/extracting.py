import mysql.connector

mydb = mysql.connector.connect(host='localhost',
                               user='root',
                               password='12345',
                               database='db1')

cur = mydb.cursor()

s="select * from school"

cur.execute(s)

result = cur.fetchall()

for rec in result:
    print(rec)


print("Inserted Succesfully .....")