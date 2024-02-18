import mysql.connector

mydb = mysql.connector.connect(host='localhost',
                               user='root',
                               password='12345',
                               database='db1')

cur = mydb.cursor()

s="create table school(sid integer(10) primary key, title varchar(20), price int(20))"

cur.execute(s)

print("Table Succesfully Created.....")