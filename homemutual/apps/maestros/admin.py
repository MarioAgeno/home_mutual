from django.contrib import admin

from .models.cuenta_mutual_models import CuentaMutual
from .models.sucursal_models import Sucursal

# Registramos los modelos independientes
admin.site.register(CuentaMutual)
admin.site.register(Sucursal)
