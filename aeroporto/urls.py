from django.urls import path
from .views import *

urlpatterns = [
    path('', mainview, name='home'),
    path('login/', loginview, name='login'),
    path('crud/', CrudView.as_view(), name='crud'),
    path('crud/ver_voo/<int:pk>', DetailVooView.as_view(), name='ver_voo'),
    path('crud/adicionar_voo/', AddVooView.as_view(), name='adicionar_voo'),
    path('crud/editar_voo/<int:pk>', EditVooView.as_view(), name='editar_voo'),
    path('crud/excluir_voo/<int:pk>', DeleteVooView.as_view(), name='excluir_voo'),
    path('monitoramento/', monitoramentoview, name='monitoramento'),
    path('monitoramento/atualizar_voo/<int:pk>', UpdateVooView, name='atualizar_voo'),
    path('relatorios/', relatorioview, name='relatorios'),
    path('relatorios/previstas_pdf', relatorio_previstas, name='relatorio_previstas'),
]

