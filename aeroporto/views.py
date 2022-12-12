from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.http import HttpResponseRedirect

from .models import *
from .forms import *

from dateutil.parser import parse
from datetime import timedelta

voo_list_general = []



# View com função de redirecionar cada login para a página correta - Login.
def redirect(request):
    group = request.user.groups.all()

    if group.filter(name__in=['companhia']).exists():
        return HttpResponseRedirect('monitoramento/')
    elif group.filter(name__in=['gerente']).exists():
        return HttpResponseRedirect('relatorio/')
    elif group.filter(name__in=['operador']).exists():
        return HttpResponseRedirect('crud')
    elif group.filter(name__in=['piloto']).exists():
        return HttpResponseRedirect('monitoramento/')
    elif group.filter(name__in=['torre']).exists():
        return HttpResponseRedirect('monitoramento/')

    return HttpResponseRedirect('monitoramento/monitoramento_all')



# Views referentes às telas do CRUD - CRUD
class CrudView(ListView):
    model = Voo 
    template_name = 'crud/crud.html'
    
class AddVooView(CreateView):
    model = Voo
    form_class = VooForm
    template_name = 'crud/adicionar_voo.html'
    
class DetailVooView(DetailView):
    model = Voo
    template_name = 'crud/ver_voo.html'
    
class EditVooView(UpdateView):
    model = Voo
    form_class = VooEditForm
    template_name = 'crud/editar_voo.html'
    
class DeleteVooView(DeleteView):
    model = Voo
    template_name = 'crud/excluir_voo.html'
    success_url = reverse_lazy('crud')
    


# Vies referentes às telas do monitoramento - Monitoramento
class MonitoramentoAllView(ListView):
    model = Voo
    template_name = 'monitoramento/monitoramento_all.html'
    
    def get(self, request):
        voo_object = Voo.objects.all()
        partindo = list()
        chegando = list()
        
        for voo in voo_object:
            if voo.condicao == 'Partindo':
                partindo.append(voo)
            elif voo.condicao == 'Chegando':
                chegando.append(voo)
        
        partindo.sort(key=lambda x: x.partidaPrevista)
        chegando.sort(key=lambda x: x.chegadaPrevista)
        return render(request, self.template_name, {'chegando': chegando, 'partindo': partindo})


class UpdateVooStatusView(UpdateView):
    model = Voo
    form_class = VooUpdateStatusForm
    template_name = 'monitoramento/atualizar_status_voo.html'
 
    def get(self, request, pk):
        codigoVoo = pk
        voo_object = Voo.objects.get(codigoVoo=codigoVoo)
        status = voo_object.status
        
        if voo_object.condicao == 'Partindo':
            if status == 'Aguardo':
                choices = [('Aguardo', 'Aguardo'), ('Embarcando', 'Embarcando'), ('Cancelado', 'Cancelado')]
            elif status == 'Cancelado':
                choices = [('Cancelado', 'Cancelado'), ('Aguardo', 'Aguardo')]
            elif status == 'Embarcando':
                choices = [('Embarcando', 'Embarcando'), ('Programado', 'Programado')]
            elif status == 'Programado':
                choices = [('Programado', 'Programado'), ('Taxiando', 'Taxiando')]
            elif status == 'Taxiando':
                choices = [('Taxiando', 'Taxiando'), ('Pronto', 'Pronto')]
            elif status == 'Pronto':
                choices = [('Pronto', 'Pronto'), ('Autorizado', 'Autorizado')]
            elif status == 'Autorizado':
                choices = [('Autorizado', 'Autorizado'), ('Em voo', 'Em voo')]
            elif status == 'Em voo':
                choices = [('Em voo', 'Em voo'), ('Aguardo', 'Aguardo')]
                
        elif voo_object.condicao == 'Chegando':
            if status == 'Aguardo':
                choices = [('Aguardo', 'Aguardo'), ('Em voo', 'Em voo')]
            elif status == 'Em voo':
                choices = [('Em voo', 'Em voo'), ('Aterrissado', 'Aterrissado')]
            elif status == 'Aterrissado':
                choices = [('Aterrissado', 'Aterrissado'), ('Aguardo', 'Aguardo')]
        
        form = self.form_class(choices=choices)
        return render(request, self.template_name, {'form': form, 'voo': voo_object})
    
    def get_success_url(self):
        codigoVoo=self.kwargs['pk']
        return f'{reverse_lazy("monitoramento")}?voo={codigoVoo}'


class UpdateVooDepartureView(UpdateView):
    model = Voo
    form_class = VooUpdateDepartureForm
    template_name = 'monitoramento/atualizar_partida_voo.html'
    
    def get_success_url(self):
        codigoVoo=self.kwargs['pk']
        return f'{reverse_lazy("monitoramento")}?voo={codigoVoo}'
    

class UpdateVooArrivalView(UpdateView):
    model = Voo
    form_class = VooUpdateArrivalForm
    template_name = 'monitoramento/atualizar_chegada_voo.html'
    
    def get_success_url(self):
        codigoVoo=self.kwargs['pk']
        return f'{reverse_lazy("monitoramento")}?voo={codigoVoo}'


def monitoramentoview(request):
    context = {}
    return render(request, 'monitoramento/monitoramento.html', context=context)


def voo_search_view(request):
    voo_object = None
    query = None
    query_dict = request.GET
    
    try:
        query = int(query_dict.get('voo'))
    except:
        query = None

    if query is not None:
        try:
            voo_object = Voo.objects.get(codigoVoo=query)
        except:
            voo_object = None
            messages.error(request, f'Não foi encontrado Voo com o código {query}')
            
    context = {'voo': voo_object}
    return render(request, 'monitoramento/voosearch.html', context=context)



# Views referentes às telas dos relatórios - Relatório
def relatorioview(request):
    return render(request, 'relatorio/relatorio.html')


def relatorio_chegadas_view(request):
    template_name = 'relatorio/relatorio_chegadas.html'
    object_list = Voo.objects.all()
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    
    if start_date and end_date:
        end_date = parse(end_date) + timedelta(1)
        object_list = object_list.filter(
            chegadaReal__range=[start_date, end_date]
        )

    context =  {'object_list': object_list}
    return render(request, template_name, context)


def relatorio_partidas_view(request):
    template_name = 'relatorio/relatorio_partidas.html'
    object_list = Voo.objects.all()
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        end_date = parse(end_date) + timedelta(1)
        object_list = object_list.filter(
            partidaReal__range=[start_date, end_date]
        )

    context =  {'object_list': object_list}
    return render(request, template_name, context=context)
