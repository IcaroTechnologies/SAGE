# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('Sist_SAGE', '0042_auto_20141123_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pago',
            name='anoVencimiento',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(b'^(201[4-9]|20[2-9][0-9])$', b'El a\xc3\xb1o de expiraci\xc3\xb3n de la tarjeta debe ser mayor a la fecha actual')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pago',
            name='codigoSeguridad',
            field=models.CharField(max_length=4, validators=[django.core.validators.RegexValidator(b'^[0-9]{3,4}$', b'El codigo de seguridad debe tener 3 o 4 d\xc3\xadgitos')]),
            preserve_default=True,
        ),
    ]
