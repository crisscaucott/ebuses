# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_squashed_0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='persona',
            table='persona',
        ),
    ]
