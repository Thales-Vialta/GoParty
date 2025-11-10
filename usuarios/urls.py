from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('logout/', views.logout_view, name='logout'),
]
