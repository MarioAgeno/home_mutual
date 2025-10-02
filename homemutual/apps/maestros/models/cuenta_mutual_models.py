# apps/maestros/models/cuenta_mutual_models.py
from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import Q
from apps.usuarios.models import User
from .base_gen_models import ModeloBaseGenerico
from .sucursal_models import Sucursal
from .sg_catalogo_models import SgEntidadTipoDocumento, SgTipoPersona, SgTipoCuenta
from entorno.constantes_base import ESTATUS_GEN

SEXO_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ('X', 'No binario'),
)


class CuentaMutual(ModeloBaseGenerico):
    id_cuenta_mutual = models.AutoField(primary_key=True)
    estatus_cuenta_mutual = models.BooleanField("Estatus*", default=True, choices=ESTATUS_GEN)

    # Relación
    id_user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='cuenta')
    id_sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Sucursal*")

    # Identificadores internos Mutual
    id_socio = models.IntegerField("ID Socio*", null=True, blank=True)
    cuenta = models.IntegerField("Cuenta*", null=True, blank=True)

    # Datos de persona para SG (POST /Usuarios)
    documento = models.CharField("DNI", max_length=20, blank=True, null=True)  # numeroDocumento
    cuit = models.CharField("CUIT", max_length=11, blank=True, null=True)
    razon_social = models.CharField("Razón Social", max_length=80, blank=True, null=True)  # NULL si no aplica (PF)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=True, null=True)
    fecha_nacimiento = models.DateField("Fecha Nacimiento", blank=True, null=True)

    # Teléfono descompuesto (recomendado por SG)
    caracteristica_pais_telefono = models.CharField(max_length=2, blank=True, null=True)  # ej: "54"
    codigo_area_telefono = models.CharField(max_length=4, blank=True, null=True)
    numero_telefono = models.CharField(max_length=10, blank=True, null=True)

    id_entidad_tipo_documento = models.ForeignKey(
        SgEntidadTipoDocumento,
        to_field='id_sg_entidad_tipo_documento',
        on_delete=models.PROTECT,
        null=True, blank=True,
    )

    id_tipo_persona = models.ForeignKey(
        SgTipoPersona,
        to_field='id_sg_tipo_persona', 
        on_delete=models.PROTECT,
        null=True, blank=True,
    )

    id_tipo_cuenta = models.ForeignKey(
        SgTipoCuenta,
        to_field='id_sg_tipo_cuenta', 
        on_delete=models.PROTECT,
        null=True, blank=True,
    )

    # Identificadores SG
    id_sg_usuario = models.CharField(max_length=36, unique=True, blank=True, null=True)  
    id_sg_cuenta  = models.CharField(max_length=36, unique=True, blank=True, null=True)  
    cvu          = models.CharField(max_length=22, unique=True, blank=True, null=True)
    alias        = models.CharField(max_length=60, blank=True, null=True)


    razon_social = models.CharField("Razón Social", max_length=80, blank=True, null=True)  # null OK cuando PF


    def clean(self):
        super().clean()
        if self.id_user and self.id_user.is_staff:
            raise ValidationError({"id_user": "No se puede asignar una cuenta a un usuario staff."})

    class Meta:
        db_table = 'cuenta_mutual'
        verbose_name = 'Cuenta Mutual'
        verbose_name_plural = 'Cuentas Mutuales'
        ordering = ['id_cuenta_mutual']
        constraints = [
            models.UniqueConstraint(
                fields=['id_sg_usuario'],
                name='uniq_id_sg_usuario_not_null',
                condition=Q(id_sg_usuario__isnull=False),
            ),
            models.UniqueConstraint(
                fields=['id_sg_cuenta'],
                name='uniq_id_sg_cuenta_not_null',
                condition=Q(id_sg_cuenta__isnull=False),
            ),
            models.UniqueConstraint(
                fields=['cvu'],
                name='uniq_cvu_not_null',
                condition=Q(cvu__isnull=False),
            ),
        ]      

    def __str__(self):
        u = self.id_user
        return f"{self.cuenta} / {u.username if u else 'sin usuario'}"

    @property
    def usuario_nombre(self):
        u = self.id_user
        full = f"{u.first_name} {u.last_name}".strip() if u else ''
        return full or (u.username if u else '')
