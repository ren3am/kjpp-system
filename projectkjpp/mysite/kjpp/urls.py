from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('kertaskerja', views.kertaskerja, name='kertaskerja'),
    path('dashboard', views.dashboard, name='dashboard')
]