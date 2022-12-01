"""MyProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from aeroporto import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.loginview, name='login'),
    path('main', views.mainview, name='main'),
    path('crud', views.CrudView.as_view(), name='crud'),
    path('crud/ver_voo/<int:pk>', views.DetailVooView.as_view(), name='ver_voo'),
    path('crud/adicionar_voo/', views.AddVooView.as_view(), name='adicionar_voo'),
    path('crud/editar_voo/<int:pk>', views.EditVooView.as_view(), name='editar_voo'),
    path('crud/excluir_voo/<int:pk>', views.DeleteVooView.as_view(), name='excluir_voo'),
    path('monitoramento/', views.voo_search_view, name='monitoramento_voo'),
    path('monitoramento/', views.monitoramentoview, name='monitoramento'),
    path('monitoramento/monitoramento_all', views.MonitoramentoAllView.as_view(), name='monitoramento_all'),
    path('monitoramento/atualizar_status_voo/<int:pk>', views.UpdateVooStatusView.as_view(), name='atualizar_status_voo'),
    path('monitoramento/atualizar_partida_voo/<int:pk>', views.UpdateVooDepartureView.as_view(), name='atualizar_partida_voo'),
    path('monitoramento/atualizar_chegada_voo/<int:pk>', views.UpdateVooArrivalView.as_view(), name='atualizar_chegada_voo'),
    path('relatorio/', views.relatorioview, name='relatorio'),
    path('relatorios/chegadas', views.relatorio_chegadas_view, name='relatorio_chegadas'),
    path('relatorios/partidas', views.relatorio_partidas_view, name='relatorio_partidas'),
    path('relatorios/chegadas_pdf', views.relatorio_chegadas, name='relatorio_chegadas_pdf'),
    path('relatorios/partidas_pdf', views.relatorio_partidas, name='relatorio_partidas_pdf'),
    
    
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('members.urls')),
    path('', include('aeroporto.urls')),
]
