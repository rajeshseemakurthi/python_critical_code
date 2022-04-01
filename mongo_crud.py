from pymongo import MongoClient
import datetime

cluster="mongodb+srv://mflex22student:mflex22password@mflex.isiup.mongodb.net/test?"
client=MongoClient(cluster)

print(client.list_database_names())

db=client.test

print(db.list_collection_names())

todo1={"names":"000000","status":"My first todo!","status":"open",
     "tags":["python","java"],"date":datetime.datetime.utcnow()}

todos=db.todos

#result=todos.insert_one(todo1)

todos2=[{"names":"00000main_main0000","status":"My first todo!","status":"open","tags":["python","java"],"date":datetime.datetime(2021,1,1,10,45)},
     {"names":"222","status":"My first todo!","status":"open","tags":["python","java"],"date":datetime.datetime(2022,2,15,11,43)}]

#result=todos.insert_many(todos2)

todos3=[{"name":111111},
        {"name":222222},
        {"name":333333},
        {"name":444444}]

#result=todos.insert_many(todos3)

# result=todos.find_one()
# print(result)

# results=todos.find({"names":"1245"})
# print(results)

# for result in results:
#      print(result)

# print(todos.count_documents({"names":"000000"}))
print(todos.count_documents({"tags":"python"}))

d=datetime.datetime(2021,7,2)

# results=todos.find({"date":{"$lt":d}})
# for result in results:
#      print(result)

# results=todos.find({"date":{"$gt":d}})
# for result in results:
#      print(result)

#for removing records
# from bson.objectid import ObjectId
# result=todos.delete_one({"_id":ObjectId("6245d5e23471ed9535609162")})

#for removing multiple records
# result=todos.delete_many({"name":444444})
# result=todos.delete_many({"name":111111})
# result=todos.delete_many({"name":222222})

todo4=[{"name":1223,"status":"open"},
        {"name":4536,"status":"open"}]

# result=todos.insert_many(todo4)

#for unsetting the field (removing the field)
# result=todos.update_one({"name":1},{"$set":{"status":True}})

result=todos.update_many({"name":1},{"$unset":{"status":None}})

