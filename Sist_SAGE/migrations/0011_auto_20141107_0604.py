# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('Sist_SAGE', '0010_auto_20141107_0601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacionamiento',
            name='correo_2',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.EmailValidator()]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estacionamiento',
            name='telefono_2',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator(regex=b'^0?[24]12-?[0-9]{7}$', message=b'Formato Invalido')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estacionamiento',
            name='telefono_3',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator(regex=b'^0?[24]12-?[0-9]{7}$', message=b'Formato Invalido')]),
            preserve_default=True,
        ),
    ]
