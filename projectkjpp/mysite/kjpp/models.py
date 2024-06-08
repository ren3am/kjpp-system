from django.db import models

# buat urusan database

class Pemberi_tugas(models.Model):
    pemberitugas_nama = models.CharField('Nama pemberi tugas', max_length=100, null=True)
    pemberitugas_alamat = models.CharField('Alamat pemberi tugas', max_length=100, null=True)
    pemberitugas_desa = models.CharField('Desa pemberi tugas', max_length=100, null=True)
    pemberitugas_kecamatan = models.CharField('Kecamatan pemberi tugas', max_length=100, null=True)
    pemberitugas_kabupaten = models.CharField('Kabupaten pemberi tugas', max_length=100, null=True)
    pemberitugas_provinsi = models.CharField('Provinsi pemberi tugas', max_length=100, null=True)
    
    def __str__(self):
        return self.pemberitugas_nama
    
class data_properti(models.Model):
    #properti
    properti_tipeproperti = models.CharField('Tipe properti', max_length=100)
    properti_luastanah = models.IntegerField('Luas tanah')
    properti_namadebitur = models.CharField('Nama debitur', max_length=100)
    properti_alamataset = models.CharField('Alamat Aset', max_length=300)
    properti_kelurahan = models.CharField('Kelurahan', max_length=100)
    properti_kecamatan = models.CharField('Kecamatan', max_length=100)
    properti_kabupaten = models.CharField('Kabupaten', max_length=100)
    properti_provinsi = models.CharField('Provinsi', max_length=100)
    properti_kodepos = models.CharField('Kode pos', max_length=10)
    properti_notelp = models.CharField('No Telp', max_length=15)
    properti_titikkoordinat = models.CharField('Titik Koordinat', max_length=100)
    properti_pencapaianlokasiaksesjalan = models.CharField('Pencapaian lokasi / akses jalan', max_length=100)
    properti_lebarjalandepanproperti = models.IntegerField('Lebar jalan depan properti')
    properti_kondisijalanmaterialjalan = models.CharField('Kondisi jalan / material jalan', max_length=100)
    properti_penghunipersilsaatini = models.CharField('Penghuni persil saat ini', max_length=100)
    properti_peruntukaneksisting = models.CharField('Peruntukan eksisting', max_length=100)
    status = models.CharField ('Status', max_length=30)
    properti_namabangunan = models.CharField('Nama Bangunan', max_length=100, default='Unknown')

    def __str__(self):
        return self.properti_alamataset
        
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

# class tenaga_ahli(models.Model):



class akun(models.Model): 
    username = models.CharField('username', max_length=100) 
    password = models.CharField('password', max_length=100) 

    def __str__(self):
        return self.username 


class PropertyData(models.Model):
    alamat_properti = models.CharField(max_length=255)
    titik_koordinat = models.CharField(max_length=100)
    rekaman_record = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=100)
    jenis_data = models.CharField(max_length=50, choices=[('Transaksi', 'Transaksi'), ('Penawaran', 'Penawaran')])
    jenis_properti = models.CharField(max_length=100)
    luas_tanah = models.DecimalField(max_digits=10, decimal_places=2)
    luas_bangunan = models.DecimalField(max_digits=10, decimal_places=2)
    unit_perbandingan = models.CharField(max_length=50)
    record = models.CharField(max_length=255)
    harga_penawaran = models.DecimalField(max_digits=15, decimal_places=2)
    diskon = models.DecimalField(max_digits=5, decimal_places=2)
    perkiraan_transaksi = models.DecimalField(max_digits=15, decimal_places=2)
    perkiraan_rcn = models.DecimalField(max_digits=15, decimal_places=2)
    indikasi_nilai_pasar_bangunan = models.DecimalField(max_digits=15, decimal_places=2)
    indikasi_nilai_tanah = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.alamat_properti
