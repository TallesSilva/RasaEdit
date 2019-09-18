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
        self.data = []

    def find_to_mongo(self):
        response = None
        try:
            db = get_mongo_database()
            collection = db[self.collection]

            doc = collection.find({self.ref: self.data}) # self.ref é o tipo de dado que vai ser
            for response in doc:                         # usado para fazer a busca na DB
                print(response)                          # exemplo: "id", "cpf" e "nome"
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
        self.data = []

    def find(self):
        try: 
            self.ref = "cpf" #get_supplier_ref()
            self.data = "860.537.129-30"    #get_supplier_data()
            return self.data
        except Exception as falha:
            logger.erro(falha.__name__)
            logger.erro("falha ao buscar supplier: {}".format(str(falha)))
 
class FindCustomer(Find):
    def __init__(self):
        super(FindCustomer, self).__init__()
        self.collection = 'customer'
        self.ref = []
        self.data = []

    def find(self):
        try:
            self.ref = "cpf"
            self.data = "621.403.759-80"
            return self.data
        except Exception as falha:
            logger.erro(falha.__name__)
            logger.erro("falha ao buscar supplier: {}".format(str(falha)))
        raise

class FindTimetable(Find):
    def __init__(self):
        super(FindTimetable, self).__init__()
        self.collection = 'time_table'
        self.ref = []
        self.data = []

    def find(self):
        try:
            self.ref = "customer"
            self.data = "5d825b61f00ed355f07f94d4"
            return self.data
        except Exception as falha:
            logger.error(falha.__name__)
            logger.erro("falha ao buscar supplier: {}".format(str(falha)))
        raise

if __name__ == '__main__':
    generators = [
        #FindSupplier()
        #FindCustomer()
        #FindTimetable()
       ]
    for g in generators:
        g.find()
        g.find_to_mongo()