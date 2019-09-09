import requests
from json import dumps, loads
import logging
import json
from interfaces import get_mongo_database
from constants import (
    MONGO_HOST,
    MONGO_PORT,
    MONGO_USER,
    MONGO_PASS, 
    MONGO_DEFAULT_DB 
)
from fakes import (
    get_fake_supplier,
    get_fake_customer,
    get_fake_timetable_none,
    get_fake_timetable_date
)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

class Generator:
    def __init__(self):
        self.data = []
        

    def export_to_mongo(self):
        response = None
        print(self.data)
        try:
            db = get_mongo_database()
            collection = db[self.collection]
            response = collection.insert_one(self.data)
        except Exception as ex:
            logger.error(ex.__name__)
            logger.error("Falha ao inserir no mongo: {}".format(str(ex)))
            

class GeneratorSupplier(Generator):
    def __init__(self):
        super(GeneratorSupplier, self).__init__()
        self.collection = 'supplier'

    def generate(self):
        try:
            self.data = get_fake_supplier()
            return self.data
        except Exception as falha:
            logger.error(falha.__name__)
            logger.error("Falha ao atualizar supplier fake: {}".format(str(falha)))
            


class GeneratorCustomer(Generator):
    def __init__(self):
        super(GeneratorCustomer, self).__init__()
        self.collection = 'customer'
        
    def generate(self):
        try:
            self.data = get_fake_customer()
            return self.data
        except Exception as falha:
            logger.error(falha.__name__)
            logger.error("Falha ao atualizar customer fake: {}".format(str(falha)))
            
class GeneratorTimetable(Generator):
    def __init__(self):
        super(GeneratorTimetable,self).__init__()
        self.collection = 'time_table'
        
    def generate(self):
        try: 
            self.data = 

if __name__ == '__main__':
    generators = [
        #GeneratorSupplier()
        #GeneratorCustomer()
        #GeneratorTimetable()
    ]
    for g in generators:
        g.generate()
        g.export_to_mongo()

'''

print(json.dumps(payload, indent = 4))
#while(1)
r = requests.post('http://192.168.1.3:8080/suppliers/', data = payload )
#print(type(payload["contato"]))
print(r.text)
print(r.status_code)
'''
