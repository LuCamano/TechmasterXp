# Generated by Django 5.0.6 on 2024-06-25 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0004_hdd_rpm'),
    ]

    operations = [
        migrations.AddField(
            model_name='cooler',
            name='stock',
            field=models.PositiveIntegerField(default=30, verbose_name='Stock'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fuentealimentacion',
            name='stock',
            field=models.PositiveIntegerField(default=30, verbose_name='Stock'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gabinete',
            name='stock',
            field=models.PositiveIntegerField(default=30, verbose_name='Stock'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hdd',
            name='stock',
            field=models.PositiveIntegerField(default=30, verbose_name='Stock'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='memoriaram',
            name='stock',
            field=models.PositiveIntegerField(default=30, verbose_name='Stock'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='placabase',
            name='stock',
            field=models.PositiveIntegerField(default=30, verbose_name='Stock'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='procesador',
            name='stock',
            field=models.PositiveIntegerField(default=30, verbose_name='Stock'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ssd',
            name='stock',
            field=models.PositiveIntegerField(default=30, verbose_name='Stock'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tarjeta_grafica',
            name='stock',
            field=models.PositiveIntegerField(default=30, verbose_name='Stock'),
            preserve_default=False,
        ),
    ]
