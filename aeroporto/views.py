from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.http import FileResponse

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

from .models import *
from .forms import *
import io


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

# Views do relatório
def relatorio_previstas(request):
    # Create Bytestream buffer
    buf = io.BytesIO()
    
    # Create canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    
    # Create text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)
    
    # Designate The Model
    voos = Voo.objects.all()
    
    # Create blank list
    lines = [
        'Relatório de Partidas e Chegadas Previstas de Voo'
        ' '
    ]
    
    for voo in voos:
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
    
    # Designate The Model
    voos = Voo.objects.all()
    
    # Create blank list
    lines = [
        'Relatório de Tempos Reais de Voo'
        ' '
    ]
    
    for voo in voos:
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
    
    # Designate The Model
    voos = Voo.objects.all()
    
    # Create blank list
    lines = [
        'Relatório de Atrasos de Voo'
        ' '
    ]
    
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

def relatorioview(request):
    return render(request, 'relatorio.html')


class MonitoramentoAllView(ListView):
    model = Voo
    template_name = 'monitoramento/monitoramento_all.html'
    
    def get(self, request):
        voo_object = Voo.objects.all()
        partindo = list()
        chegando = list()
        
        for voo in voo_object:
            if voo.partindo == 'Sim':
                partindo.append(voo)
            elif voo.partindo == 'Não':
                chegando.append(voo)
        
        partindo.sort(key=lambda x: x.partidaPrevista)
        chegando.sort(key=lambda x: x.chegadaPrevista)
        return render(request, self.template_name, {'chegando': chegando, 'partindo': partindo})


# View do monitoramento
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


class UpdateVooStatusView(UpdateView):
    model = Voo
    form_class = VooUpdateStatusForm
    template_name = 'monitoramento/atualizar_status_voo.html'
 
    def get(self, request, pk):
        codigoVoo = pk
        voo_object = Voo.objects.get(codigoVoo=codigoVoo)
        status = voo_object.status
        
        if voo_object.partindo == 'Sim':
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
                
        elif voo_object.partindo == 'Não':
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
