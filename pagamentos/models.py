from django.db import models

# Create your models here.
class Pagamento(models.Model): 
    evento = models.ForeignKey('Evento',on_delete=models.CASCADE)
    