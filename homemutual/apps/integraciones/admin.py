from django.contrib import admin

from .models.sg_catalogo_models import *

# Registramos los modelos independientes
admin.site.register(SgEntidadTipoDocumento)
admin.site.register(SgTipoPersona)
admin.site.register(SgTipoCuenta)
