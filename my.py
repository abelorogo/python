import mysql.connector

con= mysql.connector.connect(
    host="localhost",
    user='root',
    password="Abel49907.",
    database ='l'
)
e= con.cursor()
e.execute("show databases")
# e.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
print(e)
