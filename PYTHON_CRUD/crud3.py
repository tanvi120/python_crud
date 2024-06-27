from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('localhost', 27017)  # Assuming MongoDB is running locally on default port 27017

# Access or create a database
db = client['testdatabase']

# Access or create a collection
collection = db['studentrecord']
# inserting
try:
    collection.insert_one({'rollno': 2, 'name': 'Anupam', 'marks': 99})
    print("Record inserted into the collection")

except Exception as e:
    print("Error occurred while inserting record:", e)
# displaying
try:
    records = collection.find()
    for record in records:
        print(record)

except Exception as e:
    print("Error occurred while fetching records:", e)
# updating
try:
    collection.update_one({'rollno': 2}, {'$set': {'name': 'Tanvi'}})
    print("Record updated successfully")

except Exception as e:
    print("Error occurred while updating record:", e)
#delete
try:
    collection.delete_one({'rollno': 2})
    print("Record deleted successfully")

except Exception as e:
    print("Error occurred while deleting record:", e)

client.close()