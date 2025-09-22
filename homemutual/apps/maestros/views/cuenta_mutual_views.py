# homemutual\apps\maestros\views\cuenta_mutual_views.py
from django.urls import reverse_lazy
from .cruds_views_generics import *
from ..models.cuenta_mutual_models import CuentaMutual
from ..forms.cuenta_mutual_forms import CuentaMutualForm
from apps.core.mixins import StaffRequiredMixin

class ConfigViews():
	# Modelo
	model = CuentaMutual
	
	# Formulario asociado al modelo
	form_class = CuentaMutualForm
	
	# Aplicación asociada al modelo
	app_label = model._meta.app_label
	
	#-- Deshabilitado por redundancia:
	# # Título del listado del modelo
	# master_title = model._meta.verbose_name_plural
	
	#-- Usar esta forma cuando el modelo esté compuesto de una sola palabra: Ej. Color.
	# model_string = model.__name__.lower()  #-- Usar esta forma cuando el modelo esté compuesto de una sola palabra: Ej. Color.
	
	#-- Usar esta forma cuando el modelo esté compuesto por más de una palabra: Ej. TipoCambio colocar "tipo_cambio".
	model_string = "cuenta_mutual"
	
	# Permisos
	permission_add = f"{app_label}.add_{model.__name__.lower()}"
	permission_change = f"{app_label}.change_{model.__name__.lower()}"
	permission_delete = f"{app_label}.delete_{model.__name__.lower()}"
	
	# Vistas del CRUD del modelo
	list_view_name = f"{model_string}_list"
	create_view_name = f"{model_string}_create"
	update_view_name = f"{model_string}_update"
	delete_view_name = f"{model_string}_delete"
	
	# Plantilla para crear o actualizar el modelo
	template_form = f"{app_label}/{model_string}_form.html"
	
	# Plantilla para confirmar eliminación de un registro
	template_delete = "base_confirm_delete.html"
	
	# Plantilla de la lista del CRUD
	template_list = f'{app_label}/maestro_list.html'
	
	# Contexto de los datos de la lista
	context_object_name	= 'objetos'
	
	# Vista del home del proyecto
	home_view_name = "home"
	
	# Nombre de la url 
	success_url = reverse_lazy(list_view_name)


class DataViewList():
	search_fields = ['id_socio', 'id_user__username', 'id_user__last_name', 'id_user__first_name']

	ordering = ['id_socio']
	
	paginate_by = 8
	  
	table_headers = {
		'estatus_cuenta_mutual': (1, 'Estatus'),
		'id_user': (1, 'Usuario'),
		'id_socio': (1, 'ID Socio'),
		'usuario_nombre': (1, 'Apellido'),
		'id_sucursal': (1, 'Sucursal'),
		'acciones': (1, 'Acciones'),
	}
	
	table_data = [
		{'field_name': 'estatus_cuenta_mutual', 'date_format': None},
		{'field_name': 'id_user', 'date_format': None},
		{'field_name': 'id_socio', 'date_format': None},
		{'field_name': 'usuario_nombre', 'date_format': None},
		{'field_name': 'id_sucursal', 'date_format': None},
	]


# CuentaMutualListView - Inicio
class CuentaMutualListView(StaffRequiredMixin, MaestroListView):
	model = ConfigViews.model
	template_name = ConfigViews.template_list
	context_object_name = ConfigViews.context_object_name
	
	search_fields = DataViewList.search_fields
	ordering = DataViewList.ordering
	
	extra_context = {
		"master_title": ConfigViews.model._meta.verbose_name_plural,
		"home_view_name": ConfigViews.home_view_name,
		"list_view_name": ConfigViews.list_view_name,
		"create_view_name": ConfigViews.create_view_name,
		"update_view_name": ConfigViews.update_view_name,
		"delete_view_name": ConfigViews.delete_view_name,
		"table_headers": DataViewList.table_headers,
		"table_data": DataViewList.table_data,
	}


# CuentaMutualCreateView - Inicio
class CuentaMutualCreateView(StaffRequiredMixin, MaestroCreateView):
	model = ConfigViews.model
	list_view_name = ConfigViews.list_view_name
	form_class = ConfigViews.form_class
	template_name = ConfigViews.template_form
	success_url = ConfigViews.success_url
	
	#-- Indicar el permiso que requiere para ejecutar la acción.
	permission_required = ConfigViews.permission_add
	
	# extra_context = {
	# 	"accion": f"Crear {ConfigViews.model._meta.verbose_name}",
	# 	"list_view_name" : ConfigViews.list_view_name
	# }
	
	#def get_initial(self):
	#	initial = super().get_initial()
	#	#-- Asignar la sucursal del usuario autenticado como valor inicial.
	#	initial['id_sucursal'] = self.request.user.id_sucursal
	#	return initial

# CuentaMutualUpdateView
class CuentaMutualUpdateView(StaffRequiredMixin, MaestroUpdateView):
	model = ConfigViews.model
	list_view_name = ConfigViews.list_view_name
	form_class = ConfigViews.form_class
	template_name = ConfigViews.template_form
	success_url = ConfigViews.success_url
	
	#-- Indicar el permiso que requiere para ejecutar la acción.
	permission_required = ConfigViews.permission_change
	
	
	# def get_context_data(self, **kwargs):
	# 	#-- Llamar al contexto base de la clase genérica.
	# 	context = super().get_context_data(**kwargs)
	# 	
	# 	# Obtener el objeto que se está editando
	# 	registro = self.get_object()
	# 	
	# 	#-- Actualizar el contexto con el ID.
	# 	context.update({
	# 		"accion": f"Editar {ConfigViews.model._meta.verbose_name} - {registro.pk}",
	# 		"list_view_name" : ConfigViews.list_view_name
	# 	})
	# 	
	# 	return context


# CuentaMutualDeleteView
class CuentaMutualDeleteView (StaffRequiredMixin, MaestroDeleteView):
	model = ConfigViews.model
	list_view_name = ConfigViews.list_view_name
	template_name = ConfigViews.template_delete
	success_url = ConfigViews.success_url
	
	#-- Indicar el permiso que requiere para ejecutar la acción.
	permission_required = ConfigViews.permission_delete
	
	# extra_context = {
	# 	"accion": f"Eliminar {ConfigViews.model._meta.verbose_name}",
	# 	"list_view_name" : ConfigViews.list_view_name,
	# 	"mensaje": "Estás seguro de eliminar el Registro"
	# }
