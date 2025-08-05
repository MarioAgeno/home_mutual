from django.contrib import admin

from .models.socio_models import Socio
from .models.sucursal_models import Sucursal

# Registramos los modelos independientes
admin.site.register(Socio)
admin.site.register(Sucursal)
