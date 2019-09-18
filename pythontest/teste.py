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

def __init__():
    self.cpf = []

def Find_Supplier(self):        
    try:
        db = get_mongo_database()
        collection = db["supplier"]

        doc = collection.find({"cpf": self.cpf})

        for response in doc :
            print(response)
        except Exception as ex: 
        logger.error(ex.__name__)
        logger.error("Falha ao inserir no mongo: {}".format(str(ex)))

export_to_mongo()