# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sist_SAGE', '0049_auto_20141124_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacionamiento',
            name='puestos',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estacionamiento',
            name='tarifa',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pago',
            name='monto',
            field=models.DecimalField(default=0, max_digits=6, decimal_places=2, blank=True),
            preserve_default=True,
        ),
    ]
