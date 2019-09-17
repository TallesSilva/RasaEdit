from faker import Faker
from json import dumps, load
from datetime import datetime

fake = Faker('pt_BR')

def get_fake_supplier():
    payload_supplier = {
        "nome": fake.name(),
        "cpf": fake.cpf(),
        "disponibilidade": "Integral",
        "cargo": "estagiario",
        "empresa": None,
        "endereco":{
            "rua": fake.street_name(),
            "numero": fake.building_number(),
            "complemento": None,
            "bairro": fake.bairro(),
            "cep": fake.postcode(),
            "cidade": fake.city(),
            "estado": fake.estado_sigla(),
            "latitude": None,
            "longitude": None
        },
        "contato":{
            "fixo": fake.cellphone_number(),
            "celular": fake.cellphone_number(),
            "email": "tallesr@kyros.com.br",
            "site": "http://192.168.1.3:8080/suppliers/",
            "whatsapp": fake.cellphone_number(),
            "telegram": fake.cellphone_number()
        }
    }
    return payload_supplier

def get_fake_customer():
    payload_customer = {
        "nome": fake.name(),
        "cpf": fake.cpf(),
        "dia_preferencia": None, #faker.providers.date_time
        "hora_preferencia": None,
        "empresa": None,
        "endereco": {
            "rua": fake.street_name(),
            "numero": fake.building_number(),
            "complemento": None,
            "bairro": fake.bairro(),
            "cep": fake.postcode(),
            "cidade": fake.city(),
            "estado": fake.estado_sigla(),
            "latitude": None,
            "longitude": None
        },
        "contato": {
            "fixo": fake.cellphone_number(),
            "celular": fake.cellphone_number(),
            "email": "tallesr@kyros.com.br",
            "site": None,
            "whatsapp": fake.cellphone_number(),
            "telegram": fake.cellphone_number()
        }
    }
    return payload_customer

def get_fake_timetable_none(): #como linkar com dados já existentes ?
    payload_timetable = {
    "data": None,
    "status": None,
    "observacao": "",
    "task": None,
    "supplier": None,
    "customer": None,
    "company": None
    }
    return payload_timetable

def get_fake_timetable_date(status, observacao, task, supplier, customer, company):
    fake_date = get_fake_date()
    payload_timetable = {
    "data": fake_date,
    "status": status,
    "observacao": observacao,
    "task": task,
    "supplier": supplier,
    "customer": customer,
    "company": company
    }
    return payload_timetable

def get_fake_date():
    fake_date = fake.future_datetime("+2d")
    try :
        if fake_date.hour > 8 and fake_date.hour < 18 :
            return fake_date #.strftime("%Y-%m-%dT%H:%M:%S")
    except:
        get_fake_date()

print(get_fake_date())