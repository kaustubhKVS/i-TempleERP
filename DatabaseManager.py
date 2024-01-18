from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['hoteldatabase']


def addCustDetails(aadhar, cname, cage, phone, caddress, finalprice, checkin, checkout):
    collection = db['customerdetails']
    cid = collection.count_documents({}) + 10
    data = {
        'cid': cid,
        'aadhar': aadhar,
        'cname': cname,
        'cage': cage,
        'phone': phone,
        'caddress': caddress,
        'finalprice': finalprice,
        'checkin': checkin,
        'checkout': checkout
    }
    collection.insert_one(data)
    return cid


def addEmployeeDetails(empid, aadhar, ename, age, gender, roleid):
    collection = db['employees']
    sal = db['roles'].find_one({'roleid': roleid})['sal']
    data = {
        'empid': empid,
        'aadhar': aadhar,
        'ename': ename,
        'age': age,
        'gender': gender,
        'roleid': roleid,
        'sal': sal
    }
    collection.insert_one(data)


def addItem(itemid, itemname, itemrate):
    collection = db['items']
    data = {
        'itemid': itemid,
        'itemname': itemname,
        'itemrate': itemrate
    }
    collection.insert_one(data)


def addRole(roleid, rolename, rolesal):
    collection = db['roles']
    data = {
        'roleid': roleid,
        'rolename': rolename,
        'rolesal': rolesal
    }
    collection.insert_one(data)


def addRoomType(roomtypeid, bednum, ac, roomrate, desc):
    collection = db['roomtype']
    data = {
        'roomtypeid': roomtypeid,
        'bednum': bednum,
        'ac': ac,
        'roomrate': roomrate,
        'desc': desc
    }
    collection.insert_one(data)


def addRoomService(itemid, quantity, rscid):
    collection = db['roomservice']
    orderid = collection.count_documents({}) + 10
    data = {
        'orderid': orderid,
        'itemid': itemid,
        'quantity': quantity,
        'rscid': rscid
    }
    collection.insert_one(data)


def addRoom(roomnum, roomid, size):
    collection = db['room']
    data = {
        'roomnum': roomnum,
        'roomid': roomid,
        'size': size
    }
    collection.insert_one(data)


def addBookingDetails(cid, totalamt):
    collection = db['bookingdetails']
    bid = collection.count_documents({}) + 10
    checkin = db['customerdetails'].find_one({'cid': cid})['checkin']
    checkout = db['customerdetails'].find_one({'cid': cid})['checkout']
    data = {
        'bid': bid,
        'cid': cid,
        'checkin': checkin,
        'checkout': checkout,
        'totalamt': totalamt
    }
    collection.insert_one(data)


def getFinalAmount(cid):
    customerdetails = db['customerdetails']
    items = db['items']
    p1 = customerdetails.find_one({'cid': cid})['finalprice']
    p2 = items.aggregate([
        {
            '$match': {'rscid': cid}
        },
        {
            '$lookup': {
                'from': 'roomservice',
                'localField': 'itemid',
                'foreignField': 'itemid',
                'as': 'roomservice'
            }
        },
        {
            '$unwind': '$roomservice'
        },
        {
            '$group': {
                '_id': None,
                'total_price': {'$sum': {'$multiply': ['$rate', '$roomservice.quantity']}}
            }
        }
    ])
    
    p2 = next(p2, None)
    p2 = p2['total_price'] if p2 else 0
    return p1 + p2


def getRoomType(roomtypeid):
    collection = db['roomtype']
    return collection.find_one({'roomtypeid': roomtypeid})


def selectRoom(roomtypeid, checkin, checkout):
    collection = db['roomtype']
    rate = collection.find_one({'roomtypeid': roomtypeid})['roomrate']
    delta = checkout - checkin
    totalprice = rate * delta.days
    return totalprice


def getCustDetails(cid):
    collection = db['customerdetails']
    return collection.find_one({'cid': cid})


def getAllItems():
    collection = db['items']
    return list(collection.find())


def getAllRoles():
    collection = db['roles']
    return list(collection.find())


def getAllEmployees():
    collection = db['employees']
    return list(collection.find())


def getAllRooms():
    collection = db['room']
    return list(collection.find())


def getAllRoomTypes():
    collection = db['roomtype']
    return list(collection.find())


def getAllBookingDetails():
    collection = db['bookingdetails']
    return list(collection.find())


def getAllCustomerDetails():
    collection = db['customerdetails']
    return list(collection.find())


def getAllOrders():
    collection = db['roomservice']
    return list(collection.find())
