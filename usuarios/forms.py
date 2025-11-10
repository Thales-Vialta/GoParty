from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Usuário', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class CadastroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password_confirm = forms.CharField(label='Confirme a Senha', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password') != cleaned_data.get('password_confirm'):
            raise forms.ValidationError('As senhas não coincidem.')
        return cleaned_data
