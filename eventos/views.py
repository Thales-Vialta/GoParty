from django.shortcuts import render
from django.http import HttpResponse

def lista_eventos(request): 
    return HttpResponse("Lista de eventos disponíveis. ")

def detalhe_evento(request, id): 
    return HttpResponse(f"Detalhes do evento {id}.")


# Create your views here.
