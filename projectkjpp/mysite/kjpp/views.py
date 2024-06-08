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

def kertaskerjatanah(request): 
    fields = [
        "Alamat Properti",
        "Titik Koordinat",
        "Rekaman / Record",
        "Contact Person",  
    ]  
    fields2 = [
        "Jenis Properti",
        "Luas Tanah",
        "Luas Bangunan",
        "Unit Perbandingan",
        "Record",
        "Harga Penawaran",
        "Diskon",
        "Perkiraan Transaksi",
        "Perkiraan RCN",
    ] 
    fields3 = [
         "Indikasi Nilai Tanah"
    ]
    if request.method == 'POST':
        PropertyData.objects.create(
            alamat_properti=request.POST['alamat_properti'],
            titik_koordinat=request.POST['titik_koordinat'],
            rekaman_record=request.POST['rekaman_record'],
            contact_person=request.POST['contact_person'],
            jenis_data=request.POST['jenis_data'],
            jenis_properti=request.POST['jenis_properti'],
            luas_tanah=request.POST['luas_tanah'],
            luas_bangunan=request.POST['luas_bangunan'],
            unit_perbandingan=request.POST['unit_perbandingan'],
            record=request.POST['record'],
            harga_penawaran=request.POST['harga_penawaran'],
            diskon=request.POST['diskon'],
            perkiraan_transaksi=request.POST['perkiraan_transaksi'],
            perkiraan_rcn=request.POST['perkiraan_rcn'],
            indikasi_nilai_pasar_bangunan=request.POST['indikasi_nilai_pasar_bangunan'],
            indikasi_nilai_tanah=request.POST['indikasi_nilai_tanah']
        )
        return redirect('success') 
    return render(request, 'kertaskerja_tanah.html', {'fields': fields , 'fields2' : fields2 , 'fields3' : fields3}) 


def kertaskerjabangunan(request):
    return render(request, 'kertaskerja_bangunan.html', {}) 




# views.py 






