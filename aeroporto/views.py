from django.shortcuts import render

# Create your views here.
def loginview(request):
    return render(request, 'login.html')

def mainview(request):
    return render(request, 'main.html')

def crudview(request):
    return render(request, 'crud.html')

def monitoramentoview(request):
    return render(request, 'monitoramento.html')

def relatorioview(request):
    return render(request, 'relatorio.html')
