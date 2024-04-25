from django.shortcuts import render

def login(request):
    return render(request, 'login.html', {})

def kertaskerja(request):
    return render(request, 'kertaskerja.html', {}) 

def register(request): 
    return render(request, 'register.html', {})
