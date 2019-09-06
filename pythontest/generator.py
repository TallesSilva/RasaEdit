import requests
from json import dumps, loads
import logging
import json

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

class Generator:
    def __init__(self):
        self.data = []

    def export_to_mongo(self):
        response = None
        print(self.data)
        try:
            response = requests.post(
                'http://192.168.1.3:8080/suppliers/',
                data=self.data)
            logger.info(
                "Foram inseridos {} documentos na coleção {}".format(self.data,
                                                                     self.collection)
            )
            return response.status_code
        except Exception as ex:
            logger.error(ex.__name__)
            logger.error("Falha ao inserir no mongo: {}".format(str(ex)))
            return response.status_code if response else 500

class GeneratorSupplier(Generator):
    def __init__(self):
        super(GeneratorSupplier, self).__init__()
        self.collection = 'suppliers'

    def generate(self):
        from fakes import get_fake_supplier
        try:
            fetch = get_fake_supplier()
            self.data = json.dumps(fetch, indent=4)
            return fetch
        except Exception as falha:
            logger.error(falha.__name__)
            logger.error("Falha ao receber supplier fake: {}".format(str(falha)))
            return response.status_code if response else 500


if __name__ == '__main__':
    generators = [
        GeneratorSupplier()
        # GeneratorUser()
    ]
    for g in generators:
        g.generate()
        g.export_to_mongo()
    print(g.export_to_mongo())


'''

print(json.dumps(payload, indent = 4))
#while(1)
r = requests.post('http://192.168.1.3:8080/suppliers/', data = payload )
#print(type(payload["contato"]))
print(r.text)
print(r.status_code)
'''
