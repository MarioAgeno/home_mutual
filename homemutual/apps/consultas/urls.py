from django.urls import path
from .views import ver_saldo

urlpatterns = [
    path('saldo/<int:cuenta>/', ver_saldo, name='ver_saldo'),
]
