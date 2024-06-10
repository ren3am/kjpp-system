from django.shortcuts import render 
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import akun #buat akun register sama login
from .models import form_isian #buat file isian kertas kerja
from .models import objekProperti #objek properti laman bangunan buat test
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

def kertaskerjatanah(request):
    return render(request, 'kertaskerja_tanah.html', {})

# def kertaskerjabangunan(request):
#     if request.method == 'POST':
#         # nama modelsnya   =   nama name di formnya
#         properti_propinsi = request.POST['properti_propinsi']
#         properti_kabupaten = request.POST['properti_kabupaten']
#         properti_tipebangunan = request.post['properti_tipebangunan']
#         properti_namabangunan = request.POST['properti_namabangunan']
#         properti_noimb = request.POST['properti_noimb']
#         properti_luasdilapangan = request.POST['properti_luasdilapangan']

#         new_properti = objekProperti(properti_propinsi=properti_propinsi,
#                                      properti_kabupaten=properti_kabupaten,
#                                      properti_tipebangunan=properti_tipebangunan,
#                                      properti_namabangunan=properti_namabangunan,
#                                      properti_noimb=properti_noimb,
#                                      properti_luasdilapangan=properti_luasdilapangan)
#         new_properti.save()


#     return render(request, 'kertaskerja_bangunan.html', {}) 

def kertaskerjabangunan(request):
    if request.method == 'POST':
        # nama modelsnya   =   nama di formnya
        properti_propinsi = request.POST.get('properti_propinsi')
        properti_kabupaten = request.POST.get('properti_kabupaten')
        properti_tipebangunan = request.POST.get('properti_tipebangunan')
        properti_namabangunan = request.POST.get('properti_namabangunan')
        properti_noimb = request.POST.get('properti_noimb')
        properti_luasdilapangan = request.POST.get('properti_luasdilapangan')

        # Optional: Add basic validation
        if all([properti_propinsi, properti_kabupaten, properti_tipebangunan,
                properti_namabangunan, properti_noimb, properti_luasdilapangan]):
            new_properti = objekProperti(
                properti_propinsi=properti_propinsi,
                properti_kabupaten=properti_kabupaten,
                properti_tipebangunan=properti_tipebangunan,
                properti_namabangunan=properti_namabangunan,
                properti_noimb=properti_noimb,
                properti_luasdilapangan=properti_luasdilapangan
            )
            new_properti.save()
            return redirect('kertaskerja')  # Ensure you have a URL named 'success_page'
        else:
            return render(request, 'kertaskerja_bangunan.html', {'error': 'All fields are required.'})
    return render(request, 'kertaskerja_bangunan.html')





# views.py 






