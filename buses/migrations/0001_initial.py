# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clasificacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estrellas', models.PositiveSmallIntegerField()),
                ('comentario', models.TextField()),
            ],
            options={
                'db_table': 'clasificacion',
            },
        ),
        migrations.CreateModel(
            name='EmpresaBuses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=40)),
                ('url', models.URLField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'empresa_buses',
            },
        ),
        migrations.CreateModel(
            name='Parada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('gps_lat', models.FloatField()),
                ('gps_lon', models.FloatField()),
            ],
            options={
                'db_table': 'parada',
            },
        ),
        migrations.CreateModel(
            name='ParadaRecorrido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('parada', models.ForeignKey(to='buses.Parada')),
            ],
            options={
                'db_table': 'parada_recorrido',
            },
        ),
        migrations.CreateModel(
            name='Recorrido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=40)),
                ('precio', models.PositiveIntegerField()),
                ('hora_llegada', models.TimeField()),
                ('hora_salida', models.TimeField()),
                ('destino', models.ForeignKey(related_name='destino', to='buses.Parada', null=True)),
                ('empresa_bus', models.ForeignKey(to='buses.EmpresaBuses')),
                ('origen', models.ForeignKey(related_name='origen', to='buses.Parada', null=True)),
            ],
            options={
                'db_table': 'recorridos',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'usuario',
            },
        ),
        migrations.AddField(
            model_name='paradarecorrido',
            name='recorrido',
            field=models.ForeignKey(to='buses.Recorrido'),
        ),
        migrations.AddField(
            model_name='clasificacion',
            name='empresa',
            field=models.ForeignKey(to='buses.EmpresaBuses'),
        ),
        migrations.AddField(
            model_name='clasificacion',
            name='recorrido',
            field=models.ForeignKey(to='buses.Recorrido'),
        ),
        migrations.AddField(
            model_name='clasificacion',
            name='usuario',
            field=models.ForeignKey(to='buses.Usuario'),
        ),
    ]
