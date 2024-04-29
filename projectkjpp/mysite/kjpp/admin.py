from django.contrib import admin

# import dari .models

from .models import Pemberi_tugas 
from .models import akun

# Register your models here.

admin.site.register(Pemberi_tugas) 
admin.site.register(akun)

