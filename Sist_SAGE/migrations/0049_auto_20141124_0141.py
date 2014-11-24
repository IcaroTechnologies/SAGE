# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sist_SAGE', '0048_auto_20141124_0131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pago',
            name='fin',
        ),
        migrations.RemoveField(
            model_name='pago',
            name='inicio',
        ),
    ]
