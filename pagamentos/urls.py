from django.urls import path 
from . import views

urlpatterns = [
    path('',views.historico_pagamentos, name='historico_pagamentos'), 
    path('checkout/', views.checkout, name='checkout'), 
]
