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

def get_fake_user():
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

def get_fake_timetable_none():
    raise NotImplementedError

def get_fake_timetable_date():
    raise NotImplementedError
