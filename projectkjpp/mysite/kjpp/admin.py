from django.contrib import admin

# import dari .models

from .models import Pemberi_tugas 
from .models import akun
from .models import form_isian 
from .models import PropertyData

# Register your models here.

admin.site.register(Pemberi_tugas) 
admin.site.register(akun)
admin.site.register(form_isian) 
admin.site.register(PropertyData)

