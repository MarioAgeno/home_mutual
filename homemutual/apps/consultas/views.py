import requests
from django.shortcuts import render, get_object_or_404
from apps.maestros.models.socio_models import Socio

def ver_saldo(request, cuenta):
    # Buscar socio por cuenta_socio, no por id_socio
    socio = get_object_or_404(Socio, cuenta_socio=cuenta)
    
    # Obtener URL base de API desde la sucursal
    ws_url_base = socio.id_sucursal.ws_url.rstrip('/')  # Quita barra final si la hay
    url_api = f"{ws_url_base}/saldos/{cuenta}"

    try:
        response = requests.get(url_api, timeout=5)
        response.raise_for_status()
        datos_saldo = response.json()
    except requests.exceptions.RequestException as e:
        datos_saldo = {"error": str(e)}
    
    return render(request, 'consultas/ver_saldo.html', {'datos': datos_saldo, 'cuenta': cuenta})
