from ctypes.wintypes import VARIANT_BOOL
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *

class CrudView(ListView):
    model = Voo 
    template_name = 'crud.html'
    
class AddVooView(CreateView):
    model = Voo
    form_class = VooForm
    template_name = 'adicionar_voo.html'
    
class DetailVooView(DetailView):
    model = Voo
    template_name = 'ver_voo.html'
    
class EditVooView(UpdateView):
    model = Voo
    form_class = VooEditForm
    template_name = 'editar_voo.html'
    
    def getInfos(request):
        
        voo = Voo.objects.all()
        
        return render(request, 'filmes_detalhes.html')
    
class DeleteVooView(DeleteView):
    model = Voo
    template_name = 'excluir_voo.html'
    success_url = reverse_lazy('crud')

# Create your views here.
def loginview(request):
    return render(request, 'login.html')

def mainview(request):
    return render(request, 'main.html')

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
