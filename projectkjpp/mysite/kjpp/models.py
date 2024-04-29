from django.db import models

# buat urusan database

class Pemberi_tugas(models.Model):
    alamat = models.CharField('Alamat Pemberi Tugas', max_length=300)
    desa = models.CharField('Desa Pemberi Tugas', max_length=300)
    kecamatan = models.CharField('Kecamatan Pemberi Tugas', max_length=300)
    kabupaten = models.CharField('Kabupaten Pemberi Tugas', max_length=300)
    propinsi = models.CharField('Propinsi Pemberi Tugas', max_length=300)

    def __str__(self):
        return self.alamat
    
    #buat munculin list alamat di admin area 

class akun(models.Model): 
    username = models.CharField('username', max_length=300) 
    password = models.CharField('password', max_length=300) 
