# Generated by Django 5.0.6 on 2024-06-22 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_alter_usuario_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='usuarios', verbose_name='Imagen'),
        ),
    ]
