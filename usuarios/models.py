from django.db import models
class usuario(models.Model):
    escolha_tipo = [('cliente','Cliente'),('fornecedor','Fornecedor'),('Admin','Administrador')] 
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices = escolha_tipo)
    telefone = models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return f'{self.nome} cadastrado com sucesso'
class Cliente(usuario):
    cpf = models.CharField(max_length=14, unique=True),
    endereco = models.CharField(max_length=200)
class Fornecedor(usuario): 
    cnpj = models.CharField(max_length=18,unique=True)
    categoria = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
        
        