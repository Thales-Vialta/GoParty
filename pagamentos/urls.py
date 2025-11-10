from django.urls import path 
from . import views

urlpatterns = [
    path('servicos/', views.listar_servico, name='listar_servico'),
    path('servicos/novo/',views.criar_servico, name='criar_servico'),
    path('',views.historico_pagamentos, name='historico_pagamentos'), 
    path('novo/', views.checkout, name='gerar_pagamento'), 
]
