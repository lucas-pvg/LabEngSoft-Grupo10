from django.urls import path, include
from .views import *
from members.views import login_view

urlpatterns = [
    # path('', login_view, name='login'),
    # path('login/', loginview, name='login'),
    path('crud/', CrudView.as_view(), name='crud'),
    path('crud/ver_voo/<int:pk>', DetailVooView.as_view(), name='ver_voo'),
    path('crud/adicionar_voo/', AddVooView.as_view(), name='adicionar_voo'),
    path('crud/editar_voo/<int:pk>', EditVooView.as_view(), name='editar_voo'),
    path('crud/excluir_voo/<int:pk>', DeleteVooView.as_view(), name='excluir_voo'),
    path('monitoramento/', monitoramentoview, name='monitoramento'),
    path('monitoramento/atualizar_voo/<int:pk>', EditVooView.as_view(), name='atualizar_voo'),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    
    # path('crud', crudview, name='crud'),
    # path('monitoramento', monitoramentoview, name='monitoramento'),
    # path('relatorios', relatorioview, name='relatorios'),
    
    path('redirect', redirect, name='redirect'),
    path('main', mainview, name='main'),
]

