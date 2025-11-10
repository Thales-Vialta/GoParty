from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Servico, Pagamento
from .forms import ServicoForm, PagamentoForm

@login_required
def listar_servico(request): 
    servicos = Servico.objects.filter(fornecedor=request.user)
    return render(request, 'pagamentos/listar_servico.html', {'servicos'},servicos)

@login_required
def criar_servico(request): 
    if request.method == 'POST': 
        form = ServicoForm(request.POST)
        if form.is_valid(): 
            servico = form.save(commit=False)
            servico.fornecedor = request.user 
            servico.save()
            return redirect('listar_servico')
    else: 
        form = ServicoForm() 
    return render(request, 'pagamentos/criar_servico.html',{'form':form})

@login_required
def historico_pagamentos(request): 
    pagamentos = Pagamento.objects.filter(evento_cliente=request.user)
    return render(request,'pagamentos/historico_pagamentos.html', {'pagamentos',pagamentos})
    
@login_required
def gerar_pagamento(request):
    if request.method == 'POST': 
        form = PagamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('historico_pagamentos')
    else: 
        form = PagamentoForm()
    return render(request,'pagamentos/gerar_pagamento.html', {'form':form})
