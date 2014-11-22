# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('Sist_SAGE', '0015_auto_20141113_0223'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='minFin',
            field=models.CharField(default=b'NA', max_length=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(60)]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reserva',
            name='minInicio',
            field=models.CharField(default=b'NA', max_length=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(60)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reserva',
            name='horaFin',
            field=models.CharField(default=b'NA', max_length=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(23)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reserva',
            name='horaInicio',
            field=models.CharField(default=b'NA', max_length=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(23)]),
            preserve_default=True,
        ),
    ]
