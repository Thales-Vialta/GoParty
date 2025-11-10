from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, CadastroForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('eventos_lista')
    else:
        form = LoginForm()
    return render(request, 'usuarios/login.html', {'form': form})

def cadastro_view(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('eventos_lista')
    else:
        form = CadastroForm()
    return render(request, 'usuarios/cadastro.html', {'form': form})

@login_required
def perfil_view(request):
    return render(request, 'usuarios/perfil.html', {'usuario': request.user})

def logout_view(request):
    logout(request)
    return redirect('login')
