# homemutual\apps\maestros\forms\cuenta_mutual_forms.py
from django import forms
from .crud_forms_generics import CrudGenericForm
from ..models.cuenta_mutual_models import CuentaMutual
from diseno_base.diseno_bootstrap import (
	formclasstext, formclassselect)
from apps.usuarios.models import User
from django.db.models import Q

class CuentaMutualForm(CrudGenericForm):
		
	class Meta:
		model = CuentaMutual
		fields ='__all__'
		
		widgets = {
			'estatus_cuenta_mutual': 
				forms.Select(attrs={**formclassselect}),
			'id_user':
				forms.Select(attrs={**formclasstext}),
			'id_sucursal': 
				forms.Select(attrs={**formclassselect}),
			'id_socio': 
				forms.TextInput(attrs={**formclassselect}),
			'cuenta': 
				forms.TextInput(attrs={**formclassselect}),
			'documento': 
				forms.TextInput(attrs={**formclasstext}),
			'id_sg_account': 
				forms.TextInput(attrs={**formclasstext}),
			'cvu': 
				forms.TextInput(attrs={**formclasstext}),
			'alias': 
				forms.TextInput(attrs={**formclasstext}),
		}
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

        # Mostrar sólo usuarios NO staff y sin cuenta asignada.
        # En edición, permitir además el propio usuario ya vinculado.
		base = User.objects.filter(is_staff=False)
		if self.instance and self.instance.pk:
			self.fields['id_user'].queryset = base.filter(
                Q(cuenta__isnull=True) | Q(pk=self.instance.id_user_id)
            )
		else:
			self.fields['id_user'].queryset = base.filter(cuenta__isnull=True)
            