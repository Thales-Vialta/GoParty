from django.db import models
class eventos(models.Model): 
    eventos_tipo = [('Aniversário','aniversário'),('Formatura','formatura'),('Colônia de férias','colônia de férias')]
    cliente = models.ForeignKey('usuarios.Cliente', on_delete=models.CASCADE)
    fornecedor = models.ForeignKey('usuarios.Fornecedor', on_delete=models.CASCADE)
    tipo_evento = models.CharField(choices = eventos_tipo)
    data_evento = models.DateField()
    descricao = models.TextField(blank=True)
    status = models.CharField(max_length=20,choices=[
       ('pendente','Pendente'), 
       ('aprovado','Aprovado'),
       ('concluido','Concluído'), 
       ('cancelado','Cancelado') 
    ], default='pendente')
    preco_total = models.DecimalField(max_digits=10,decimal_places=2)
    data_pedido = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.titulo} solicitado'
    