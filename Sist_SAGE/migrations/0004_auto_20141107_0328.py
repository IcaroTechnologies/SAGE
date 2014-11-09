# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sist_SAGE', '0003_auto_20141107_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacionamiento',
            name='nombreEst',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
