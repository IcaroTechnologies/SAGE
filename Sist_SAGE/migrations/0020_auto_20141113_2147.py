# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('Sist_SAGE', '0019_auto_20141113_0421'),
    ]

    operations = [
        migrations.AddField(
            model_name='estacionamiento',
            name='horaApertura',
            field=models.CharField(default=b'NA', max_length=3),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estacionamiento',
            name='horaAperturaReserva',
            field=models.CharField(default=0, max_length=50, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estacionamiento',
            name='horaCierre',
            field=models.CharField(default=b'NA', max_length=3),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estacionamiento',
            name='horaCierreReserva',
            field=models.CharField(default=0, max_length=50, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estacionamiento',
            name='minApertura',
            field=models.CharField(default=b'NA', max_length=3),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estacionamiento',
            name='minAperturaReserva',
            field=models.CharField(default=0, max_length=50, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estacionamiento',
            name='minCierre',
            field=models.CharField(default=b'NA', max_length=3),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estacionamiento',
            name='minCierreReserva',
            field=models.CharField(default=0, max_length=50, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estacionamiento',
            name='puestos',
            field=models.CharField(default=0, max_length=50, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estacionamiento',
            name='tarifa',
            field=models.CharField(default=0, max_length=10, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
    ]
