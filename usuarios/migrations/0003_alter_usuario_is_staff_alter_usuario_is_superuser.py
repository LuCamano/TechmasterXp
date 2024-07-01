# Generated by Django 5.0.6 on 2024-07-01 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_alter_usuario_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='is_staff',
            field=models.BooleanField(choices=[(True, 'Empleado'), (False, 'Cliente')], default=False, verbose_name='Tipo de usuario'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='is_superuser',
            field=models.BooleanField(choices=[(True, 'Superusuario'), (False, 'No es superusuario')], default=False, help_text='(Debe ser empleado para que tenga efecto)', verbose_name='Superusuario'),
        ),
    ]
