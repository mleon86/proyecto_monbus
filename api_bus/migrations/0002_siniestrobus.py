# Generated by Django 3.0.7 on 2020-09-05 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_bus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiniestroBus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time_solic', models.DateTimeField()),
                ('estado_solicitud', models.CharField(choices=[('I', 'INACTIVO'), ('A', 'ACTIVO')], default='I', max_length=10)),
                ('viaje_inicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_bus.Viaje_Incio')),
            ],
            options={
                'verbose_name': 'SiniestroBus',
                'verbose_name_plural': 'Siniestros Bus',
                'ordering': ['time_solic'],
            },
        ),
    ]