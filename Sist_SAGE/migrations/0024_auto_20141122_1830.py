# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('Sist_SAGE', '0023_auto_20141115_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacionamiento',
            name='nombreEst',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(b'^[a-zA-Z\\\xc3\xb1]+$', b'Solo se permiten letras en este campo.')]),
            preserve_default=True,
        ),
    ]
