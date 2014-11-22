# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('Sist_SAGE', '0020_auto_20141113_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacionamiento',
            name='horaAperturaReserva',
            field=models.CharField(blank=True, max_length=50, validators=[django.core.validators.RegexValidator(regex=b'^(0?[0-9]|1[0-9]|2[0-3])$', message=b'Formato de hora incorrecto, debe estar entre 0 y 23')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estacionamiento',
            name='horaCierreReserva',
            field=models.CharField(blank=True, max_length=50, validators=[django.core.validators.RegexValidator(regex=b'^(0?[0-9]|1[0-9]|2[0-3])$', message=b'Formato de hora incorrecto, debe estar entre 0 y 23')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estacionamiento',
            name='minAperturaReserva',
            field=models.CharField(blank=True, max_length=50, validators=[django.core.validators.RegexValidator(regex=b'^[0-5][0-9]$', message=b'Formato de hora incorrecto, debe estar entre 0 y 59')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estacionamiento',
            name='minCierreReserva',
            field=models.CharField(blank=True, max_length=50, validators=[django.core.validators.RegexValidator(regex=b'^[0-5][0-9]$', message=b'Formato de hora incorrecto, debe estar entre 0 y 59')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reserva',
            name='horaFin',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex=b'^(0?[0-9]|1[0-9]|2[0-3])$', message=b'Formato de hora incorrecto, debe estar entre 0 y 23')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reserva',
            name='horaInicio',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex=b'^(0?[0-9]|1[0-9]|2[0-3])$', message=b'Formato de hora incorrecto, debe estar entre 0 y 23')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reserva',
            name='minFin',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex=b'^[0-5][0-9]$', message=b'Formato de hora incorrecto, debe estar entre 0 y 59')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reserva',
            name='minInicio',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex=b'^[0-5][0-9]$', message=b'Formato de hora incorrecto, debe estar entre 0 y 59')]),
            preserve_default=True,
        ),
    ]
