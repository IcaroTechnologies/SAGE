#!/usr/bin/env python
# -*- coding: utf_8 -*-

from django.core.validators import EmailValidator, RegexValidator,\
    MinValueValidator, MaxValueValidator
from django.db import models
from django.core import validators


class Estacionamiento (models.Model):
    
    solo_letras= RegexValidator(r'^[a-zA-Z\ñ]+$', 'Solo se permiten letras en este campo.')
    formato_telefono = RegexValidator(regex='^0?(212|412|414|424|416|426)-?[0-9]{7}$',message="Formato Invalido, ej: 02121234567")
    formato_hora = RegexValidator(regex='^(0?[0-9]|1[0-9]|2[0-3])$', message="Formato de hora incorrecto, debe estar entre 0 y 23")
    formato_minuto =RegexValidator(regex='^[0-5]?[0-9]$', message="Formato de hora incorrecto, los minutos deben estar entre 0 y 59")
    
    nombreEst = models.CharField(max_length=50, validators=[solo_letras])
    nombreDueno = models.CharField(max_length=50)
    direccionEst = models.CharField(max_length=50)
    correo_1 = models.CharField(max_length=50,validators=[EmailValidator()])
    correo_2 = models.CharField(max_length=50,blank=True, validators=[EmailValidator()])
    telefono_1 = models.CharField(max_length=50,validators=[formato_telefono])
    telefono_2 = models.CharField(max_length=50,blank=True,validators=[formato_telefono])
    telefono_3 = models.CharField(max_length=50,blank=True,validators=[formato_telefono])
    rif = models.CharField(max_length=10)
    puestos = models.CharField(max_length=10, validators=[MinValueValidator(0)])
    horaApertura = models.CharField(max_length=2,validators=[formato_hora])
    minApertura=models.CharField(max_length=2,validators=[formato_minuto])
    horaCierre = models.CharField(max_length=2,validators=[formato_hora])
    minCierre = models.CharField(max_length=2,validators=[formato_minuto])
    tarifa = models.CharField(max_length=10, validators=[MinValueValidator(0)])
    horaAperturaReserva = models.CharField(max_length=2,blank=True, validators=[formato_hora])
    minAperturaReserva = models.CharField(max_length=2,blank=True,validators=[formato_minuto])
    horaCierreReserva = models.CharField(max_length=2,blank=True, validators=[formato_hora])
    minCierreReserva = models.CharField(max_length=2,blank=True,validators=[formato_minuto])
    
    def __unicode__(self):              # __unicode__ on Python 2
        return (u"Dueño: "+self.nombreDueno+
                "\nEstacionamiento: "+self.nombreEst+
                "\nDirección: "+self.direccionEst+
                "\nRIF: "+ self.rif+
                "\nTeléfono principal: "+self.telefono_1+
                "\nTeléfono opcional #1: "+self.telefono_2+
                "\nTeléfono opcional #2: "+self.telefono_3+
                "\nCorreo principal: "+self.correo_1+
                "\nCorreo secundario: "+self.correo_2+
                "\nRIF: "+self.rif)
        
        
    

class reserva (models.Model):
    
    formato_hora = RegexValidator(regex='^(0?[0-9]|1[0-9]|2[0-3])$', message="Formato de hora incorrecto, debe estar entre 0 y 23")
    formato_minuto =RegexValidator(regex='^[0-5]?[0-9]$', message="Formato de hora incorrecto, los minutos deben estar entre 0 y 59")
    
    horaInicio = models.CharField(max_length=2,validators=[formato_hora])
    minInicio = models.CharField(max_length=2,validators=[formato_minuto])
    horaFin = models.CharField(max_length=2,validators=[formato_hora])
    minFin = models.CharField(max_length=2,validators=[formato_minuto])
    
    def get_inicio(self):
        return self.horaInicio + ":"+ self.minInicio
    
    def get_fin(self):
        return self.horaFin + ":"+ self.minFin

    def __unicode__(self):
        return "Hora de entrada -> "+ self.horaInicio+ ":"+ self.minInicio+"\nHora de salida ->"+self.horaFin+":"+self.minFin
    
    
class pago (models.Model):
    
    solo_letras= RegexValidator(r'^[a-zA-Z\ñ]+$', 'Solo se permiten letras en este campo.')
    formato_cedula = RegexValidator(r'^[0-9]{,8}$', 'Formato incorrecto de la cédula, solo escriba los digitos de la cedula sin espacios ni otros caracteres.')
    formato_tarjeta = RegexValidator(r'^[0-9]{16}$', 'Formato incorrecto, deben ser 16 dígitos sin espacios')
    formato_ano = RegexValidator(r'^[0-9]{4}$', 'El año de expiración de la tarjeta debe ser mayor a la fecha actual')
    formato_mes = RegexValidator(r'^(0?[1-9]|1[0-2])$', 'El mes de expiración debe estar entre 0 y 12')
    formato_codigo = RegexValidator(r'^[0-9]{3,4}$', 'El codigo de seguridad debe tener 3 o 4 dígitos')
    formato_tipo_tarjeta = RegexValidator(r'^(Visa|MasterCard|Express)$','Tipo de tarjeta incorrecto')
    
    
    nombre = models.CharField(max_length=50,validators=[solo_letras])
    cedula = models.CharField(max_length=10,validators=[formato_cedula])
    tipoTarjeta = models.CharField(max_length=10, validators=[formato_tipo_tarjeta])
    digitos = models.CharField(max_length=16,validators=[formato_tarjeta])
    anoVencimiento = models.CharField(max_length=50,validators=[MinValueValidator(2014), formato_ano])
    mesVencimiento = models.CharField(max_length=10,validators=[formato_mes])
    codigoSeguridad = models.CharField(max_length=10,validators=[formato_codigo])
    codigoConfirmacion = models.CharField(max_length=18,blank=True)
    inicio = models.CharField(max_length=10,blank=True, default="NA")
    fin = models.CharField(max_length=10,blank=True, default="NA")
    
 
    

    
    
    
    
    
    
    
      
      

    
    
    