# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('Sist_SAGE', '0028_auto_20141123_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pago',
            name='codigoConfirmacion',
            field=models.CharField(max_length=18, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pago',
            name='tipoTarjeta',
            field=models.CharField(max_length=10, choices=[(b'Visa', b'Visa'), (b'MasterCard', b'MasterCard'), (b'Express', b'Express')], validators=[django.core.validators.RegexValidator(b'^(Visa|MasterCard|Express)$', b'Tipo de tarjeta incorrecto')]),
            preserve_default=True,
        ),
    ]
