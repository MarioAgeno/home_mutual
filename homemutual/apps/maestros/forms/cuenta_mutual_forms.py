import re
from django import forms
from django.db.models import Q
from .crud_forms_generics import CrudGenericForm
from ..models.cuenta_mutual_models import CuentaMutual
from diseno_base.diseno_bootstrap import (formclasstext, formclassselect, formclassdate)
from ..models.sg_catalogo_models import (SgEntidadTipoDocumento, SgTipoPersona, SgTipoCuenta)
from apps.usuarios.models import User


class CuentaMutualForm(CrudGenericForm):
    id_entidad_tipo_documento = forms.ModelChoiceField(
        queryset=SgEntidadTipoDocumento.objects.all().order_by('nombre'),
        required=False, empty_label="-- Seleccionar --",
        widget=forms.Select(attrs={**formclassselect})
    )
    id_tipo_persona = forms.ModelChoiceField(
        queryset=SgTipoPersona.objects.all().order_by('tipo_persona'),
        required=False, empty_label="-- Seleccionar --",
        widget=forms.Select(attrs={**formclassselect})
    )
    id_tipo_cuenta = forms.ModelChoiceField(
        queryset=SgTipoCuenta.objects.all().order_by('tipo_cuenta'),
        required=False, empty_label="-- Seleccionar --",
        widget=forms.Select(attrs={**formclassselect})
    )

    class Meta:
        model = CuentaMutual
        fields = '__all__'
        widgets = {
            'estatus_cuenta_mutual': forms.Select(attrs={**formclassselect}),
            'id_sucursal': forms.Select(attrs={**formclassselect}),
            'id_socio': forms.TextInput(attrs={**formclasstext}),
            'cuenta': forms.TextInput(attrs={**formclasstext}),
            'documento': forms.TextInput(attrs={**formclasstext}),
            'cvu': forms.TextInput(attrs={**formclasstext}),
            'alias': forms.TextInput(attrs={**formclasstext}),
            'id_user': forms.Select(attrs={**formclassselect}),
            'razon_social': forms.TextInput(attrs={**formclasstext}),
            'cuit': forms.TextInput(attrs={**formclasstext}),
            'sexo': forms.Select(attrs={**formclassselect}),
            'fecha_nacimiento': forms.TextInput(attrs={'type':'date', **formclassdate}),
            'caracteristica_pais_telefono': forms.TextInput(attrs={**formclasstext}),
            'codigo_area_telefono': forms.TextInput(attrs={**formclasstext}),
            'numero_telefono': forms.TextInput(attrs={**formclasstext}),
            'id_sg_usuario': forms.TextInput(attrs={**formclasstext}),
            'id_sg_cuenta': forms.TextInput(attrs={**formclasstext}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Usuarios NO staff sin cuenta; en edición, permitir el propio usuario ya vinculado
        base = User.objects.filter(is_staff=False)
        if self.instance and self.instance.pk and self.instance.id_user_id:
            self.fields['id_user'].queryset = base.filter(
                Q(cuenta__isnull=True) | Q(pk=self.instance.id_user_id)
            )
        else:
            self.fields['id_user'].queryset = base.filter(cuenta__isnull=True)

        self.fields["id_entidad_tipo_documento"].label_from_instance = lambda o: o.nombre
        self.fields["id_tipo_persona"].label_from_instance           = lambda o: o.tipo_persona
        self.fields["id_tipo_cuenta"].label_from_instance            = lambda o: o.tipo_cuenta

    def clean_documento(self):
        doc = self.cleaned_data.get("documento", "")
        d = re.sub(r"\D+", "", str(doc or ""))
        if d:
            d = d.zfill(8)  # lo mismo que exige SG
        return d