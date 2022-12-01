from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from aeroporto.custom_auth_func import piloto, companhia, gerente, operador, torre
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.http import HttpResponseRedirect


def mainview(request):
    return render(request, 'main.html')


def redirect(request):
    
    group = request.user.groups.all()

    if group.filter(name__in=['companhia']).exists():
        return HttpResponseRedirect('monitoramento')
    elif group.filter(name__in=['gerente']).exists():
        return HttpResponseRedirect('relatorios')
    elif group.filter(name__in=['operador']).exists():
        return HttpResponseRedirect('crud')
    elif group.filter(name__in=['piloto']).exists():
        return HttpResponseRedirect('monitoramento')
    elif group.filter(name__in=['torre']).exists():
        return HttpResponseRedirect('monitoramento')

    return render(request, 'usuario_sem_grupo.html')


def crudview(request):
    return render(request, 'crud.html')


def monitoramentoview(request):
    return render(request, 'monitoramento.html')


def relatorioview(request):
    return render(request, 'relatorio.html')
