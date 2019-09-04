from django.conf.urls import url
from rest_framework import routers
from rest_framework_mongoengine import routers as merouters

from .views import (
    DocumentoViewSet,
    TemplateViewSet,
    CompanyViewSet,
    SupplierViewSet,
    CustomerViewSet,
    TaskViewSet,
    TimeTableViewSet,
    EnviarEmailViewSet
)

merouter = merouters.DefaultRouter()
merouter.register(r'documentos', DocumentoViewSet, basename='documentos')
merouter.register(r'templates', TemplateViewSet, basename='templates')
merouter.register(r'companies', CompanyViewSet, basename='companies')
merouter.register(r'suppliers', SupplierViewSet, basename='suppliers')
merouter.register(r'customers', CustomerViewSet, basename='customers')
merouter.register(r'tasks', TaskViewSet, basename='tasks')
merouter.register(r'timetables', TimeTableViewSet, basename='timetables')
merouter.register(r'enviaremail', EnviarEmailViewSet, basename='enviaremail')

urlpatterns = []
urlpatterns += merouter.urls
