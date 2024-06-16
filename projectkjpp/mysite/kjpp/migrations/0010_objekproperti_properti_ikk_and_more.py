# Generated by Django 5.0.6 on 2024-06-11 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kjpp', '0009_objekproperti_delete_data_properti'),
    ]

    operations = [
        migrations.AddField(
            model_name='objekproperti',
            name='properti_ikk',
            field=models.CharField(blank=True, default='0', max_length=200, null=True, verbose_name='IKK'),
        ),
        migrations.AddField(
            model_name='objekproperti',
            name='properti_ilm',
            field=models.CharField(blank=True, default='0', max_length=200, null=True, verbose_name='ILM'),
        ),
        migrations.AddField(
            model_name='objekproperti',
            name='properti_jumlahlantai',
            field=models.CharField(default='0', max_length=200, verbose_name='Jumlah lantai'),
        ),
        migrations.AddField(
            model_name='objekproperti',
            name='properti_tahunbangun',
            field=models.CharField(default='0', max_length=200, verbose_name='Tahun bangun'),
        ),
        migrations.AddField(
            model_name='objekproperti',
            name='properti_tahunpenilaian',
            field=models.CharField(default='0', max_length=200, verbose_name='Tahun penilaian'),
        ),
        migrations.AddField(
            model_name='objekproperti',
            name='properti_tahunrenovasi',
            field=models.CharField(default='0', max_length=200, verbose_name='Tahun renovasi'),
        ),
        migrations.AddField(
            model_name='objekproperti',
            name='properti_umurekonomis',
            field=models.CharField(default='0', max_length=200, verbose_name='Umur ekonomis'),
        ),
    ]
