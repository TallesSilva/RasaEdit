from django.db import models
from django.utils import timezone

from mongoengine import Document, fields, EmbeddedDocument
from faker import Faker
from datetime import datetime

fake = Faker('pt_BR')
now = datetime.now()

ESTADOS = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG',
           'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']

STATUS = ['Aberto', 'Pendente', 'Fechado', 'Cancelado', 'Agendado']

DIAS = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']

WORKHOURS = ['Manhã', 'Tarde', 'Integral']

class Endereco(EmbeddedDocument):
    meta = {'strict': False}

    rua = fields.StringField(required=True)
    numero = fields.StringField(required=True)
    complemento = fields.StringField(required=False)
    bairro = fields.StringField(required=True)
    cep = fields.StringField(required=True)
    cidade = fields.StringField(required=True)
    estado = fields.StringField(required=True, choices=ESTADOS)
    latitude = fields.StringField(required=True)
    longitude = fields.StringField(required=True)

class Contato(EmbeddedDocument):
    meta = {'strict': False}

    fixo = fields.StringField(required=False)
    celular = fields.StringField(required=True)
    email = fields.EmailField(required=True)
    site = fields.StringField(required=False)
    whatsapp = fields.StringField(required=False)
    telegram = fields.StringField(required=False)

# ------------------------------------------------------------

class Template(Document):
    meta = {'strict': False}

    name = fields.StringField(required=True, unique=True)
    file = fields.StringField(required=False, null=True)
    fields = fields.ListField()

class Documento(Document):
    meta = {'strict': False}

    template = fields.ReferenceField('Template', required=True)
    active = fields.BooleanField(default=True)
    name = fields.StringField(required=False, unique=True)
    format = fields.StringField(required=False, null=True)
    created = fields.DateTimeField(default=timezone.now)
    fields = fields.DynamicField(required=True)

class Company(Document):
    meta = {'strict': False}

    nome = fields.StringField(required=True)
    nome_responsavel = fields.StringField(required=False)
    razao_social = fields.StringField(required=True)
    cnpj = fields.StringField(required=True, unique=True)
    endereco = fields.EmbeddedDocumentField(Endereco, required=True)
    contato = fields.EmbeddedDocumentField(Contato, required=True)

class Supplier(Document):
    meta = {'strict': False}

    nome = fields.StringField(required=True)
    cpf = fields.StringField(required=True, unique=True)
    disponibilidade = fields.StringField(required=False, choices=WORKHOURS)
    endereco = fields.EmbeddedDocumentField(Endereco, required=False)
    empresa = fields.ReferenceField('Company', required=False)
    cargo = fields.StringField(required=False)
    contato = fields.EmbeddedDocumentField(Contato, required=False)

class Customer(Document):
    meta = {'strict': False}

    nome = fields.StringField(required=True)
    cpf = fields.StringField(required=True, unique=True)
    endereco = fields.EmbeddedDocumentField(Endereco, required=True)
    contato = fields.EmbeddedDocumentField(Contato, required=True)
    empresa = fields.ReferenceField('Company', required=True)
    dia_preferencia = fields.StringField(required=True)
    hora_preferencia = fields.StringField(required=True)

class Task(Document):
    meta = {'strict': False}

    descricao = fields.StringField(required=True)
    company = fields.ReferenceField('Company', required=True)

class TimeTable(Document):
    meta = {'strict': False}

    data = fields.DateTimeField(required=True)
    status = fields.StringField(required=True, choices=STATUS)
    task = fields.ReferenceField('Task', required=True)
    supplier = fields.ReferenceField('Supplier', required=True)
    customer = fields.ReferenceField('Customer', required=True)
    company = fields.ReferenceField('Company', required=True)
    observacao = fields.StringField(required=False)
