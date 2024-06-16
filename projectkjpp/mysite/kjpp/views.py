from django.shortcuts import render 
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import akun #buat akun register sama login
from .models import form_isian #buat file isian kertas kerja
from .models import objekProperti #objek properti laman bangunan buat test
from .models import pemberi_tugas
from .models import debitur
from .models import survei
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
    if request.method == 'POST':
        # ambil data dari formnya
        # nama modelsnya   =   nama di formnya(name)
        pemberitugas_alamat = request.POST.get('pemberitugas_alamat')
        pemberitugas_desa = request.POST.get('pemberitugas_desa')
        pemberitugas_kecamatan = request.POST.get('pemberitugas_kecamatan')
        pemberitugas_kabupaten = request.POST.get('pemberitugas_kabupaten')
        pemberitugas_provinsi = request.POST.get('pemberitugas_provinsi')
        #
        isian_suratorder_no = request.POST.get('isian_suratorder_no')
        isian_suratorder_tanggal = request.POST.get('isian_suratorder_tanggal')
        #
        isian_spk_no = request.POST.get('isian_spk_no')
        isian_spk_tanggal = request.POST.get('isian_spk_tanggal')
        #
        survei_nosurattugas = request.POST.get('survei_nosurattugas')
        survei_tanggal = request.POST.get('survei_tanggal')
        survei_pukul = request.POST.get('survei_pukul')
        #
        isian_tujuanpenilaian = request.POST.get('isian_tujuanpenilaian')
        isian_kantorkjpp = request.POST.get('isian_kantorkjpp')
        isian_pendampinginspeksi = request.POST.get('isian_pendampinginspeksi')
        #
        properti_tipeproperti = request.POST.get('properti_tipeproperti')
        properti_luastanah = request.POST.get('properti_luastanah')
        debitur_namadebitur = request.POST.get('debitur_namadebitur')
        properti_alamataset = request.POST.get('properti_alamataset')
        properti_kecamatan = request.POST.get('properti_kecamatan')
        properti_kabupaten = request.POST.get('properti_kabupaten')
        properti_propinsi = request.POST.get('properti_propinsi')
        properti_kodepos = request.POST.get('properti_kodepos')
        properti_notelp = request.POST.get('properti_notelp')
        properti_titikkoordinat = request.POST.get('properti_titikkoordinat')
        properti_pencapaianlokasiaksesjalan = request.POST.get('properti_pencapaianlokasiaksesjalan')
        properti_lebarjalandepanproperti = request.POST.get('properti_lebarjalandepanproperti')
        properti_kondisijalanmaterialjalan = request.POST.get('properti_kondisijalanmaterialjalan')
        properti_penghunipersilsaatini = request.POST.get('properti_penghunipersilsaatini')
        properti_peruntukaneksisting = request.POST.get('properti_peruntukaneksisting')


        # Basic validation isi semua atau nggak
        if all([pemberitugas_alamat, pemberitugas_desa, pemberitugas_kecamatan, pemberitugas_kabupaten,
                pemberitugas_provinsi, isian_suratorder_no, isian_suratorder_tanggal, isian_spk_no,
                isian_spk_tanggal, survei_nosurattugas, survei_tanggal, survei_pukul,
                isian_tujuanpenilaian, isian_kantorkjpp, isian_pendampinginspeksi, properti_tipeproperti,
                properti_luastanah, debitur_namadebitur, properti_alamataset, properti_kecamatan,
                properti_kabupaten, properti_propinsi, properti_kodepos, properti_notelp,
                properti_titikkoordinat, properti_pencapaianlokasiaksesjalan,
                properti_lebarjalandepanproperti, properti_kondisijalanmaterialjalan,
                properti_penghunipersilsaatini, properti_peruntukaneksisting]):
            new_properti = objekProperti(
                properti_tipeproperti = properti_tipeproperti,
                properti_luastanah = properti_luastanah,
                properti_alamataset = properti_alamataset,
                properti_kecamatan = properti_kecamatan,
                properti_kabupaten = properti_kabupaten,
                properti_propinsi = properti_propinsi,
                properti_kodepos = properti_kodepos,
                properti_notelp = properti_notelp,
                properti_titikkoordinat = properti_titikkoordinat,
                properti_pencapaianlokasiaksesjalan = properti_pencapaianlokasiaksesjalan,
                properti_penghunipersilsaatini = properti_penghunipersilsaatini,
                properti_peruntukaneksisting = properti_peruntukaneksisting,

            )
            new_properti.save()

            new_pemberitugas = pemberi_tugas(
                pemberitugas_alamat = pemberitugas_alamat,
                pemberitugas_desa = pemberitugas_desa,
                pemberitugas_kecamatan = pemberitugas_kecamatan,
                pemberitugas_kabupaten = pemberitugas_kabupaten,
                pemberitugas_provinsi = pemberitugas_provinsi,
            )
            new_pemberitugas.save()

            new_formisian = form_isian(
                isian_suratorder_no = isian_suratorder_no,
                isian_suratorder_tanggal = isian_suratorder_tanggal,
                #
                isian_tujuanpenilaian = isian_tujuanpenilaian,
                isian_kantorkjpp = isian_kantorkjpp,
                isian_pendampinginspeksi = isian_pendampinginspeksi,
            )
            new_formisian.save()

            new_survei = survei(
                survei_nosurattugas=survei_nosurattugas,
                survei_tanggal = survei_tanggal,
                survei_pukul = survei_pukul,
            )
            new_survei.save()

            new_debitur = debitur(
                debitur_namadebitur = debitur_namadebitur,
            )
            new_debitur.save()


            
            return redirect('kertaskerja')  # Ensure you have a URL named 'success_page'
        else:
            return render(request, 'kertaskerja_bangunan.html', {'error': 'All fields are required.'})
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
        # ambil data dari formnya
        # nama modelsnya   =   nama di formnya
        properti_propinsi = request.POST.get('properti_propinsi')
        properti_kabupaten = request.POST.get('properti_kabupaten')
        properti_tipebangunan = request.POST.get('properti_tipebangunan')
        properti_namabangunan = request.POST.get('properti_namabangunan')
        properti_noimb = request.POST.get('properti_noimb')
        properti_luasdilapangan = request.POST.get('properti_luasdilapangan')
        properti_jumlahlantai = request.POST.get('properti_jumlahlantai')
        properti_tahunbangun = request.POST.get('properti_tahunbangun')
        properti_tahunrenovasi = request.POST.get('properti_tahunrenovasi')
        properti_tahunpenilaian = request.POST.get('properti_tahunpenilaian')
        properti_umurekonomis = request.POST.get('properti_umurekonomis')
        properti_ikk = request.POST.get('properti_ikk')
        properti_ilm = request.POST.get('properti_ilm')

        # Basic validation isi semua atau nggak
        if all([properti_propinsi, properti_kabupaten, properti_tipebangunan,
                properti_namabangunan, properti_noimb, properti_luasdilapangan,
                properti_jumlahlantai, properti_tahunbangun, properti_tahunrenovasi,
                properti_tahunpenilaian, properti_umurekonomis]):
            new_properti = objekProperti(
                properti_propinsi=properti_propinsi,
                properti_kabupaten=properti_kabupaten,
                properti_tipebangunan=properti_tipebangunan,
                properti_namabangunan=properti_namabangunan,
                properti_noimb=properti_noimb,
                properti_luasdilapangan=properti_luasdilapangan,
                properti_jumlahlantai = properti_jumlahlantai,
                properti_tahunbangun = properti_tahunbangun,
                properti_tahunrenovasi = properti_tahunrenovasi,
                properti_tahunpenilaian = properti_tahunpenilaian,
                properti_umurekonomis = properti_umurekonomis,
                properti_ikk = properti_ikk,
                properti_ilm = properti_ilm,
            )
            new_properti.save()
            return redirect('kertaskerja')  # Ensure you have a URL named 'success_page'
        else:
            return render(request, 'kertaskerja_bangunan.html', {'error': 'All fields are required.'})
    return render(request, 'kertaskerja_bangunan.html')





# views.py 






