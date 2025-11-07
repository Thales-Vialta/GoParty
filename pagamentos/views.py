from django.shortcuts import render
from django.http import HttpResponse 

def historico_pagamentos(request): 
    return HttpResponse("Histórico de pagamentos do usuário.")
def checkout(request): 
    return HttpResponse("Tela de pagamento.")
