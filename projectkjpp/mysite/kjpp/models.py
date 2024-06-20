from django.db import models
from django.contrib.auth.models import User

# buat urusan database

class customer (models.Model):
    nama_cust = models.CharField('Nama customer', max_length=100, null=True, blank=True)
    alamat_cust = models.CharField('Alamat customer', max_length=100, null=True, blank=True)
    desa_cust = models.CharField('Desa customer', max_length=100, null=True, blank=True)
    kecamatan_cust = models.CharField('Kecamatan customer', max_length=100, null=True, blank=True)
    kabupaten_cust = models.CharField('Kabupaten customer', max_length=100, null=True, blank=True)
    provinsi_cust = models.CharField('Provinsi customer', max_length=100, null=True, blank=True)

    def __str__(self) :
        return self.nama_cust

class form_isian(models.Model):
    pemberitugas = models.ForeignKey(customer, on_delete=models.CASCADE, blank=True, null=True)
    isian_suratorder_no = models.CharField('No Surat Order', max_length=30, blank=True, null=True)
    isian_suratorder_tanggal = models.DateField('Tanggal Surat Order', blank=True, null=True)
    isian_tujuanpenilaian = models.CharField('Tujuan penilaian', max_length=100, blank=True, null=True)
    isian_kantorkjpp = models.CharField('Kantor KJPP', max_length=100, blank=True, null=True)
    isian_pendampinginspeksi = models.CharField('Pendamping inspeksi', max_length=100, blank=True, null=True)
    isian_spk_no = models.CharField('No SPK', max_length=30, blank=True, null=True)
    isian_spk_tanggal = models.DateField('Tanggal SPK', blank=True, null=True)
    
    def __str__(self):
        return self.isian_suratorder_no
    
class survei(models.Model):
    survei_nosurattugas = models.CharField('No surat tugas', max_length=30, null=True, blank=True)
    survei_tanggal = models.DateField('Tanggal Survei', null=True, blank=True)
    survei_tahun = models.IntegerField('Tahun survei', null=True, blank=True)
    survei_pukul = models.CharField('Waktu survei', max_length=10, null=True)
    isian = models.OneToOneField(form_isian, on_delete=models.CASCADE)

    def __str__(self):
        return self.survei_nosurattugas

    

# class tenaga_ahli(models.Model):

class pegawai(models.Model):
    pegawai_id = models.CharField('Id pegawai', max_length=100, null=True, blank=True)
    pegawai_nama = models.CharField('Nama pegawai', max_length=100, null=True, blank=True)
    pegawai_nomappi = models.CharField('No MAPPI pegawai', max_length=100, null=True, blank=True)
    pegawai_noregister = models.CharField('No register pegawai', max_length=100, null=True, blank=True)
    survei = models.ManyToManyField(survei, through="detail_survei")

    def __str__(self):
        return self.pegawai_nama

#intermediary many to many

class detail_survei(models.Model):
    pegawai = models.ForeignKey(pegawai, on_delete=models.CASCADE)
    survei = models.ForeignKey(survei, on_delete=models.CASCADE)
    surveidate = models.DateField()

# intermediary end

class akun(models.Model): 
    username = models.CharField('username', max_length=100) 
    password = models.CharField('password', max_length=100) 

    def __str__(self):
        return self.username
    
class debitur(models.Model):
    debitur_namadebitur = models.CharField('Nama debitur', max_length=300, null=True, blank=True)
    debitur_alamat = models.CharField('Alamat debitur', max_length=300, null=True, blank=True)
    debitur_desa = models.CharField('Desa debitur', max_length=30, null=True, blank=True)
    debitur_kecamatan = models.CharField('Kecamatan debitur', max_length=30, null=True, blank=True)
    debitur_kabupaten = models.CharField('Desa debitur', max_length=30, null=True, blank=True)
    debitur_propinsi = models.CharField('Propinsi debitur', max_length=30, null=True, blank=True)
    isian = models.OneToOneField(form_isian, on_delete=models.CASCADE)
    
#TEST DATABASE KERTAS KERJA BANGUNAN

