# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estacionamiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombreEst', models.CharField(max_length=50)),
                ('nombreDueno', models.CharField(max_length=50)),
                ('direccionEst', models.CharField(max_length=50)),
                ('correo_1', models.CharField(max_length=50)),
                ('correo_2', models.CharField(max_length=50)),
                ('telefono_1', models.CharField(max_length=50)),
                ('telefono_2', models.CharField(max_length=50)),
                ('telefono_3', models.CharField(max_length=50)),
                ('rif', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
