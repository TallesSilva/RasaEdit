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
from create_profile import (
    get_fake_supplier,
    get_fake_customer,
    get_fake_timetable_none,
    get_fake_timetable_date,
)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

####################################################################################################
#                          Metodos construtores das super classes                                  #
####################################################################################################
class Insert:
    def __init__(self):
        self.data = []

    def insert_to_mongo(self):
        response = None
        try:
            db = get_mongo_database()
            collection = db[self.collection]
            response = collection.insert_one(self.data)
        except Exception as ex:
            logger.error(ex.__name__)
            logger.error("Falha ao inserir no mongo: {}".format(str(ex)))
        return response

####################################################################################################
#                                  Metodos construtores das sub classes                            #
####################################################################################################

class GeneratorSupplier(Insert):
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

class GeneratorCustomer(Insert):
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

class GeneratorTimetableNone(Insert):
    def __init__(self):
        super(GeneratorTimetableNone,self).__init__()
        self.collection = 'time_table'

    def generate(self):
        try: 
            self.data = get_fake_timetable_none()
            return self.data
        except Exception as falha:
            logger.erro(falha.__name__)
            logger.erro("falha ao criar timetable sem a data: {}".format(str(falha)))            

class GeneratorTimetabledate(Insert):
    def __init__(self):
        super(GeneratorTimetabledate,self).__init__()
        self.collection = 'time_table'

    def generate(self):
        try: 
            self.data = get_fake_timetable_date("Aberto", "TesteObservation", "5d64086607538688f4e94077", "5d825b61f00ed355f07f94d2", "5d825b61f00ed355f07f94d4", "5d6020abd12e66a47a7888ed")
            return self.data
        except Exception as falha:
            logger.erro(falha.__name__)
            logger.erro("falha ao criar timetable sem a data: {}".format(str(falha)))            

if __name__ == '__main__':
    generators = [
        #GeneratorSupplier(),
        #GeneratorCustomer(),
        #GeneratorTimetableNone()
        #GeneratorTimetabledate()
    ]
    for g in generators:
        g.generate()
        g.insert_to_mongo()