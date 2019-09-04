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

class User:
    def __init__(self, id, name, phone, when, retrials, address):
        self.id = id
        self.name = name #fake.name()
        self.phone = phone # fake.phone_number()
        self.when = when #fake.name() *************
        self.retrials = retrials #fake.name() *************
        self.address = address #fake.address()

    def generate_user(self):
        Col_User.insert_one({
            'Id' : self.id,
            'Name' : self.name,
            'Phone' : self.phone,
            'Retrials' : self.retrials,
            'Address' : self.address,
            'when' : self.when,
        })

class Supplier:
    def __init__(self, cpf, name, workinghours, when, available):
        self.id = cpf
        self.name = name #fake.name()
        self.working_hours = workinghours #fake.name() *************
        self.when = when #fake.name() *************
        self.available = available #fake.address()

    def generate_supplier(self):
        Col_Supplier.insert_one({
            'Id' : self.id,
            'Name': self.name,
            'Workhours': self.working_hours, #descobrir como preencher
            'when' : self.when,
            'available' : self.available,
        })

class Timetable:
    def __init__(self, id, idsupplier, iduser, date):
        self.id = id
        self.idsupplier = idsupplier #fake.name()
        self.iduser = iduser #fake.name() *************
        self.date = date #fake.name() ************

    def generate_timetable_date(self):
        Col_Timetable_Date.insert_one({
            'Id' : Id, #descobrir como linkar
            'IDSupplier': None, #descobrir como linkar
            'IDUser': None, #descobrir como linkar
            'date' : now.strftime("%d/%m/%Y %H:%M:%S"),
        })

    def generate_timetable_None(self):
        Col_Timetable_None.insert_one({
            'Id' : Id, #descobrir como linkar
            'IDSupplier': None, #descobrir como linkar
            'IDUser': None, #descobrir como linkar
            'date' : None,
        })

class Confirmation:
    def __init__(self, id, Idtimetable, confirmed, rescheduled1, rescheduled2, when):
        self.id = id,
        self.Idtimetable = Idtimetable,
        self.confirmed = confirmed,
        self.rescheduled1 = rescheduled1,
        self. rescheduled2 = rescheduled2,
        self.when = when,

    def generate_confirmation(self):
        Col_Confirmation.insert_one({
            'Id' : Id,
            'IDtimetable' : None, #descobrir como linkar
            'Confirmed' : None,
            'rescheduled' : None,
            'rescheduled' : None,
            'when' : None,
        })

class Metadata:
    def __init__(self, morning, afternoon, full):
        self.morning = morning,
        self.afternoon = afternoon,
        self.full = full,

    def generate_metadata(self):
        Col_Metadata.insert_one({
            'Morning' : '7:00 até 12:00',
            'Afternon': '13:00 até 18:00',
            'Full': '7:00 até 12:00 e 13:00 até 18:00',
        })


Random_user = User(fake.cpf(), fake.name(), fake.phone_number(), None, None, fake.address())
Random_supplier = Supplier(fake.cpf(), fake.name(), None, None, None)

#Random_user.generate_user()
#Random_supplier.generate_supplier()
print("ok")
