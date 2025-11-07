from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='usuarios_index'),
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
]
