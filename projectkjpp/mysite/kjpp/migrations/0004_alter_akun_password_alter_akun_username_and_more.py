# Generated by Django 5.0.6 on 2024-06-02 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kjpp', '0003_form_isian'),
    ]

    operations = [
        migrations.AlterField(
            model_name='akun',
            name='password',
            field=models.CharField(max_length=100, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='akun',
            name='username',
            field=models.CharField(max_length=100, verbose_name='username'),
        ),
        migrations.AlterField(
            model_name='form_isian',
            name='properti_luastanah',
            field=models.IntegerField(verbose_name='Luas tanah'),
        ),
    ]