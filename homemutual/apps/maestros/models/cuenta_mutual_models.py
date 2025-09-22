# homemutual\apps\maestros\models\cuenta_mutual_models.py
from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import Q
from apps.usuarios.models import User  
from .base_gen_models import ModeloBaseGenerico
from .sucursal_models import Sucursal
from entorno.constantes_base import (ESTATUS_GEN)


class CuentaMutual(ModeloBaseGenerico):
	id_cuenta_mutual = models.AutoField(primary_key=True)
	estatus_cuenta_mutual = models.BooleanField("Estatus*", default=True, 
										  choices=ESTATUS_GEN)
	id_user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='cuenta')  # nos permite usar request.user.socio
	id_sucursal = models.ForeignKey(
		Sucursal, 
		on_delete=models.CASCADE,
		null=True, blank=True,
		verbose_name="Sucursal*")
	id_socio = models.IntegerField("ID Socio*", null=True, blank=True)
	cuenta = models.IntegerField("Cuenta*", null=True, blank=True)
	documento = models.CharField(max_length=20, blank=True, null=True)
    # Identificadores SG
	id_sg_account = models.CharField(max_length=64, unique=True, blank=True, null=True)
	cvu = models.CharField(max_length=22, unique=True, blank=True, null=True)
	alias = models.CharField(max_length=60, blank=True, null=True)

	def clean(self):
		super().clean()
		errors = {}
		if self.id_user and self.id_user.is_staff:
			raise ValidationError({"id_user": "No se puede asignar una cuenta a un usuario staff."})
		if errors:
			raise ValidationError(errors)

	class Meta:
		db_table = 'cuenta_mutual'
		verbose_name = 'Cuenta Mutual'
		verbose_name_plural = 'Cuentas Mutuales'
		ordering = ['id_cuenta_mutual']
        # OneToOne ya garantiza unicidad de id_user; si querés condicionar unicidades:
		constraints = [
            models.UniqueConstraint(
                fields=['id_sg_account'],
                name='uniq_id_sg_account_not_null',
                condition=Q(id_sg_account__isnull=False),
            ),
            models.UniqueConstraint(
                fields=['cvu'],
                name='uniq_cvu_not_null',
                condition=Q(cvu__isnull=False),
            ),
        ]

	def __str__(self):
		return f"{self.cuenta} / {self.id_user.username}"

	@property
	def usuario_nombre(self):
		u = self.id_user
		full = f"{u.first_name} {u.last_name}".strip()	
		return full or u.username