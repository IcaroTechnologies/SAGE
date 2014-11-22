# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sist_SAGE', '0013_auto_20141112_1631'),
    ]

    operations = [
        migrations.CreateModel(
            name='reserva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('horaInicio', models.TimeField()),
                ('horaFin', models.TimeField()),
                ('factible', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
