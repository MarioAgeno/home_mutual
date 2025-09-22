# homemutual\homemutual\urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home_view
from django.views.defaults import permission_denied
handler403 = permission_denied  # usará templates/403.html

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('usuarios/', include('apps.usuarios.urls')),
    path('maestros/', include('apps.maestros.urls')),
    path('consultas/', include('apps.consultas.urls')),
]

#-- Manejo de archivos estáticos en modo DEBUG.
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
