from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from .models import usuario

class CadastroForm(UserCreationForm): 
    class Meta: 
        model = usuario 
        fields = ['nome','email','senha','tipo','telefone']
        
class LoginForm(AuthenticationForm): 
    pass