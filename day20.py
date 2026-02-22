import mysql.connector

db = mysql.connector.connect(
    user ="root",
    host= "localhost",
    database = "jan11python"
)


terminal = db.cursor()
# create table

terminal.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

try:
    # TODO Insert
    '''
    query = "insert into student (fname, lname, address) value ('suman','sharma','ktm'),('ram','kc','jhapa')";
    terminal.execute(query)
    db.commit()
    '''

    # TODO update
    '''
    query = "UPDATE student SET address = 'dang' WHERE lname = 'kc'"
    terminal.execute(query)
    db.commit()
    '''

    # TODO delete
    '''
    query = "Delete from student   WHERE lname = 'kc'"
    terminal.execute(query)
    db.commit()
    '''

    # TODO create
    query = "SELECT fname, lname FROM student limit 10"
    terminal.execute(query)
    result = terminal.fetchall()
    for i in result:
        print(i[0], i[1])

except mysql.connector.errors.IntegrityError as e:
    print(e)
except:
    print("something went wrong")