# Generated by Django 5.0.6 on 2024-06-02 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kjpp', '0006_alter_form_isian_properti_namabangunan'),
    ]

    operations = [
        migrations.CreateModel(
            name='data_properti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('properti_tipeproperti', models.CharField(max_length=100, verbose_name='Tipe properti')),
                ('properti_luastanah', models.IntegerField(verbose_name='Luas tanah')),
                ('properti_namadebitur', models.CharField(max_length=100, verbose_name='Nama debitur')),
                ('properti_alamataset', models.CharField(max_length=300, verbose_name='Alamat Aset')),
                ('properti_kelurahan', models.CharField(max_length=100, verbose_name='Kelurahan')),
                ('properti_kecamatan', models.CharField(max_length=100, verbose_name='Kecamatan')),
                ('properti_kabupaten', models.CharField(max_length=100, verbose_name='Kabupaten')),
                ('properti_provinsi', models.CharField(max_length=100, verbose_name='Provinsi')),
                ('properti_kodepos', models.CharField(max_length=10, verbose_name='Kode pos')),
                ('properti_notelp', models.CharField(max_length=15, verbose_name='No Telp')),
                ('properti_titikkoordinat', models.CharField(max_length=100, verbose_name='Titik Koordinat')),
                ('properti_pencapaianlokasiaksesjalan', models.CharField(max_length=100, verbose_name='Pencapaian lokasi / akses jalan')),
                ('properti_lebarjalandepanproperti', models.IntegerField(verbose_name='Lebar jalan depan properti')),
                ('properti_kondisijalanmaterialjalan', models.CharField(max_length=100, verbose_name='Kondisi jalan / material jalan')),
                ('properti_penghunipersilsaatini', models.CharField(max_length=100, verbose_name='Penghuni persil saat ini')),
                ('properti_peruntukaneksisting', models.CharField(max_length=100, verbose_name='Peruntukan eksisting')),
                ('status', models.CharField(max_length=30, verbose_name='Status')),
                ('properti_namabangunan', models.CharField(default='Unknown', max_length=100, verbose_name='Nama Bangunan')),
            ],
        ),
        migrations.RemoveField(
            model_name='form_isian',
            name='pemberitugas_alamat',
        ),
        migrations.RemoveField(
            model_name='form_isian',
            name='pemberitugas_desa',
        ),
        migrations.RemoveField(
            model_name='form_isian',
            name='pemberitugas_kabupaten',
        ),
        migrations.RemoveField(
            model_name='form_isian',
            name='pemberitugas_kecamatan',
        ),
        migrations.RemoveField(
            model_name='form_isian',
            name='pemberitugas_nama',
        ),
        migrations.RemoveField(
            model_name='form_isian',
            name='pemberitugas_provinsi',
        ),
        migrations.RemoveField(
            model_name='form_isian',
            name='properti_alamataset',
        ),
        migrations.RemoveField(
            model_name='form_isian',
            name='properti_kabupaten',
        ),
        migrations.RemoveField(
            model_name='form_isian',
            name='properti_kecamatan',
        ),
        migrations.RemoveField(
            model_name='form_isian',
            name='properti_kelurahan',
        ),
        migrations.RemoveField(
            model_name='form_isian',
            name='properti_kodepos',
        ),
        migrations.RemoveField(
            model_name='form_isian',
            name='properti_kondisijalanmaterialjalan',
        ),
        migrations.RemoveField(
            model_name='form_isian',
            name='properti_lebarjalandepanproperti',
        ),
        migrations.RemoveField(
            model_name='form_isian',
            name='properti_luastanah',
        ),
        migrations.RemoveField(
            model_name='form_isian',
            name='properti_namabangunan',
        ),
        migrations.RemoveField(
            model_name='form_isian',
            name='properti_namadebitur',
        ),
        migrations.RemoveField(
            model_name='form_isian',
            name='properti_notelp',
        ),
        migrations.RemoveField(
            model_name='form_isian',
            name='properti_pencapaianlokasiaksesjalan',
        ),
        migrations.RemoveField(
            model_name='form_isian',
            name='properti_penghunipersilsaatini',
        ),
        migrations.RemoveField(
            model_name='form_isian',
            name='properti_peruntukaneksisting',
        ),
        migrations.RemoveField(
            model_name='form_isian',
            name='properti_provinsi',
        ),
        migrations.RemoveField(
            model_name='form_isian',
            name='properti_tipeproperti',
        ),
        migrations.RemoveField(
            model_name='form_isian',
            name='properti_titikkoordinat',
        ),
        migrations.RemoveField(
            model_name='form_isian',
            name='status',
        ),
        migrations.RemoveField(
            model_name='pemberi_tugas',
            name='alamat',
        ),
        migrations.RemoveField(
            model_name='pemberi_tugas',
            name='desa',
        ),
        migrations.RemoveField(
            model_name='pemberi_tugas',
            name='kabupaten',
        ),
        migrations.RemoveField(
            model_name='pemberi_tugas',
            name='kecamatan',
        ),
        migrations.RemoveField(
            model_name='pemberi_tugas',
            name='propinsi',
        ),
        migrations.AddField(
            model_name='pemberi_tugas',
            name='pemberitugas_alamat',
            field=models.CharField(max_length=100, null=True, verbose_name='Alamat pemberi tugas'),
        ),
        migrations.AddField(
            model_name='pemberi_tugas',
            name='pemberitugas_desa',
            field=models.CharField(max_length=100, null=True, verbose_name='Desa pemberi tugas'),
        ),
        migrations.AddField(
            model_name='pemberi_tugas',
            name='pemberitugas_kabupaten',
            field=models.CharField(max_length=100, null=True, verbose_name='Kabupaten pemberi tugas'),
        ),
        migrations.AddField(
            model_name='pemberi_tugas',
            name='pemberitugas_kecamatan',
            field=models.CharField(max_length=100, null=True, verbose_name='Kecamatan pemberi tugas'),
        ),
        migrations.AddField(
            model_name='pemberi_tugas',
            name='pemberitugas_nama',
            field=models.CharField(max_length=100, null=True, verbose_name='Nama pemberi tugas'),
        ),
        migrations.AddField(
            model_name='pemberi_tugas',
            name='pemberitugas_provinsi',
            field=models.CharField(max_length=100, null=True, verbose_name='Provinsi pemberi tugas'),
        ),
    ]
