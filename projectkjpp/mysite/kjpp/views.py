from django.shortcuts import render 
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import akun #buat akun register sama login
from .models import form_isian #buat file isian kertas kerja
from .forms import LoginForm 
from .forms import MyForm
from .forms import RegisterForm

def login(request):    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            Akun = akun.objects.get(username=username, password=password)
            # If user exists, redirect to a success page
            # return redirect('main_page')
            return redirect('kertaskerja') #placeholder blm ada main page
        except akun.DoesNotExist:
            # If user doesn't exist, show an error message
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def kertaskerja(request):
    return render(request, 'kertaskerja.html', {}) 

def register(request): 
    if request.POST:
        registerform = RegisterForm(request.POST, request.FILES)
        print(request.FILES)
        if registerform.is_valid():
            registerform.save()
        return redirect(login)
    return render(request, 'register.html', {'form' : RegisterForm})  

def main_page(request): 
    akuns = akun.objects.all()
    return render(request, 'main_page.html', {"akuns" : akuns}) 




# views.py 