class objekProperti(models.Model):
    #relationship
    survei = models.OneToOneField(survei, on_delete=models.CASCADE, primary_key=True)
    #
    properti_tipeproperti = models.CharField('Tipe properti', max_length=200, null=True, blank=True)
    properti_luastanah = models.CharField('Luas tanah', max_length=200, null=True, blank=True)
    properti_alamataset = models.CharField('Alamat aset', max_length=200, null=True, blank=True)
    #
    properti_propinsi = models.CharField('Provinsi properti', max_length=200, null=True, blank=True)
    properti_kabupaten = models.CharField('Kabupaten properti', max_length=200, null=True, blank=True)
    properti_kecamatan = models.CharField('Kecamatan properti', max_length=200, null=True, blank=True)
    #
    properti_kodepos = models.CharField('Kode Pos', max_length=200, null=True, blank=True)
    properti_notelp = models.CharField('No Telp', max_length=200, null=True, blank=True)
    properti_titikkoordinat = models.CharField('Titik Koordinat', max_length=200, null=True, blank=True)
    properti_pencapaianlokasiaksesjalan = models.CharField('Pencapaian Lokasi / Akses Jalan', max_length=200, null=True, blank=True)
    properti_lebarjalandepanproperti = models.CharField('Lebar jalan depan properti', max_length=200, null=True, blank=True)
    properti_kondisijalanmaterialjalan = models.CharField('Kondisi jalan / material jalan', max_length=200, null=True, blank=True)
    properti_penghunipersilsaatini = models.CharField('Penghuni persil saat ini', max_length=200, null=True, blank=True)
    properti_peruntukaneksisting = models.CharField('Peruntukan eksisting', max_length=200, null=True, blank=True)
    # bangunan
    properti_tipebangunan = models.CharField('Tipe bangunan', max_length=200, null=True, blank=True)
    properti_namabangunan = models.CharField('Nama bangunan', max_length=200, null=True, blank=True)
    properti_noimb = models.CharField('No imb', max_length=200, null=True, blank=True)
    properti_luasdilapangan = models.CharField('', max_length=200, null=True, blank=True)
    properti_noimb = models.CharField('No imb', max_length=200, null=True, blank=True)
    # properti_luassesuailist = models.CharField('Luas sesuai list', max_length=200, null=False, blank=False)
    properti_jumlahlantai = models.CharField('Jumlah lantai', max_length=200, null=True, blank=True, default='0')
    properti_tahunbangun = models.CharField('Tahun bangun', max_length=200, null=True, blank=True, default='0')
    properti_tahunrenovasi = models.CharField('Tahun renovasi', max_length=200, null=True, blank=True, default='0')
    properti_tahunpenilaian = models.CharField('Tahun penilaian', max_length=200, null=True, blank=True, default='0')
    properti_umurekonomis = models.CharField('Umur ekonomis', max_length=200, null=True, blank=True, default='0')
    properti_ikk = models.CharField('IKK', max_length=200, null=True, blank=True, default='0')
    properti_ilm = models.CharField('ILM', max_length=200, null=True, blank=True, default='0')
    

    def __str__(self) :
        return self.properti_namabangunan
    
   
class customerData (models.Model):
    customer_nama = models.CharField('Nama customer', max_length=100)

    def __str__(self) :
        return self.customer_nama
    
class pemberi_tugas(models.Model):
    pemberitugas_nama = models.CharField('Nama pemberi tugas', max_length=100, null=True, blank=True)
    pemberitugas_alamat = models.CharField('Alamat pemberi tugas', max_length=100, null=True, blank=True)
    pemberitugas_desa = models.CharField('Desa pemberi tugas', max_length=100, null=True, blank=True)
    pemberitugas_kecamatan = models.CharField('Kecamatan pemberi tugas', max_length=100, null=True, blank=True)
    pemberitugas_kabupaten = models.CharField('Kabupaten pemberi tugas', max_length=100, null=True, blank=True)
    pemberitugas_provinsi = models.CharField('Provinsi pemberi tugas', max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.pemberitugas_nama
    



    


