from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['hoteldatabase']

# Creating Collections (equivalent to tables in SQL)
customerdetails = db['customerdetails']
room = db['room']
roomtype = db['roomtype']
roomservice = db['roomservice']
items = db['items']
bookingdetails = db['bookingdetails']
employees = db['employees']
roles = db['roles']

# Creating Documents (equivalent to inserting rows in SQL)
customerdetails.insert_one({
    'cid': 115,
    'aadhar': '669524138972',
    'cname': 'Rohit M S',
    'cage': 20,
    'phone': '9358432100',
    'caddress': '#41, 1st Main, Marathahalli, Bangalore',
    'finalprice': 1500,
    'checkin': '2022-11-12',
    'checkout': '2022-11-13'
})

roles.insert_one({
    'roleid': 11,
    'rolename': 'Manager',
    'sal': 95000
})

employees.insert_one({
    'empid': 31,
    'aadhar': '668574239817',
    'ename': 'Samuel Johnson',
    'age': 32,
    'gender': 'Male',
    'roleid': 11,
    'sal': 95000
})

items.insert_one({
    'itemid': 1,
    'itemname': 'Chocolate Ice Cream',
    'rate': 150
})

roomtype.insert_one({
    'roomtypeid': 1,
    'bednum': 2,
    'ac': 'AC',
    'rate': 2500,
    'description': 'Comfortable double room with AC, two single beds, a wardrobe and an outward facing window'
})

room.insert_one({
    'roomnum': 188,
    'roomtypeid': 1,
    'size': 268
})

roomservice.insert_one({
    'orderid': 1768,
    'itemid': 1,
    'quantity': 3,
    'rscid': 115
})

bookingdetails.insert_one({
    'bid': 1327,
    'cid': 115,
    'checkin': '2022-11-12',
    'checkout': '2022-11-13',
    'finalprice': 1950
})

# Adding References (equivalent to foreign keys in SQL)
room.create_index('roomtypeid')
roomservice.create_index('itemid')
bookingdetails.create_index('cid')
employees.create_index('roleid')
roomservice.create_index('rscid')




# def createTables():
#     collections = {
#         "customerdetails": [
#             {"name": "cid", "type": "int", "primary_key": True},
#             {"name": "aadhar", "type": "char", "size": 20},
#             {"name": "cname", "type": "char", "size": 50},
#             {"name": "cage", "type": "int"},
#             {"name": "phone", "type": "char", "size": 20},
#             {"name": "caddress", "type": "char", "size": 100},
#             {"name": "finalprice", "type": "float"},
#             {"name": "checkin", "type": "date"},
#             {"name": "checkout", "type": "date"}
#         ],
#         "room": [
#             {"name": "roomnum", "type": "int", "primary_key": True},
#             {"name": "roomtypeid", "type": "int"},
#             {"name": "size", "type": "int"}
#         ],
#         "roomtype": [
#             {"name": "roomtypeid", "type": "int", "primary_key": True},
#             {"name": "bednum", "type": "int"},
#             {"name": "ac", "type": "char", "size": 10},
#             {"name": "rate", "type": "float"},
#             {"name": "description", "type": "char", "size": 200}
#         ],
#         "roomservice": [
#             {"name": "orderid", "type": "int", "primary_key": True},
#             {"name": "itemid", "type": "int"},
#             {"name": "quantity", "type": "int"},
#             {"name": "rscid", "type": "int"}
#         ],
#         "items": [
#             {"name": "itemid", "type": "int", "primary_key": True},
#             {"name": "itemname", "type": "char", "size": 20},
#             {"name": "rate", "type": "float"}
#         ],
#         "bookingdetails": [
#             {"name": "bid", "type": "int", "primary_key": True},
#             {"name": "cid", "type": "int"},
#             {"name": "checkin", "type": "date"},
#             {"name": "checkout", "type": "date"},
#             {"name": "finalprice", "type": "float"}
#         ],
#         "employees": [
#             {"name": "empid", "type": "int", "primary_key": True},
#             {"name": "aadhar", "type": "char", "size": 20},
#             {"name": "ename", "type": "char", "size": 50},
#             {"name": "age", "type": "int"},
#             {"name": "gender", "type": "char", "size": 10},
#             {"name": "roleid", "type": "int"},
#             {"name": "sal", "type": "float"}
#         ],
#         "roles": [
#             {"name": "roleid", "type": "int", "primary_key": True},
#             {"name": "rolename", "type": "char", "size": 50},
#             {"name": "sal", "type": "float"}
#         ]
#     }

