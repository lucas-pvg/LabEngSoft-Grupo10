from django.shortcuts import render
from django.views.generic import ListView
from .models import *
from datetime import datetime

class CrudView(ListView):
    model = Voo 
    template_name = 'crud.html'

# Create your views here.
def loginview(request):
    return render(request, 'login.html')

def mainview(request):
    context = {}
    return render(request, 'main.html', context=context)

def monitoramentoview(request):
    context = {}
    return render(request, 'monitoramento/monitoramento.html', context=context)

def relatorioview(request):
    return render(request, 'relatorio.html')


def voo_search_view(request):
    query_dict = request.GET
    voo_object = None
    try:
        query = int(query_dict.get('voo'))
    except:
        query = None

    if query is not None:
            voo_object = Voo.objects.get(codigoVoo=query)
    context = {
        "voo": voo_object
    }
    
    return render(request, 'monitoramento/voosearch.html', context=context)
