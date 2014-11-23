# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sist_SAGE', '0039_auto_20141123_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pago',
            name='reserva',
            field=models.OneToOneField(primary_key=True, serialize=False, to='Sist_SAGE.reserva'),
            preserve_default=True,
        ),
    ]
