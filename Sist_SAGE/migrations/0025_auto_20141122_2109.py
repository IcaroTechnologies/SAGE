# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('Sist_SAGE', '0024_auto_20141122_1830'),
    ]

    operations = [
        migrations.CreateModel(
            name='pago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(b'^[a-zA-Z\\\xc3\xb1]+$', b'Solo se permiten letras en este campo.')])),
                ('cedula', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(b'^[0-9]{,8}$', b'Formato incorrecto de la c\xc3\xa9dula, solo escriba los digitos de la cedula sin espacios ni otros caracteres.')])),
                ('tipoTarjeta', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(b'^(Visa|MasterCard|Express)$', b'Tipo de tarjeta incorrecto')])),
                ('digitos', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(b'^[0-9]{16}$', b'Formato incorrecto, deben ser 16 d\xc3\xadgitos sin espacios')])),
                ('anoVencimiento', models.CharField(max_length=50, validators=[django.core.validators.MinValueValidator(2014), django.core.validators.RegexValidator(b'^[0-9]{4}$', b'El a\xc3\xb1o de expiraci\xc3\xb3n de la tarjeta debe ser mayor a la fecha actual')])),
                ('mesVencimiento', models.CharField(max_length=2, validators=[django.core.validators.RegexValidator(b'^(0?[1-9]|1[0-2])$', b'El mes de expiraci\xc3\xb3n debe estar entre 0 y 12')])),
                ('codigoSeguridad', models.CharField(max_length=4, validators=[django.core.validators.RegexValidator(b'^[0-9]{3,4}$', b'El codigo de seguridad debe tener 3 o 4 d\xc3\xadgitos')])),
                ('codigoConfirmacion', models.CharField(max_length=18, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='estacionamiento',
            name='horaApertura',
            field=models.CharField(max_length=2, validators=[django.core.validators.RegexValidator(regex=b'^(0?[0-9]|1[0-9]|2[0-3])$', message=b'Formato de hora incorrecto, debe estar entre 0 y 23')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estacionamiento',
            name='horaAperturaReserva',
            field=models.CharField(blank=True, max_length=2, validators=[django.core.validators.RegexValidator(regex=b'^(0?[0-9]|1[0-9]|2[0-3])$', message=b'Formato de hora incorrecto, debe estar entre 0 y 23')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estacionamiento',
            name='horaCierre',
            field=models.CharField(max_length=2, validators=[django.core.validators.RegexValidator(regex=b'^(0?[0-9]|1[0-9]|2[0-3])$', message=b'Formato de hora incorrecto, debe estar entre 0 y 23')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estacionamiento',
            name='horaCierreReserva',
            field=models.CharField(blank=True, max_length=2, validators=[django.core.validators.RegexValidator(regex=b'^(0?[0-9]|1[0-9]|2[0-3])$', message=b'Formato de hora incorrecto, debe estar entre 0 y 23')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estacionamiento',
            name='minApertura',
            field=models.CharField(max_length=2, validators=[django.core.validators.RegexValidator(regex=b'^[0-5]?[0-9]$', message=b'Formato de hora incorrecto, los minutos deben estar entre 0 y 59')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estacionamiento',
            name='minAperturaReserva',
            field=models.CharField(blank=True, max_length=2, validators=[django.core.validators.RegexValidator(regex=b'^[0-5]?[0-9]$', message=b'Formato de hora incorrecto, los minutos deben estar entre 0 y 59')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estacionamiento',
            name='minCierre',
            field=models.CharField(max_length=2, validators=[django.core.validators.RegexValidator(regex=b'^[0-5]?[0-9]$', message=b'Formato de hora incorrecto, los minutos deben estar entre 0 y 59')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estacionamiento',
            name='minCierreReserva',
            field=models.CharField(blank=True, max_length=2, validators=[django.core.validators.RegexValidator(regex=b'^[0-5]?[0-9]$', message=b'Formato de hora incorrecto, los minutos deben estar entre 0 y 59')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estacionamiento',
            name='puestos',
            field=models.CharField(max_length=10, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estacionamiento',
            name='rif',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reserva',
            name='horaFin',
            field=models.CharField(max_length=2, validators=[django.core.validators.RegexValidator(regex=b'^(0?[0-9]|1[0-9]|2[0-3])$', message=b'Formato de hora incorrecto, debe estar entre 0 y 23')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reserva',
            name='horaInicio',
            field=models.CharField(max_length=2, validators=[django.core.validators.RegexValidator(regex=b'^(0?[0-9]|1[0-9]|2[0-3])$', message=b'Formato de hora incorrecto, debe estar entre 0 y 23')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reserva',
            name='minFin',
            field=models.CharField(max_length=2, validators=[django.core.validators.RegexValidator(regex=b'^[0-5]?[0-9]$', message=b'Formato de hora incorrecto, los minutos deben estar entre 0 y 59')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reserva',
            name='minInicio',
            field=models.CharField(max_length=2, validators=[django.core.validators.RegexValidator(regex=b'^[0-5]?[0-9]$', message=b'Formato de hora incorrecto, los minutos deben estar entre 0 y 59')]),
            preserve_default=True,
        ),
    ]
