import mysql.connector

db=mysql.connector.connect(
    user="root",
    host="localhost",
    database="jan11-python"
    
)
print(db)
