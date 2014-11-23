# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sist_SAGE', '0026_auto_20141122_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='pago',
            name='fin',
            field=models.CharField(default=b'NA', max_length=10, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pago',
            name='inicio',
            field=models.CharField(default=b'NA', max_length=10, blank=True),
            preserve_default=True,
        ),
    ]
