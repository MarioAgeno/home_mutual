from django.db import transaction
from apps.maestros.models.cuenta_mutual_models import CuentaMutual
from .sg_client import sg_post_usuarios, sg_get_cvu, SGConnectorError

def build_sg_usuario_payload(c: CuentaMutual) -> dict:
    u = c.id_user
    return {
        "nombre":  (u.first_name or "").strip(),
        "apellido": (u.last_name or "").strip(),
        "sexo": (c.sexo or "X"),
        "idEntidadTipoDocumento": str(c.id_entidad_tipo_documento_id) if c.id_entidad_tipo_documento_id else None,
        "numeroDocumento": c.documento or "",
        "fechaNacimiento": c.fecha_nacimiento.isoformat() if c.fecha_nacimiento else None,
        "cuit": int(c.cuit) if (c.cuit and str(c.cuit).isdigit()) else None,
        "email": (u.email or f"user{u.pk}@example.com"),
        "caracteristicaPaisTelefono": c.caracteristica_pais_telefono or "54",
        "codigoAreaTelefono": c.codigo_area_telefono or "",
        "numeroTelefono": c.numero_telefono or "",
        "idTipoPersona": str(c.id_tipo_persona_id) if c.id_tipo_persona_id else None,
        "numeroCuentaEntidad": c.nro_cuenta_entidad or (str(c.cuenta) if c.cuenta else str(c.pk)),
        "idTipoCuenta": str(c.id_tipo_cuenta_id) if c.id_tipo_cuenta_id else None,
    }

@transaction.atomic
def crear_o_sincronizar_en_sg(cuenta: CuentaMutual) -> CuentaMutual:
    # 1) Alta si falta
    if not cuenta.id_sg_usuario:
        data = sg_post_usuarios(build_sg_usuario_payload(cuenta))
        cuenta.id_sg_usuario = data.get("idUsuario")
        cuenta.cvu           = data.get("cvu")
        cuenta.alias         = data.get("alias")
        cuenta.save(update_fields=["id_sg_usuario", "cvu", "alias", "updated_at"])

    # 2) (Opcional) Traer id_sg_cuenta
    if not cuenta.id_sg_cuenta and cuenta.id_sg_usuario:
        try:
            items = sg_get_cvu(cuenta.id_sg_usuario)  # lista de CVU del usuario
            target = None
            nce = (cuenta.nro_cuenta_entidad or str(cuenta.cuenta) or str(cuenta.pk))
            for it in items:
                if str(it.get("numeroCuentaEntidad")) == nce:
                    target = it; break
            if not target and items:
                target = items[0]
            if target and target.get("id"):
                cuenta.id_sg_cuenta = target.get("id")
                if target.get("cvu") and not cuenta.cvu:
                    cuenta.cvu = target.get("cvu")
                if target.get("alias") and not cuenta.alias:
                    cuenta.alias = target.get("alias")
                cuenta.save(update_fields=["id_sg_cuenta", "cvu", "alias", "updated_at"])
        except SGConnectorError:
            pass

    cuenta.refresh_from_db()
    return cuenta
