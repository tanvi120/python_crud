import mysql.connector

# Establish a connection to the MySQL database
mysqldb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3307",
    database="testdataset"
)

# Create a cursor object to execute SQL queries
mysqlcursor = mysqldb.cursor()
'''
mysqlcursor.execute("CREATE TABLE studentrecord(rollno INT, name VARCHAR(30), marks INT)")'''

# Insert a record into the studentrecord table
'''

try:
    mysqlcursor.execute("INSERT INTO studentrecord (rollno, name, marks) VALUES (2, 'Anupam', 99)")
    mysqldb.commit()
    print("Record inserted into the table")
    # Close the database connection
    

except:
    mysqldb.rollback()

mysqldb.close()

'''

#display record
'''

try:
    mysqlcursor.execute("SELECT * FROM studentrecord")
    result = mysqlcursor.fetchall()
    for i in result:
        roll = i[0]
        name = i[1]
        marks = i[2]
        print(roll, name, marks)

except:
    print("some issue in the code")

mysqldb.close()
'''

# update the record
'''
try:
    mysqlcursor.execute("update studentrecord set name='Tanvi' where rollno=1")
    mysqldb.commit()
    print("record updated successfully")
except:
    mysqldb.rollback()

'''
# delete the record

try:
    mysqlcursor.execute("delete from studentrecord where rollno=1")
    mysqldb.commit()
    print("record deleted successfully")
except:
    mysqldb.rollback()

