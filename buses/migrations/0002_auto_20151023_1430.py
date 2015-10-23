# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='apellido',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='rut',
            field=models.CharField(default='', max_length=12),
            preserve_default=False,
        ),
    ]
