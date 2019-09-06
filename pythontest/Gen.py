import requests
from faker import Faker

fake = Faker('pt_BR')

payload = ({
    "nome": fake.name(),
    "cpf": fake.cpf(),
    "disponibilidade": None,
    "cargo": None,
    "empresa": None,
    "endereco": {
        "rua": fake.street_name(),
        "numero": fake.building_number(),
        "complemento": None,
        "bairro": fake.bairro(),
        "cep": fake.postcode(),
        "cidade": fake.city(),
        "estado": fake.estado_nome(),
        "latitude": None,
        "longitude": None
    },
    "contato": {
        "fixo": fake.phone_number(),
        "celular": fake.cellphone_number(),
        "email": None,
        "site": None,
        "whatsapp": None,
        "telegram": None
    }
})

print(payload)
#while(1)
r = requests.post('http://192.168.1.3:8080/suppliers/', data = payload )
print(r.status_code)
print(r.text)