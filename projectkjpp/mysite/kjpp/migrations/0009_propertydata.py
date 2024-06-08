# Generated by Django 5.0.4 on 2024-06-08 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kjpp', '0008_survei_remove_form_isian_survei_bulan_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alamat_properti', models.CharField(max_length=255)),
                ('titik_koordinat', models.CharField(max_length=100)),
                ('rekaman_record', models.CharField(max_length=255)),
                ('contact_person', models.CharField(max_length=100)),
                ('jenis_data', models.CharField(choices=[('Transaksi', 'Transaksi'), ('Penawaran', 'Penawaran')], max_length=50)),
                ('jenis_properti', models.CharField(max_length=100)),
                ('luas_tanah', models.DecimalField(decimal_places=2, max_digits=10)),
                ('luas_bangunan', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unit_perbandingan', models.CharField(max_length=50)),
                ('record', models.CharField(max_length=255)),
                ('harga_penawaran', models.DecimalField(decimal_places=2, max_digits=15)),
                ('diskon', models.DecimalField(decimal_places=2, max_digits=5)),
                ('perkiraan_transaksi', models.DecimalField(decimal_places=2, max_digits=15)),
                ('perkiraan_rcn', models.DecimalField(decimal_places=2, max_digits=15)),
                ('indikasi_nilai_pasar_bangunan', models.DecimalField(decimal_places=2, max_digits=15)),
                ('indikasi_nilai_tanah', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
    ]
