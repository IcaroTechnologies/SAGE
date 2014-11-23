# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sist_SAGE', '0037_auto_20141123_1903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pago',
            name='reserva',
        ),
        migrations.AddField(
            model_name='pago',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
