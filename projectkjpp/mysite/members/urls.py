from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='login'),
    path('login_user', views.login_user, name="login"),
]