from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'), 
    path('register' ,views.register, name='register'),
    path('kertaskerja', views.kertaskerja, name='kertaskerja') , 
    path('main_page', views.main_page,  name='main_page'),
    path('kertaskerja/tanah', views.kertaskerjatanah, name="kertaskerjatanah"),
    path('kertaskerja/bangunan', views.kertaskerjabangunan, name="kertaskerjabangunan"),
  
]