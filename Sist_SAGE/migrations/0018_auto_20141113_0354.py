# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('Sist_SAGE', '0017_auto_20141113_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='horaFin',
            field=models.CharField(max_length=3, validators=[django.core.validators.RegexValidator(regex=b'^(0?[1-9]|1[0-9]|2[0-3])$', message=b'Formato de hora incorrecto')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reserva',
            name='horaInicio',
            field=models.CharField(max_length=3, validators=[django.core.validators.RegexValidator(regex=b'^(0?[1-9]|1[0-9]|2[0-3])$', message=b'Formato de hora incorrecto')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reserva',
            name='minFin',
            field=models.CharField(max_length=3, validators=[django.core.validators.RegexValidator(regex=b'^[0-5][0-9]$', message=b'Formato de hora incorrecto')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reserva',
            name='minInicio',
            field=models.CharField(max_length=3, validators=[django.core.validators.RegexValidator(regex=b'^[0-5][0-9]$', message=b'Formato de hora incorrecto')]),
            preserve_default=True,
        ),
    ]
