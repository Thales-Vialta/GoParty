from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nome', 'data', 'local', 'descricao', 'fornecedor']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'local': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'fornecedor': forms.Select(attrs={'class': 'form-select'}),
        }
