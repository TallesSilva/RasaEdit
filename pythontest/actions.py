from pymongo import MongoClient
from faker import Faker
from datetime import datetime

class User:
    def __init__(self, id, name, phone, when, retrials, address):
        client = MongoClient('localhost', 27017).User
        faker = Faker()
        self.name = name #fake.name()
        self.phone = phone # fake.phone_number()
        self.when = when #fake.name() *************
        self.retrials = retrials #fake.name() *************
        self.address = address #fake.address()

    def generate_user (self, id, name, phone, when, retrials, address):
        self.id = fake.profile()
        self.name = fake.name()
        self.phone = fake.phone_number()
        self.address = fake.address()
        db = MongoClient().User{self.name, self.phone, self.address}

class Supplier:
    def __init__(self, id, name, working_hours, when, available):
        client = MongoClient('localhost', 27017).Supplier
        faker = Faker()
        self.name = name #fake.name()
        self.phone = phone # fake.phone_number()
        self.working_hours = working_hours #fake.name() *************
        self.when = when #fake.name() *************
        self.available = available #fake.address()

    def generate_supplier(self, id, name, working_hours, when, available):


connect()
U = User()
U.generate_user()
