# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('Sist_SAGE', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacionamiento',
            name='nombreEst',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(1)]),
            preserve_default=True,
        ),
    ]
