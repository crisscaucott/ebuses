# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buses', '0003_auto_20151027_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresabuses',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]
