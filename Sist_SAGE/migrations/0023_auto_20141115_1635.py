# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('Sist_SAGE', '0022_auto_20141115_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='minFin',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex=b'^[0-5]?[0-9]$', message=b'Formato de hora incorrecto, debe estar entre 0 y 59')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reserva',
            name='minInicio',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex=b'^[0-5]?[0-9]$', message=b'Formato de hora incorrecto, debe estar entre 0 y 59')]),
            preserve_default=True,
        ),
    ]
