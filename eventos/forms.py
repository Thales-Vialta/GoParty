from django import forms 
from .models import eventos

class EventoForm(forms.ModelForm): 
    class Meta: 
        model = eventos
        fields = ['fornecedor','tipo_evento','data_evento','descricao','status','preco_total','data_pedido']