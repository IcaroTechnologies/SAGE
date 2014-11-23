# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sist_SAGE', '0033_auto_20141123_1814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pago',
            name='id',
        ),
        migrations.AlterField(
            model_name='pago',
            name='reserva',
            field=models.OneToOneField(primary_key=True, serialize=False, to='Sist_SAGE.reserva'),
            preserve_default=True,
        ),
    ]
