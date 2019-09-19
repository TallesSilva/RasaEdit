from interfaces import get_mongo_database
import logging
import json
from constants import (
    MONGO_HOST,
    MONGO_PORT,
    MONGO_USER,
    MONGO_PASS, 
    MONGO_DEFAULT_DB 
)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def __init__():
    self.cpf = []

def Find_Supplier():        
    try:
        db = get_mongo_database()
        collection = db["time_table"]

        doc = collection.find({},{'_id': 0,'status': 'Aberto', 'customer': 1})

        for response in doc :
            print(response)
    except Exception as falha:
        logger.erro(falha.__name__)
        logger.erro("falha ao buscar supplier: {}".format(str(falha)))  

Find_Supplier()