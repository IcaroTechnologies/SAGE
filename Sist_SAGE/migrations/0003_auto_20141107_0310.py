# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sist_SAGE', '0002_auto_20141107_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacionamiento',
            name='nombreDueno',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
    ]
