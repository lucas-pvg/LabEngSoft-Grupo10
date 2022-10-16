from django.urls import path, include
from .views import *

urlpatterns = [
    path('', mainview, name='home'),
    path('login/', loginview, name='login'),
    path('crud/', crudview, name='crud'),
    path('monitoramento/', monitoramentoview, name='monitoramento'),
    path('relatorios/', relatorioview, name='relatorios'),
]