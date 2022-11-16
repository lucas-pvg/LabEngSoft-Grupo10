from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from .filters import VooFilter

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


# Views do CRUD
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
    
class DeleteVooView(DeleteView):
    model = Voo
    template_name = 'excluir_voo.html'
    success_url = reverse_lazy('crud')
    
voo_list_general = []

# Views do relatório
def relatorioview(request):
    template_name = 'relatorio.html'
    object_list = Voo.objects.all()
    voo_list = (VooFilter(request.GET, queryset = object_list))
    object_list = voo_list.qs
    
    context =   {
        'object_list': object_list,
        'filter': voo_list
    }
    
    return render(request, template_name, context)

def relatorio_previstas(request):
    
    # Create Bytestream buffer
    buf = io.BytesIO()
    
    # Create canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    
    # Create text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)
    
    # Object
    voos = Voo.objects.all()
    
    # Create blank list
    lines = [
        'Relatório de Partidas e Chegadas Previstas de Voo'
        ' '
    ]
    
    if len(voo_list_general) == 0:
        for voo in voos:
            lines.append(" ")
            lines.append("Código do Voo:" + " " + str(voo.codigoVoo))
            lines.append("Companhia Aérea:" + " " + str(voo.companhiaAerea))
            lines.append("Partida Prevista:" + " " + str(voo.partidaPrevista))
            lines.append("Chegada Prevista:" + " " + str(voo.chegadaPrevista))
            lines.append("Aeroporto de Origem:" + " " + str(voo.aeroportoOrigem))
            lines.append("Aeroporto de Destino:" + " " + str(voo.aeroportoDestino))
    else:
        for voo in voo_list_general:
            lines.append(" ")
            lines.append("Código do Voo:" + " " + str(voo.codigoVoo))
            lines.append("Companhia Aérea:" + " " + str(voo.companhiaAerea))
            lines.append("Partida Prevista:" + " " + str(voo.partidaPrevista))
            lines.append("Chegada Prevista:" + " " + str(voo.chegadaPrevista))
            lines.append("Aeroporto de Origem:" + " " + str(voo.aeroportoOrigem))
            lines.append("Aeroporto de Destino:" + " " + str(voo.aeroportoDestino))
        
    # Loop
    for line in lines:
        textob.textLine(line)
    
    # Finishing Up
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    
    # Return
    return FileResponse(buf, as_attachment=True, filename='tempos_previstos.pdf')

def relatorio_reais(request):
    # Create Bytestream buffer
    buf = io.BytesIO()
    
    # Create canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    
    # Create text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)
    
    # Object
    voos = Voo.objects.all()
    
    # Create blank list
    lines = [
        'Relatório de Tempos Reais de Voo'
        ' '
    ]
    
    if len(voo_list_general) == 0:
        for voo in voos:
            lines.append(" ")
            lines.append("Código do Voo:" + " " + str(voo.codigoVoo))
            lines.append("Companhia Aérea:" + " " + str(voo.companhiaAerea))
            lines.append("Partida Real:" + " " + str(voo.partidaReal))
            lines.append("Chegada Real:" + " " + str(voo.chegadaReal))
            lines.append("Aeroporto de Origem:" + " " + str(voo.aeroportoOrigem))
            lines.append("Aeroporto de Destino:" + " " + str(voo.aeroportoDestino))
    else:
        for voo in voo_list_general:
            lines.append(" ")
            lines.append("Código do Voo:" + " " + str(voo.codigoVoo))
            lines.append("Companhia Aérea:" + " " + str(voo.companhiaAerea))
            lines.append("Partida Real:" + " " + str(voo.partidaReal))
            lines.append("Chegada Real:" + " " + str(voo.chegadaReal))
            lines.append("Aeroporto de Origem:" + " " + str(voo.aeroportoOrigem))
            lines.append("Aeroporto de Destino:" + " " + str(voo.aeroportoDestino))
        
    # Loop
    for line in lines:
        textob.textLine(line)
    
    # Finishing Up
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    
    # Return
    return FileResponse(buf, as_attachment=True, filename='tempos_reais.pdf')

def relatorio_atrasos(request):
    # Create Bytestream buffer
    buf = io.BytesIO()
    
    # Create canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    
    # Create text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)
    
    # Object
    voos = Voo.objects.all()
    
    # Create blank list
    lines = [
        'Relatório de Atrasos de Voo'
        ' '
    ]
    
    if len(voo_list_general) == 0:
        for voo in voos:
            lines.append(" ")
            lines.append("Código do Voo:" + " " + str(voo.codigoVoo))
            lines.append("Companhia Aérea:" + " " + str(voo.companhiaAerea))
            lines.append("Partida Prevista:" + " " + str(voo.partidaPrevista))
            lines.append("Partida Real:" + " " + str(voo.partidaReal))
            lines.append("Chegada Prevista:" + " " + str(voo.chegadaPrevista))
            lines.append("Chegada Real:" + " " + str(voo.chegadaReal))
            lines.append("Aeroporto de Origem:" + " " + str(voo.aeroportoOrigem))
            lines.append("Aeroporto de Destino:" + " " + str(voo.aeroportoDestino))
    else:
        for voo in voo_list_general:
            lines.append(" ")
            lines.append("Código do Voo:" + " " + str(voo.codigoVoo))
            lines.append("Companhia Aérea:" + " " + str(voo.companhiaAerea))
            lines.append("Partida Prevista:" + " " + str(voo.partidaPrevista))
            lines.append("Partida Real:" + " " + str(voo.partidaReal))
            lines.append("Chegada Prevista:" + " " + str(voo.chegadaPrevista))
            lines.append("Chegada Real:" + " " + str(voo.chegadaReal))
            lines.append("Aeroporto de Origem:" + " " + str(voo.aeroportoOrigem))
            lines.append("Aeroporto de Destino:" + " " + str(voo.aeroportoDestino))
        
    # Loop
    for line in lines:
        textob.textLine(line)
    
    # Finishing Up
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    
    # Return
    return FileResponse(buf, as_attachment=True, filename='atrasos.pdf')

# Create your views here.
def loginview(request):
    return render(request, 'login.html')

def mainview(request):
    return render(request, 'main.html')

def monitoramentoview(request):
    context = {}
    return render(request, 'monitoramento/monitoramento.html', context=context)

# View do monitoramento
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

class UpdateVooStatusView(UpdateView):
    model = Voo
    form_class = VooUpdateStatusForm
    template_name = 'monitoramento/atualizar_status_voo.html'
    success_url = reverse_lazy('monitoramento')
    
class UpdateVooDepartureView(UpdateView):
    model = Voo
    form_class = VooUpdateDepartureForm
    template_name = 'monitoramento/atualizar_partida_voo.html'
    success_url = reverse_lazy('monitoramento')
    
class UpdateVooArrivalView(UpdateView):
    model = Voo
    form_class = VooUpdateArrivalForm
    template_name = 'monitoramento/atualizar_chegada_voo.html'
    success_url = reverse_lazy('monitoramento')
