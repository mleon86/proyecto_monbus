# Generated by Django 3.0.1 on 2020-01-11 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_bus', '0003_auto_20200107_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus_datos',
            name='estado_viaje',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
    ]
