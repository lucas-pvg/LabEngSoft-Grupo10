from ctypes.wintypes import VARIANT_BOOL
from django.shortcuts import render
from django.views.generic import ListView
from .models import *

class CrudView(ListView):
    model = Voo 
    template_name = 'crud.html'

# Create your views here.
def loginview(request):
    return render(request, 'login.html')

def mainview(request):
    return render(request, 'main.html')

def monitoramentoview(request):
    return render(request, 'monitoramento.html')

def relatorioview(request):
    return render(request, 'relatorio.html')
