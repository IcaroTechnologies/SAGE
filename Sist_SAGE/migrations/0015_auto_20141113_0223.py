# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('Sist_SAGE', '0014_reserva'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='factible',
        ),
        migrations.AlterField(
            model_name='reserva',
            name='horaFin',
            field=models.CharField(max_length=6, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(60)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reserva',
            name='horaInicio',
            field=models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(regex=b'^(0?[1-9]|1[0-9]|2[0-3])$', message=b'La hora debe estar entre 0 y 23')]),
            preserve_default=True,
        ),
    ]
