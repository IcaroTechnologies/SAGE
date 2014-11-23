# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sist_SAGE', '0030_auto_20141123_0437'),
    ]

    operations = [
        migrations.AddField(
            model_name='pago',
            name='monto',
            field=models.DecimalField(default=0, max_digits=6, decimal_places=2, blank=True),
            preserve_default=True,
        ),
    ]
