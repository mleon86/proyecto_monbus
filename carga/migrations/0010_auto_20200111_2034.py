# Generated by Django 3.0.1 on 2020-01-11 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carga', '0009_auto_20200111_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itinerario',
            name='linea_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carga.Linea'),
        ),
    ]
