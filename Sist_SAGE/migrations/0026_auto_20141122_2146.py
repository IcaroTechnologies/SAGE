# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('Sist_SAGE', '0025_auto_20141122_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pago',
            name='codigoSeguridad',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(b'^[0-9]{3,4}$', b'El codigo de seguridad debe tener 3 o 4 d\xc3\xadgitos')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pago',
            name='mesVencimiento',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(b'^(0?[1-9]|1[0-2])$', b'El mes de expiraci\xc3\xb3n debe estar entre 0 y 12')]),
            preserve_default=True,
        ),
    ]
