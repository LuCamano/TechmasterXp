# Generated by Django 5.0.6 on 2024-06-26 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='is_staff',
            field=models.BooleanField(choices=[(True, 'Empleado'), (False, 'Cliente')], default=False, verbose_name='Empleado'),
        ),
    ]