#     for collection, fields in collections.items():
#         db.create_collection(collection)
#         for field in fields:
#             field_name = field["name"]
#             field_type = field["type"]
#             field_size = field.get("size")
#             field_primary_key = field.get("primary_key", False)

#             if field_type == "char":
#                 field_type = f"string:{field_size}"
#             elif field_type == "int":
#                 field_type = "int"
#             elif field_type == "float":
#                 field_type = "float"
#             elif field_type == "date":
#                 field_type = "date"

#             db[collection].create_index(field_name, unique=field_primary_key)
#             db[collection].create_index(field_name, unique=field_primary_key)
#             db[collection].create_index(field_name, unique=field_primary_key)

# def addDefaultValues():
#     collections_data = {
#         "customerdetails": [
#             {"cid": 115, "aadhar": "669524138972", "cname": "Rohit M S", "cage": 20, "phone": "9358432100", "caddress": "#41, 1st Main, Marathahalli, Bangalore", "finalprice": 1500, "checkin": "2022-11-12", "checkout": "2022-11-13"}
#         ],
#         "roles": [
#             {"roleid": 11, "rolename": "Manager", "sal": 95000}
#         ],
#         "employees": [
#             {"empid": 31, "aadhar": "668574239817", "ename": "Samuel Johnson", "age": 32, "gender": "Male", "roleid": 11, "sal": 95000}
#         ],
#         "items": [
#             {"itemid": 1, "itemname": "Chocolate Ice Cream", "rate": 150}
#         ],
#         "roomtype": [
#             {"roomtypeid": 1, "bednum": 2, "ac": "AC", "rate": 2500, "description": "Comfortable double room with AC, two single beds, a wardrobe and an outward facing window"}
#         ],
#         "room": [
#             {"roomnum": 188, "roomtypeid": 1, "size": 268}
#         ],
#         "roomservice": [
#             {"orderid": 1768, "itemid": 1, "quantity": 3, "rscid": 115}
#         ],
#         "bookingdetails": [
#             {"bid": 1327, "cid": 115, "checkin": "2022-11-12", "checkout": "2022-11-13", "finalprice": 1950}
#         ]
#     }

#     for collection, data in collections_data.items():
#         db[collection].insert_many(data)

# def addForeignKeys():
#     foreign_keys = [
#         {"collection": "room", "field": "roomtypeid", "ref_collection": "roomtype", "ref_field": "roomtypeid"},
#         {"collection": "roomservice", "field": "itemid", "ref_collection": "items", "ref_field": "itemid"},
#         {"collection": "bookingdetails", "field": "cid", "ref_collection": "customerdetails", "ref_field": "cid"},
#         {"collection": "employees", "field": "roleid", "ref_collection": "roles", "ref_field": "roleid"},
#         {"collection": "roomservice", "field": "rscid", "ref_collection": "customerdetails", "ref_field": "cid"}
#     ]

#     for foreign_key in foreign_keys:
#         collection = foreign_key["collection"]
#         field = foreign_key["field"]
#         ref_collection = foreign_key["ref_collection"]
#         ref_field = foreign_key["ref_field"]

#         db[collection].create_index(field)
#         db[collection].create_index(ref_field)
#         db[collection].create_index(field)
#         db[collection].create_index(ref_field)

#         db[collection].create_index([(field, pymongo.ASCENDING), (ref_field, pymongo.ASCENDING)], unique=True)
#         db[collection].create_index([(field, pymongo.ASCENDING), (ref_field, pymongo.ASCENDING)], unique=True)

# createTables()
# addDefaultValues()
# addForeignKeys()
