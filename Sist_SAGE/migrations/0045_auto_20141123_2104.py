# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('Sist_SAGE', '0044_auto_20141123_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pago',
            name='codigoSeguridad',
            field=models.IntegerField(max_length=4, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=True,
        ),
    ]
