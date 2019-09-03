from pymongo import MongoClient
from faker import Faker
from datetime import datetime

fake = Faker('pt_BR')
client = MongoClient('localhost', 27017)

db = client.Agenda

Col_User = db.User
Col_Supplier = db.Supplier
Col_Timetable = db.Timetable
Col_Metadata = db.Metadata

Id = fake.bban()
CPF = fake.cpf()
phone = fake.phone_number()
name = fale.name()
address = fake.address()
data = fake.data()
now = datetime.now()

Col_User.insert_one({
    'Id' : CPF,
    'Name' : name,
    'Phone' : phone,
    'Retrials' : None,
    'Address' : address,
    'when' : None,
})

Col_Supplier.insert_one({
    'Id' : CPF,
    'Name': phone,
    'Workhours': name,
    'when' : address,
})

Col_Timetable.insert_one({
    'Id' : Id,
    'IDSupplier': IDSupplier,
    'IDUser': IDUser,
    'date' : now.strftime("%d/%m/%Y %H:%M:%S"),
})

Col_Timetable.insert_one({

})

Col_Metadata.insert_one({
    'Morning' : '7:00 até 12:00',
    'Afternon': '13:00 até 18:00',
    'Full': '7:00 até 12:00 e 13:00 até 18:00',
})
