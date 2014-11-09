# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('Sist_SAGE', '0006_auto_20141107_0550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacionamiento',
            name='telefono_1',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(regex=b'^0?4[12][46]-?[0-9]{7}$', message=b'Formato Inv\xc3\xa1lido'), django.core.validators.RegexValidator(regex=b'^0?[24]12-?[0-9]{7}$', message=b'Formato Invalido')]),
            preserve_default=True,
        ),
    ]
