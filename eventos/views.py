from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import eventos 
from .forms import EventoForm

@login_required
def lista_eventos(request): 
    if request.user.tipo == 'cliente': 
        Eventos = eventos.objects.filter(cliente=request.user)
    else: 
        Eventos = eventos.objects.filter(fornecedor=request.user)
    return render(request,'eventos/list.html', {'eventos':Eventos}
                  )
@login_required
def criar_evento(request):
    if request.metho == 'POST': 
        form = EventoForm(request.POST)
        if form.is_valid(): 
            evento = form.save(commit=False)
            evento.cliente = request.user 
            evento.save( )
            return redirect('lista_eventos') 
    else: 
        form = EventoForm()
    return render(request, 'eventos/create.html',{'form':form})


# Create your views here.
