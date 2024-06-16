from django.db import models

# buat urusan database

# class Pemberi_tugas(models.Model):
#     pemberitugas_nama = models.CharField('Nama pemberi tugas', max_length=100, null=True)
#     pemberitugas_alamat = models.CharField('Alamat pemberi tugas', max_length=100, null=True)
#     pemberitugas_desa = models.CharField('Desa pemberi tugas', max_length=100, null=True)
#     pemberitugas_kecamatan = models.CharField('Kecamatan pemberi tugas', max_length=100, null=True)
#     pemberitugas_kabupaten = models.CharField('Kabupaten pemberi tugas', max_length=100, null=True)
#     pemberitugas_provinsi = models.CharField('Provinsi pemberi tugas', max_length=100, null=True)
    
#     def __str__(self):
#         return self.pemberitugas_nama
    
# class data_properti(models.Model):
#     #properti
#     properti_tipeproperti = models.CharField('Tipe properti', max_length=100)
#     properti_luastanah = models.IntegerField('Luas tanah')
#     properti_namadebitur = models.CharField('Nama debitur', max_length=100)
#     properti_alamataset = models.CharField('Alamat Aset', max_length=300)
#     properti_kelurahan = models.CharField('Kelurahan', max_length=100)
#     properti_kecamatan = models.CharField('Kecamatan', max_length=100)
#     properti_kabupaten = models.CharField('Kabupaten', max_length=100)
#     properti_provinsi = models.CharField('Provinsi', max_length=100)
#     properti_kodepos = models.CharField('Kode pos', max_length=10)
#     properti_notelp = models.CharField('No Telp', max_length=15)
#     properti_titikkoordinat = models.CharField('Titik Koordinat', max_length=100)
#     properti_pencapaianlokasiaksesjalan = models.CharField('Pencapaian lokasi / akses jalan', max_length=100)
#     properti_lebarjalandepanproperti = models.IntegerField('Lebar jalan depan properti')
#     properti_kondisijalanmaterialjalan = models.CharField('Kondisi jalan / material jalan', max_length=100)
#     properti_penghunipersilsaatini = models.CharField('Penghuni persil saat ini', max_length=100)
#     properti_peruntukaneksisting = models.CharField('Peruntukan eksisting', max_length=100)
#     status = models.CharField ('Status', max_length=30)
#     properti_namabangunan = models.CharField('Nama Bangunan', max_length=100, default='Unknown')

#     def __str__(self):
#         return self.properti_alamataset
        
class form_isian(models.Model):
    #isian
    isian_suratorder_no = models.CharField('No Surat Order', max_length=30)
    isian_suratorder_tanggal = models.DateField('Tanggal Surat Order')
    isian_tujuanpenilaian = models.CharField('Tujuan penilaian', max_length=100)
    isian_kantorkjpp = models.CharField('Kantor KJPP', max_length=100)
    isian_pendampinginspeksi = models.CharField('Pendamping inspeksi', max_length=100)
    isian_spk_no = models.CharField('No SPK', max_length=30)
    isian_spk_tanggal = models.DateField('Tanggal SPK')
    
    def __str__(self):
        return self.isian_suratorder_no
    
    #buat munculin list alamat di admin area 

class survei(models.Model):
    survei_nosurattugas = models.CharField('No surat tugas', max_length=30, null=True)
    survei_tanggal = models.DateField('Tanggal Survei')
    survei_tahun = models.IntegerField('Tahun survei')
    survei_pukul = models.CharField('Waktu survei', max_length=10, null=True)
    
    def __str__(self):
        return self.survei_nosurattugas
    
class form_isian(models.Model):
    isian_suratorder_no = models.CharField('Surat order no', max_length=100, null=True, blank=True)
    isian_suratorder_tanggal = models.CharField('Surat order tanggal', max_length=100, null=True, blank=True)
    isian_tujuanpenilaian = models.CharField('Tujuan penilaian', max_length=100, null=True, blank=True)
    isian_kantorkjpp = models.CharField('Kantor KJPP', max_length=100, null=True, blank=True)
    isian_pendampinginspeksi = models.CharField('Tujuan penilaian', max_length=100, null=True, blank=True)
    isian_spk_no = models.CharField('Spk no', max_length=100, null=True, blank=True)
    isian_spk_tanggal = models.CharField('Spk tanggal', max_length=100, null=True, blank=True)

    def __str__(self):
        return self.isian_suratorder_no

class pemberi_tugas(models.Model):
    pemberitugas_nama = models.CharField('Nama pemberi tugas', max_length=100, null=True, blank=True)
    pemberitugas_alamat = models.CharField('Alamat pemberi tugas', max_length=100, null=True, blank=True)
    pemberitugas_desa = models.CharField('Desa pemberi tugas', max_length=100, null=True, blank=True)
    pemberitugas_kecamatan = models.CharField('Kecamatan pemberi tugas', max_length=100, null=True, blank=True)
    pemberitugas_kabupaten = models.CharField('Kabupaten pemberi tugas', max_length=100, null=True, blank=True)
    pemberitugas_provinsi = models.CharField('Provinsi pemberi tugas', max_length=100, null=True, blank=True)

# class tenaga_ahli(models.Model):

class pegawai(models.Model):
    pegawai_id = models.CharField('Id pegawai', max_length=100, null=True, blank=True)
    pegawai_nama = models.CharField('Nama pegawai', max_length=100, null=True, blank=True)
    pegawai_nomappi = models.CharField('No MAPPI pegawai', max_length=100, null=True, blank=True)
    pegawai_noregister = models.CharField('No register pegawai', max_length=100, null=True, blank=True)

class akun(models.Model): 
    username = models.CharField('username', max_length=100) 
    password = models.CharField('password', max_length=100) 

    def __str__(self):
        return self.username
    
class debitur(models.Model):
    debitur_alamat = models.CharField('Alamat debitur', max_length=300, null=True, blank=True)
    debitur_desa = models.CharField('Desa debitur', max_length=30, null=True, blank=True)
    debitur_kecamatan = models.CharField('Kecamatan debitur', max_length=30, null=True, blank=True)
    debitur_kabupaten = models.CharField('Desa debitur', max_length=30, null=True, blank=True)
    debitur_propinsi = models.CharField('Propinsi debitur', max_length=30, null=True, blank=True)
    
#TEST DATABASE KERTAS KERJA BANGUNAN

class objekProperti(models.Model):
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
    


