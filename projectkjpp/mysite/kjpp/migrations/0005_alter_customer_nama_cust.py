# Generated by Django 5.0.6 on 2024-06-18 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kjpp', '0004_rename_testfield_customer_nama_cust'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='nama_cust',
            field=models.CharField(max_length=20, verbose_name='Nama customer'),
        ),
    ]
