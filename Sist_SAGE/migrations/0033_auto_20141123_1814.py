# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sist_SAGE', '0032_auto_20141123_1808'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pago',
            old_name='prueba',
            new_name='reserva',
        ),
    ]
