# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sist_SAGE', '0016_auto_20141113_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='horaFin',
            field=models.CharField(default=b'NA', max_length=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reserva',
            name='horaInicio',
            field=models.CharField(default=b'NA', max_length=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reserva',
            name='minFin',
            field=models.CharField(default=b'NA', max_length=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reserva',
            name='minInicio',
            field=models.CharField(default=b'NA', max_length=3),
            preserve_default=True,
        ),
    ]
