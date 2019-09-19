from faker import Faker
from datetime import datetime
import json
from interfaces import get_mongo_database
from constants import (
    MONGO_HOST,
    MONGO_PORT,
    MONGO_USER,
    MONGO_PASS, 
    MONGO_DEFAULT_DB 
)
from find_manage import (
    FindOne,
)

fake = Faker('pt_BR')

####################################################################################################
#                                      Criação de perfil Fake                                      #
####################################################################################################

def get_fake_supplier():
    payload_supplier = {
        "nome": fake.name(),
        u"cpf": fake.cpf(),
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
        "dia_preferencia": None,
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

def get_fake_timetable_none():
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
    payload_timetable = {
    "data": get_fake_date(),
    "status": status,
    "observacao": observacao,
    "task": task,
    "supplier": supplier,
    "customer": customer,
    "company": company
    }
    return payload_timetable

def get_fake_date():
    fake_data = []
    try :
        fake_date = valida_data()
        #fake_date = fake_date.strftime("%Y-%m-%dT%H:%M:%S")
        return fake_date
    except:
        raise NotImplementedError

def valida_data():
    data = fake.future_datetime("+2d")
    #data.minute = None
    #data.second = None
    if data.hour<8 or data.hour>17:
        data = valida_data()
    return data    

def get_supplier(data_type, data_info, collection):
    f = FindOne()
    f.find()
    response = f.Find_one_to_mongo()
    return response

def get_customer(data_type, data_info, collection):
    f = FindOne()
    f.find()
    response = f.Find_one_to_mongo()
    return response

def get_timetable(data_type, data_info, collection):
    f = FindOne()
    f.find()
    response = f.Find_one_to_mongo()
    return response

def get_company(data_type, data_info, collection):
    f = FindOne()
    f.find()
    response = f.Find_one_to_mongo()
    return response

def get_all_customer(referencia):
    f = FindOne() 
    f.find(referencia, 1, 'customer')
    response = f.find_all_to_mongo()
    return response

def get_all_supplier(referencia):
    f = FindOne() 
    f.find(referencia, 1, 'supplier')
    response = f.find_all_to_mongo()
    return response

def get_all_company(referencia):
    f = FindOne() 
    f.find(referencia, 1, 'company')
    response = f.find_all_to_mongo()
    return response

def get_all_timetable(referencia):
    f = FindOne() 
    f.find(referencia, 1, 'time_table')
    response = f.find_all_to_mongo()
    return response

def create_timetable():
    customers = get_all_customer('cpf')
    companies = get_all_company('cnpj')
    timetables = get_all_timetable('task')
    suppliers = get_all_supplier('cpf')
    print(customers)
    print(companies)
    print(timetables)
    print(suppliers)
    payload_timetable = {
    "data": get_fake_date(),
    "status": 'Aberto',
    "observacao": '',
    "task": 'Instalação de Modem',
    "supplier": suppliers[0],
    "customer": customers[0],
    "company": companies[0]
    }
    return payload_timetable

create_timetable()