from faker import Faker
from json import dumps
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

def get_fake_timetable_date(): #como linkar com dados já existentes ?
    payload_timetable = {
    "data": None,
    "status": None,
    "observacao": "",
    "task": None,
    "supplier": null,
    "customer": null,
    "company": null
    }
    return payload_timetable

def get_fake_date():
    payload_date =  {
        'summary': summary,
        'location': location,
        'description': description,
        'start': {
            'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': timezone,
        },
        'end': {
            'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': timezone,
        },
        'attendees': [
        {'email':attendees },
    ],
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }