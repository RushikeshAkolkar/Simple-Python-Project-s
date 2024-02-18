import mysql.connector

mydb = mysql.connector.connect(host='localhost',user='root',password='12345')

cur = mydb.cursor()

cur.execute("Create database db1")

print("Succesfully")
