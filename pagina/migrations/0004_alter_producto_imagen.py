# Generated by Django 5.0.6 on 2024-06-22 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0003_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media/productos', verbose_name='Imagen'),
        ),
    ]