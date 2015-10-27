# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buses', '0002_auto_20151023_1430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clasificacion',
            name='empresa',
        ),
        migrations.AddField(
            model_name='recorrido',
            name='dia',
            field=models.DateTimeField(null=True),
        ),
    ]
