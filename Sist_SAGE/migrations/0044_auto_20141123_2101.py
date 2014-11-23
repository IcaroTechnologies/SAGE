# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('Sist_SAGE', '0043_auto_20141123_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pago',
            name='codigoSeguridad',
            field=models.CharField(max_length=4, validators=[django.core.validators.RegexValidator(b'^[0-9][0-9]$', b'El codigo de seguridad debe tener 3 o 4 d\xc3\xadgitos')]),
            preserve_default=True,
        ),
    ]
