# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('Sist_SAGE', '0045_auto_20141123_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pago',
            name='codigoSeguridad',
            field=models.CharField(max_length=4, validators=[django.core.validators.RegexValidator(b'^[0-9]{3,4}$', b'El codigo de seguridad debe tener 3 o 4 d\xc3\xadgitos')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pago',
            name='tipoTarjeta',
            field=models.CharField(max_length=10, choices=[(b'MR', b'Mr.'), (b'MRS', b'Mrs.'), (b'MS', b'Ms.')], validators=[django.core.validators.RegexValidator(b'^(Visa|MasterCard|Express)$', b'Tipo de tarjeta incorrecto')]),
            preserve_default=True,
        ),
    ]
