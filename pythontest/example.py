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
Col_Timetable_Date = db.Timetable
Col_Timetable_None = db.Timetable
Col_Confirmation = db.Confirmed

Id = fake.bban()
CPF = fake.cpf()
phone = fake.phone_number()
name = fake.name()
address = fake.address()
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
    'Name': name,
    'Workhours': None, #descobrir como preencher
    'when' : None,
    'available' : None,
})

Col_Timetable_Date.insert_one({
    'Id' : Id, #descobrir como linkar
    'IDSupplier': None, #descobrir como linkar
    'IDUser': None, #descobrir como linkar
    'date' : now.strftime("%d/%m/%Y %H:%M:%S"),
})

Col_Timetable_None.insert_one({
    'Id' : Id, #descobrir como linkar
    'IDSupplier': None, #descobrir como linkar
    'IDUser': None, #descobrir como linkar
    'date' : None,
})

Col_Confirmation.insert_one({
    'Id' : Id,
    'IDtimetable' : None, #descobrir como linkar
    'Confirmed' : None,
    'rescheduled' : None,
    'rescheduled' : None,
    'when' : None,
})

Col_Metadata.insert_one({
    'Morning' : '7:00 até 12:00',
    'Afternon': '13:00 até 18:00',
    'Full': '7:00 até 12:00 e 13:00 até 18:00',
})
