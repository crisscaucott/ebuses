# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url_img', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'banner',
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_termino', models.DateTimeField()),
                ('empresa', models.ForeignKey(to='buses.EmpresaBuses')),
            ],
            options={
                'db_table': 'pago',
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
                ('duracion', models.SmallIntegerField()),
                ('limite_imgs', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'plan',
            },
        ),
        migrations.AddField(
            model_name='pago',
            name='plan',
            field=models.ForeignKey(to='pagos.Plan'),
        ),
        migrations.AddField(
            model_name='banner',
            name='pago',
            field=models.ForeignKey(to='pagos.Pago'),
        ),
    ]
