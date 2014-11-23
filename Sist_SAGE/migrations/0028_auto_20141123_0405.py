# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sist_SAGE', '0027_auto_20141122_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pago',
            name='codigoConfirmacion',
            field=models.CharField(default=b'generarCodigoConfirmacion()', max_length=18, editable=False),
            preserve_default=True,
        ),
    ]
