from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.lista_eventos, name='lista_eventos'), 
    path('novo/',views.criar_evento, name='criar_evento'),
]
