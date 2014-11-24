# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('Sist_SAGE', '0047_auto_20141123_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='pago',
            name='reserva',
            field=models.OneToOneField(default=b'1', to='Sist_SAGE.reserva'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pago',
            name='nombre',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(b'^[a-zA-Z\\\xc3\xb1]+ [a-zA-Z\\\xc3\xb1 ]+$', b'Escriba su nombre y apellido, Solo se permiten letras en este campo.')]),
            preserve_default=True,
        ),
    ]
