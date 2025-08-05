# homemutual\apps\maestros\forms\socio_forms.py
from django import forms
from .crud_forms_generics import CrudGenericForm
from ..models.socio_models import Socio
from diseno_base.diseno_bootstrap import (
	formclasstext, formclassselect)


class SocioForm(CrudGenericForm):
		
	class Meta:
		model = Socio
		fields ='__all__'
		
		widgets = {
			'estatus_socio': 
				forms.Select(attrs={**formclassselect}),
			'cuenta_socio':
				forms.TextInput(attrs={**formclasstext}),
			'tipo_cuenta': 
				forms.Select(attrs={**formclassselect}),
			'nombre_socio': 
				forms.TextInput(attrs={**formclasstext}),
			'telefono_socio': 
				forms.TextInput(attrs={**formclasstext}),
			'email_socio': 
				forms.TextInput(attrs={**formclasstext}),
			'id_sucursal': 
				forms.Select(attrs={**formclassselect}),
		}
	
	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user', None)  # Extraer el usuario autenticado
		super().__init__(*args, **kwargs)
		
		###################################################################################
		#-- Si es un nuevo registro.
		if not self.instance.pk:
			self.fields['id_sucursal'].initial = self.initial.get('id_sucursal')
			#-- Deshabilita el campo.
			self.fields['id_sucursal'].widget.attrs['disabled'] = True
		else:
				#-- Configuración en modo edición.
			self.fields['id_sucursal'].widget = forms.HiddenInput()
			self.fields['id_sucursal'].required = False
			self.initial['id_sucursal'] = self.instance.id_sucursal
	
	def clean(self):
		cleaned_data = super().clean()
		#-- Asignar automáticamente id_sucursal si el formulario está en modo edición.
		if self.instance.pk:
			cleaned_data['id_sucursal'] = self.instance.id_sucursal
			#-- Remover id_sucursal de la validación en modo edición.
			self._errors.pop('id_sucursal', None)
		return cleaned_data
