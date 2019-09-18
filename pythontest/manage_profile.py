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

def get_supplier():
    raise NotImplementedError

def get_customer():
    raise NotImplementedError

def get_timetable_date():
    raise NotImplementedError

