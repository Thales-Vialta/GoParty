from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Evento
from .forms import EventoForm

@login_required
def lista_eventos(request):
    eventos = Evento.objects.filter(cliente=request.user)
    return render(request, 'eventos/lista_eventos.html', {'eventos': eventos})

@login_required
def novo_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.cliente = request.user
            evento.save()
            return redirect('eventos_lista')
    else:
        form = EventoForm()
    return render(request, 'eventos/novo_evento.html', {'form': form})

@login_required
def detalhe_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    return render(request, 'eventos/detalhe_evento.html', {'evento': evento})
