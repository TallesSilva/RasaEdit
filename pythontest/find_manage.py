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
        self.info = []
        self.collection = []
        
    def find_one_to_mongo(self):
            response = None
            try:
                db = get_mongo_database()
                collection = db[self.collection]

                doc = collection.find({self.data_type: self.data_info}) # self.ref é o tipo de dado que vai ser
                for response in doc:                                   # usado para fazer a busca na DB
                    print(response)                                    # exemplo: "id", "cpf" e "nome"
                    return response
            except Exception as ex: 
                logger.error(ex.__name__)
                logger.error("Falha ao inserir no mongo: {}".format(str(ex)))

    def find_all_to_mongo(self):
        vetor = []
        i=0
        try:
            db = get_mongo_database()
            collection = db[self.collection]
            doc = collection.find({},{self.data_type: self.data_info})
            for response in doc:
                vetor.insert(i, response['cpf'])
                i+=1
            return vetor
        except Exception as ex: 
            logger.error(ex.__name__)
            logger.error("Falha ao inserir no mongo: {}".format(str(ex)))

####################################################################################################
#                                  Metodos construtores das sub classes                            #
####################################################################################################

class FindOne(Find):
    def __init__(self):
        super(FindOne,self).__init__()
        self.collection = []
        self.ref = []
        self.data = []

    def find(self, data_type, data_info, collection):
        try: 
            self.collection = collection
            self.data_type = data_type
            self.data_info = data_info
            return self.data
        except Exception as falha:
            logger.erro(falha.__name__)
            logger.erro("falha ao buscar: {}".format(str(falha)))


if __name__ == '__main__':
    x=0
    generators = [
        FindOne()
       ]
    for g in generators:
        g.find('cpf', 1, 'customer')
        #g.find_one_to_mongo()
        g.find_all_to_mongo()
        

        