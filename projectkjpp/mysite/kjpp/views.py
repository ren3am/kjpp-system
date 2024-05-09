from django.shortcuts import render 
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import akun
from .forms import LoginForm 
from .forms import MyForm   

def login(request):    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            Akun = akun.objects.get(username=username, password=password)
            # If user exists, redirect to a success page
            return redirect('main_page')
        except akun.DoesNotExist:
            # If user doesn't exist, show an error message
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def kertaskerja(request):
    return render(request, 'kertaskerja.html', {}) 

def register(request): 
    return render(request, 'register.html', {})  

def main_page(request): 
    akuns = akun.objects.all()
    return render(request, 'main_page.html', {"akuns" : akuns}) 




# views.py 






