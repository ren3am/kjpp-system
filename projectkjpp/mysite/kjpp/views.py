from django.shortcuts import render

def login(request):
    return render(request, 'login.html', {})

def kertaskerja(request):
    return render(request, 'kertaskerja_test.html', {})

def dashboard(request):
    return render(request, 'dashboard.html', {})
