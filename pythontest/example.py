from pymongo import MongoClient
from faker import Faker

fake = Faker()
client = MongoClient('localhost', 27017)

db = client.Agenda

Col_User = db.User
Col_Supplier = db.Supplier
Col_Timetable = db.Timetable
Col_Metadata = db.Metadata

profile = fake.profile()
Id = fake.bban()
phone = fake.phone_number()
name = fale.name()
address = fake.address()

Col_User.insert_one({
    'Id' : Id,
    'Phone' : phone,
    'Retrials' : None,
    'Address' : address,
    'when' : None,
})

Col_Supplier.insert_one({
    'Id' : Id,
    'Phone': phone,
    'Name': name,
    'Address' : address,

})

Col_Timetable.insert_one({
    'Id' : Id,
    'IDSupplier': phone,
    'IDUser': name,
    'date' : address,

})

Col_Metadata.insert_one({


})
