# \apps\maestros\urls.py
from django.urls import path

#-- Tablas
from .views.socio_views import *
from .views.sucursal_views import *

urlpatterns = [
	#-- Tablas:
	#-- Socio.
	path('socio/', SocioListView.as_view(), name='socio_list'),
	path('socio/nueva/', SocioCreateView.as_view(), name='socio_create'),
	path('socio/<int:pk>/editar/', SocioUpdateView.as_view(), name='socio_update'),
	path('socio/<int:pk>/eliminar/', SocioDeleteView.as_view(), name='socio_delete'),
	
	#-- Sucursal.
	path('sucursal/', SucursalListView.as_view(), name='sucursal_list'),
	path('sucursal/nueva/', SucursalCreateView.as_view(), name='sucursal_create'),
	path('sucursal/<int:pk>/editar/', SucursalUpdateView.as_view(), name='sucursal_update'),
	path('sucursal/<int:pk>/eliminar/', SucursalDeleteView.as_view(), name='sucursal_delete'),
	

]