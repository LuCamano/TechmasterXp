# Generated by Django 5.0.6 on 2024-07-01 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_alter_usuario_is_staff_alter_usuario_is_superuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='direccion1',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='direccion2',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='telefono',
        ),
    ]