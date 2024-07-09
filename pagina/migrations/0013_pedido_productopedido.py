# Generated by Django 5.0.6 on 2024-07-05 09:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('pagina', '0012_remove_carrito_total'),
        ('usuarios', '0008_alter_tarjeta_fecha_vencimiento'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de pedido')),
                ('total', models.PositiveIntegerField(verbose_name='Total')),
                ('estado', models.CharField(choices=[('En preparación', 'En preparación'), ('Enviado', 'Enviado'), ('Entregado', 'Entregado'), ('Cancelado', 'Cancelado')], default='En preparación', max_length=50, verbose_name='Estado')),
                ('direccion', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.direccion', verbose_name='Dirección')),
                ('tarjeta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.tarjeta', verbose_name='Tarjeta')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
        migrations.CreateModel(
            name='ProductoPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1, verbose_name='Cantidad')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contenttypes.contenttype')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pagina.pedido', verbose_name='Pedido')),
            ],
            options={
                'verbose_name': 'Producto en pedido',
                'verbose_name_plural': 'Productos en pedido',
            },
        ),
    ]