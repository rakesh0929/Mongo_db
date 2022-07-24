import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.test   # client.name of databse
# info = db.testinformation
print(db)

# # mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false


d = [{
    "name":"Rakesh",
    "email" : "rakeshbathala29@gmail.com",
    "surname" : "Raki"
},
    {
        "name": "Rakesh_name",
        "email": "rakeshbathala29_email@gmail.com",
        "surname": "Raki_surname"
    },
    {
        "name": "Rakesh_2",
        "email": "rakeshbathala29@gmail.com",
        "surname": "Raki_2"
    }
]
db1 = client['mongotest']
coll = db1['test']
# coll.insert_one(d)   ## for one record
coll.insert_many(d)
