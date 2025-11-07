from django.contrib import admin
from .models import usuario, Cliente, Fornecedor

admin.site.register(usuario)
admin.site.register(Cliente)
admin.site.register(Fornecedor)
