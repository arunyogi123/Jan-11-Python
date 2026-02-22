import mysql.connector

db=mysql.connector.connect(
    user="root",
    host="localhost",
    database="jan11-python"
    
)
terminal=db.cursor()
print(db)

# terminal.execute("insert into revision (fname,lname,address) values ('aruna','tamang','lalitpur'),('sahil','kc','baneshwor')")
# db.commit()



 
# terminal.execute ("UPDATE revision SET address = 'dolakha' WHERE lname = 'yogi'")

# db.commit()
    
    

# terminal.execute("Delete from revision   WHERE lname = 'kc'")

# db.commit()



terminal.execute("select fname,lname from revision limit 2")
result=terminal.fetchall()
print(result)