# homemutual\apps\maestros\models\socio_models.py
from django.db import models
from django.core.exceptions import ValidationError
import re
from apps.usuarios.models import User  

from .base_gen_models import ModeloBaseGenerico
from .sucursal_models import Sucursal
from entorno.constantes_base import (
	ESTATUS_GEN, TIPO_CUENTA)


class Socio(ModeloBaseGenerico):
	id_socio = models.AutoField(primary_key=True)
	estatus_socio = models.BooleanField("Estatus*", default=True, 
										  choices=ESTATUS_GEN)
	cuenta_socio = models.IntegerField("Cuenta*", null=True, blank=True)
	tipo_cuenta = models.CharField("Tipo de Cuenta", default="C", 
								    max_length=1, choices=TIPO_CUENTA)
	nombre_socio = models.CharField("Nombre Socio*", max_length=50)
	telefono_socio = models.CharField("Teléfono*", max_length=15)
	email_socio = models.EmailField("Email*", max_length=50)
	id_sucursal = models.ForeignKey(Sucursal, 
									on_delete=models.CASCADE,
									null=True, blank=True,
									verbose_name="Sucursal*")
	id_user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='socio'  # nos permite usar request.user.socio
    )
	
	class Meta:
		db_table = 'socio'
		verbose_name = ('Socio')
		verbose_name_plural = ('Socios')
		ordering = ['nombre_socio']
												
	def __str__(self):
		return self.nombre_socio
	
	def clean(self):
		super().clean()
		
		#-- Diccionario contenedor de errores.
		errors = {}
		
		#-- Convertir a string los valores de los campos previo a la validación.
		telefono_str = str(self.telefono_socio) if self.telefono_socio else ''
		
		if not re.match(r'^\+?\d[\d ]{0,14}$', telefono_str):
			errors.update({'telefono_socio': 'Debe indicar sólo dígitos numéricos positivos, \
       			mínimo 1 y máximo 15, el signo + y espacios.'})
		
		if errors:
			#-- Lanza el conjunto de excepciones.
			raise ValidationError(errors)
	





