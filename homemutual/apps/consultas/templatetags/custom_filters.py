from django import template

register = template.Library()

@register.filter
def formato_miles(valor):
    try:
        valor = float(valor)
        return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except:
        return valor
