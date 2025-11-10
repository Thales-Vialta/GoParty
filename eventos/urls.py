from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_eventos, name='eventos_lista'),
    path('novo/', views.novo_evento, name='novo_evento'),
    path('<int:id>/', views.detalhe_evento, name='detalhe_evento'),
]
