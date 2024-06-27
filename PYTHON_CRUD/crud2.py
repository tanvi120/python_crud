import vertica_python

# Connection details
conn_info = {
    'host': '192.168.50.179',
    'port': 5433,
    'user': 'dbadmin',
    'password': 'db@min',
    'database': 'smartech'
}
connection = vertica_python.connect(**conn_info)
cursor=connection.cursor()


# inserting record in table
'''
try:
    cursor.execute("INSERT INTO migration.ClientPayloadInfo(cid, payload_param, event_id) values(1,'vt_brands',2)")
    connection.commit()
    print("record inserted")
except:
    connection.rollback()

connection.close()  
'''

# display record of the table
'''
try:
    cursor.execute("SELECT * FROM migration.ClientPayloadInfo")
    result = cursor.fetchall()
    for i in result:
        client = i[0]
        payload_param = i[1]
        event_id = i[2]
        print(client, payload_param, event_id)

except:
    print("some issue in the code")

connection.close()

'''

# update the record
'''
try:
    cursor.execute("UPDATE migration.ClientPayloadInfo SET payload_param='vt_abc' WHERE cid=1")
    connection.commit()
    print("record updated successfully")
except:
    connection.rollback()
'''

# delete the record

try:
    cursor.execute("delete from migration.ClientPayloadInfo where cid=1")
    connection.commit()
    print("record deleted successfully")
except:
    cursor.rollback()
