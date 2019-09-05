# /'kɑpiɹajt/ Kyros Tecnologia
# Codigo generico para testes de criação de bd usando pymongo
# dev : TallesSilva https://github.com/TallesSilva/RasaEdit

from pymongo import MongoClient
from faker import Faker
from datetime import datetime

fake = Faker('pt_BR')
now = datetime.now()

user = DocHand
password = Doc123
host =

try:
    # Python 3.x
    from urllib.parse import quote_plus
except ImportError:
    # Python 2.x
    from urllib import quote_plus

uri = "mongodb://192.168.1.242:27017" % (
    quote_plus(user), quote_plus(password), host)
client = MongoClient(uri)

db = client.aia
Col_User = db.customer
Col_Supplier = db.supplier
Col_Timetable = db.timetable
Col_Metadata = db.metadata
Col_Timetable_Date = db.timetable
Col_Timetable_None = db.timetable
Col_Confirmation = db.confirmed

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
    def __init__(self, name, cpf, workinghours, cargo, empresa, address, numero, complemento, bairro, cep, cidade, estado, latitude, longitude, fixo, celular, email, site, whatsapp, telegram ):
        self.cpf = cpf
        self.name = name
        self.working_hours = workinghours
        self.cargo = cargo
        self.empresa = empresa
        self.address = address
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cep = cep
        self.cidade = cidade
        self.estado = estado
        self.latitude = latitude
        self.longitude = longitude
        self.fixo = fixo
        self.celular = celular
        self.email = email
        self.site = site
        self.whatsapp = whatsapp
        self.telegram = telegram

    def generate_supplier(self):
        Col_Supplier.insert_one(
                {
                                "nome": self.name,
                                "cpf": self.cpf,
                                "disponibilidade": self.working_hours,
                                "cargo": self.cargo,
                                "empresa": self.empresa,
                                "endereco": {
                                    "rua": self.address,
                                    "numero": self.numero,
                                    "complemento": self.complemento,
                                    "bairro": self.bairro,
                                    "cep": self.cep,
                                    "cidade": self.cidade,
                                    "estado": self.estado,
                                    "latitude": self.latitude,
                                    "longitude": self.longitude
                                },
                                "contato": {
                                    "fixo": self.fixo,
                                    "celular": self.celular,
                                    "email": self.email,
                                    "site": self.site,
                                    "whatsapp": self.whatsapp,
                                    "telegram": self.telegram,
                                }
})

class Timetable:
    def __init__(self, id, idsupplier, iduser, date):
        self.id = id
        self.idsupplier = idsupplier
        self.iduser = iduser
        self.date = date

    def generate_timetable_date(self):
        Col_Timetable_Date.insert_one({
            'Id' : self.id,
            'IDSupplier': None,
            'IDUser': None,
            'date' : self.date,
        })

    def generate_timetable_None(self):
        Col_Timetable_None.insert_one({
            'Id' : self.id,
            'IDSupplier': None,
            'IDUser': None,
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
            'IDtimetable' : None,
            'Confirmed' : None,
            'rescheduled' : None,
            'rescheduled' : None,
            'when' : None,
        })

class Metadata:
    def __init__(self, morning, afternoon, full):
        self.morning = '7:00 até 12:00',
        self.afternoon = '13:00 até 18:00',
        self.full = '7:00 até 12:00 e 13:00 até 18:00',

    def generate_metadata(self):
        Col_Metadata.insert_one({
            'Morning' : self.morning,
            'Afternon': self.afternoon,
            'Full': self.full,
        })


Random_user = User(fake.cpf(), fake.name(), fake.phone_number(), None, None, fake.address())
Random_supplier = Supplier(fake.name(), fake.cpf(), None, None, None, fake.street_name(), fake.building_number(), None, fake.bairro(), fake.postcode(), fake.city(), fake.estado_nome(), None, None,
fake.phone_number(), fake.cellphone_number(), None, None, None, None)
Random_timetable = Timetable(fake.bban(), None, None, now.strftime("%d/%m/%Y %H:%M:%S"))

Random_user.generate_user()
#Random_supplier.generate_supplier()
#Random_timetable.generate_timetable_None()
#Random_timetable.generate_timetable_date()
print("ok")
print(now.strftime("%d/%m/%Y %H:%M:%S"))
