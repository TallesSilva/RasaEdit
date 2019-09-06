from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework_mongoengine import viewsets as meviewsets
from rest_framework.decorators import action

from .handler.document_template import DocumentTemplate
from .handler.email import envia_email

from .models import (
    Documento,
    Template,
    Company,
    Supplier,
    Customer,
    Task,
    TimeTable
)

from .serializers import (
    DocumentoSerializer,
    TemplateSerializer,
    CompanySerializer,
    SupplierSerializer,
    CustomerSerializer,
    TaskSerializer,
    TimeTableSerializer
)


class DocumentoViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer

    def get_queryset(self):
        queryset = Documento.objects.all()

        active = self.request.query_params.get('active', None)
        name = self.request.query_params.get('name', None)

        if active:
            active = True if active.lower() in ['true', '1'] else False
            queryset = queryset.filter(active=active)

        if name:
            queryset = queryset.filter(name=name)

        return queryset


class TemplateViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer

    def get_queryset(self):
        queryset = Template.objects.all()

        name = self.request.query_params.get('name', None)

        if name:
            queryset = queryset.filter(name=name)

        return queryset


class CompanyViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class SupplierViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class CustomerViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class TaskViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TimeTableViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = TimeTable.objects.all()
    serializer_class = TimeTableSerializer


class EnviarEmailViewSet(viewsets.ViewSet):

    def create(self, request):
        data = request.data
        emails = data.get('emails', None)
        doc_id = data.get('id', None)

        if None in [emails, doc_id]:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'detail': "'emails' e 'id'(ID do Documento) são obrigatórios"})
        elif not isinstance(emails, list):
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'detail': "'emails' deve ser uma lista de emails"})


        documento = Documento.objects.get(id=doc_id)
        path = DocumentTemplate().retrieve(documento)
        sent = envia_email(emails, path)
        DocumentTemplate.delete(path)
        return Response(data={'path': path, 'emails': emails, 'sent': sent})
