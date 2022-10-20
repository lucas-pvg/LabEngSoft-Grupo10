from django.urls import path, include
from .views import *

urlpatterns = [
    path('', mainview, name='home'),
    path('login/', loginview, name='login'),
    path('crud/', CrudView.as_view(), name='crud'),
    path('monitoramento/', monitoramentoview, name='monitoramento'),
    path('relatorios/', relatorioview, name='relatorios'),
]