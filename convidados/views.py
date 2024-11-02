from django.shortcuts import render, redirect
from django.http import HttpResponse
from noivos.models import Convidados, Presentes


def convidados(request):
    token = request.GET.get('token')
    convidado = Convidados.objects.get(token=token)
    presentes = Presentes.objects.filter(reservado=False).order_by('-importancia')
    return render(request, 'convidados.html', {'convidado': convidado, 'presentes': presentes})


def responder_presenca(request):
    resposta = request.GET.get('resposta')
    token = request.GET.get('token')
    convidado = Convidados.objects.get(token=token)

    if resposta not in ['C', 'R']:
        return redirect(f'/convidados/?token={token}')
    
    convidado.status = resposta
    convidado.save()
    
    return HttpResponse(resposta)