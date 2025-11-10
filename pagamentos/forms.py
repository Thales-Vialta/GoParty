from django import forms 
from .models import Servico, Pagamento

class ServicoForm(forms.ModelForm): 
    class Meta: 
        model = Servico 
        fields = ['nome','preco_base','descricao','ativo']
        
class PagamentoForm(forms.ModelForm): 
    class Meta: 
        model = Pagamento
        fields = ['valor','metodo','status','data_pagamento']