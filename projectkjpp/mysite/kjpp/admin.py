from django.contrib import admin

# import dari .models

from .models import akun
from .models import form_isian
from .models import objekProperti

# Register your models here.

admin.site.register(akun)
admin.site.register(form_isian)
admin.site.register(objekProperti)

