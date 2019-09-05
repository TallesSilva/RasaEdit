from pymongo import MongoClient
from faker import Faker
from datetime import datetime

fake = Faker('pt_BR')
now = datetime.now()

user = 'DocHand'
password = 'Doc123'
host = '27017'

try:
    # Python 3.x
    from urllib.parse import quote_plus
except ImportError:
    # Python 2.x
    from urllib import quote_plus

uri = "mongodb://192.168.1.242" % (
    quote_plus(user), quote_plus(password), host)
client = MongoClient(uri)

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
workinghours = None
when = None
available = None


Col_User.insert_one({
    'Id' : CPF,
    'Name' : name,
    'Phone' : phone,
    'Retrials' : None,
    'Address' : address,
    'when' : None,
})
'''
Col_Supplier.insert_one({
    'Id' : CPF,
    'Name': name,
    'Workhours': workinghours, #descobrir como preencher
    'when' : when,
    'available' : available,
})

Col_Timetable_Date.insert_one({
    'Id' : Id, #descobrir como linkar
    'IDSupplier': None, #descobrir como linkar
    'IDUser': None, #descobrir como linkar
    'date' : now.strftime("%d/%m/%Y %H:%M:%S"), # perguntar ao rui qual a data da tabela
})

Col_Timetable_None.insert_one({
    'Id' : Id, #descobrir como linkar
    'IDSupplier': None, #descobrir como linkar
    'IDUser': None, #descobrir como linkar
    'date' : None, #perguntar ao rui qual data da tabela
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
'''
