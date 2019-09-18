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

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

####################################################################################################
#                          Metodos construtores das super classes                                  #
####################################################################################################
class Find:
    def __init__(self):
        self.cpf = []

    def find_to_mongo(self):
        try:
            db = get_mongo_database()
            collection = db[self.collection]

            doc = collection.find({self.ref: self.cpf}) # self.ref é o tipo de dado que vai ser
            for response in doc :                       # usado para fazer a busca na DB
                print(response)                         # exemplo: "id", "cpf" e "nome"
        except Exception as ex: 
            logger.error(ex.__name__)
            logger.error("Falha ao inserir no mongo: {}".format(str(ex)))

####################################################################################################
#                                  Metodos construtores das sub classes                            #
####################################################################################################

class FindSupplier(Find):
    def __init__(self):
        super(FindSupplier,self).__init__()
        self.collection = 'supplier'
        self.ref = []
        self.cpf = []

    def find(self):
        try: 
            self.ref = get_referencia_supplier()
            self.cpf = get_supplier_exist()
            return self.ref, self.cpf
        except Exception as falha:
            logger.erro(falha.__name__)
            logger.erro("falha ao buscar supplier: {}".format(str(falha)))  
