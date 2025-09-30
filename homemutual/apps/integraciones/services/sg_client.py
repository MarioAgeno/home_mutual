import requests
from django.conf import settings

class SGConnectorError(Exception):
    pass

def _headers():
    h = {"Content-Type": "application/json"}
    api_key = getattr(settings, "SG_CONNECTOR_API_KEY", "")
    if api_key:
        # si tu FastAPI espera X-API-KEY cambialo acá
        h["X-API-KEY"] = api_key
    return h

def sg_post_usuarios(payload: dict) -> dict:
    """POST /sg/usuarios -> { idUsuario, cvu, alias, ... }"""
    base = settings.SG_CONNECTOR_BASE_URL.rstrip("/")
    url = f"{base}/sg/usuarios"
    try:
        r = requests.post(url, json=payload, headers=_headers(),
                          timeout=getattr(settings, "SG_CONNECTOR_TIMEOUT", 20))
    except requests.RequestException as e:
        raise SGConnectorError(f"Error de red hacia conector SG: {e}")
    if r.status_code >= 400:
        # devolvemos el detalle que mande el conector
        try:
            detail = r.json()
        except Exception:
            detail = r.text
        raise SGConnectorError(f"SG {r.status_code}: {detail}")
    try:
        return r.json()
    except Exception:
        raise SGConnectorError("Respuesta del conector SG inválida (no es JSON).")

def sg_get_cvu(id_web_usuario_final: str) -> list[dict]:
    """
    GET /sg/cvu (o el endpoint que uses) con header IDWEBUSUARIOFINAL
    Devuelve lista de CVUs [{id, cvu, alias, numeroCuentaEntidad, ...}]
    """
    base = settings.SG_CONNECTOR_BASE_URL.rstrip("/")
    url = f"{base}/sg/cvu"
    headers = _headers()
    headers["IDWEBUSUARIOFINAL"] = id_web_usuario_final
    try:
        r = requests.get(url, headers=headers,
                         timeout=getattr(settings, "SG_CONNECTOR_TIMEOUT", 20))
    except requests.RequestException as e:
        raise SGConnectorError(f"Error de red hacia conector SG: {e}")
    if r.status_code >= 400:
        try:
            detail = r.json()
        except Exception:
            detail = r.text
        raise SGConnectorError(f"SG {r.status_code}: {detail}")
    try:
        data = r.json()
        # aseguramos lista
        return data if isinstance(data, list) else []
    except Exception:
        raise SGConnectorError("Respuesta de /cvu inválida (no es JSON).")
