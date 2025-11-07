from django.db import models

class Pagamento(models.Model): 
    evento = models.ForeignKey('eventos.eventos', on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    metodo = models.CharField(
        max_length=20, 
        choices=[
            ('pix', 'Pix'), 
            ('cartao_credito', 'Cartão de Crédito'),
            ('cartao_debito', 'Cartão de Débito'),
            ('boleto', 'Boleto')
        ]
    )
    status = models.CharField(
        max_length=20,
        choices=[('pendente', 'Pendente'), ('pago', 'Pago'), ('falhou', 'Falhou')],
        default='pendente'
    )
    data_pagamento = models.DateTimeField(auto_now_add=True)

class Servico(models.Model):
    fornecedor = models.ForeignKey('usuarios.Fornecedor', on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    preco_base = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} - {self.fornecedor.nome}"
