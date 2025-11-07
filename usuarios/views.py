from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Área de usuários do GoParty.")

def login_view(request): 
    return HttpResponse("Página de login")

def cadastro_view(request): 
    
    return HttpResponse("Página de cadastro.")
