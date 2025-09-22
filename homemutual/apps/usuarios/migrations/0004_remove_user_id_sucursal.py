# apps/usuarios/migrations/00xz_remove_user_id_sucursal.py
from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ("usuarios", "0003_user_id_sucursal"),  # o la última que tengas
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="id_sucursal",  # usa exactamente el nombre del campo en tu modelo
        ),
    ]
