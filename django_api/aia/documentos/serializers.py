from rest_framework_mongoengine import serializers
from drf_queryfields import QueryFieldsMixin

from .models import (
    Documento,
    Template,
    Company,
    Supplier,
    Customer,
    Task,
    TimeTable
)

class DocumentoSerializer(QueryFieldsMixin, serializers.DocumentSerializer):
    class Meta:
        model = Documento
        fields = '__all__'

class TemplateSerializer(QueryFieldsMixin, serializers.DocumentSerializer):
    class Meta:
        model = Template
        fields = '__all__'

class CompanySerializer(QueryFieldsMixin, serializers.DocumentSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class CompanySerializer(QueryFieldsMixin, serializers.DocumentSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class SupplierSerializer(QueryFieldsMixin, serializers.DocumentSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class CustomerSerializer(QueryFieldsMixin, serializers.DocumentSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class TaskSerializer(QueryFieldsMixin, serializers.DocumentSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TimeTableSerializer(QueryFieldsMixin, serializers.DocumentSerializer):
    class Meta:
        model = TimeTable
        fields = '__all__'