# apps/usuarios/migrations/00xx_remove_user_sucursal.py
from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ("usuarios", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="id_sucursal",
        ),
    ]
