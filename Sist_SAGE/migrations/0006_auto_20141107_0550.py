# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sist_SAGE', '0005_auto_20141107_0547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacionamiento',
            name='telefono_1',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estacionamiento',
            name='telefono_2',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estacionamiento',
            name='telefono_3',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
    ]
