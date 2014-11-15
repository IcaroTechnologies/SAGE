#!/usr/bin/env python
# -*- coding: utf_8 -*-


from django.core import validators
from django.core.validators import EmailValidator, RegexValidator,\
    MinValueValidator
from django.db import models


class Estacionamiento (models.Model):
    nombreEst = models.CharField(max_length=50)
    nombreDueno = models.CharField(max_length=50)
    direccionEst = models.CharField(max_length=50)
    correo_1 = models.CharField(max_length=50, validators=[EmailValidator()])
    correo_2 = models.CharField(max_length=50, blank=True, validators=[EmailValidator()])
    telefono_1 = models.CharField(max_length=50,validators=[RegexValidator(regex='^0?(212|412|414|424|416|426)-?[0-9]{7}$',message="Formato Invalido, ej: 02121234567")])
    telefono_2 = models.CharField(max_length=50, blank=True,validators=[RegexValidator(regex='^0?(212|412|414|424|416|426)-?[0-9]{7}$',message="Formato Invalido, ej: 02121234567")])
    telefono_3 = models.CharField(max_length=50, blank=True,validators=[RegexValidator(regex='^0?(212|412|414|424|416|426)-?[0-9]{7}$',message="Formato Invalido, ej: 02121234567")])
    rif = models.CharField(max_length=50)
    puestos = models.CharField(max_length=50, validators=[MinValueValidator(0)])
    horaApertura = models.CharField(max_length=3, default="NA")
    minApertura=models.CharField(max_length=3, default="NA")
    horaCierre = models.CharField(max_length=3,default="NA")
    minCierre = models.CharField(max_length=3,default="NA")
    tarifa = models.CharField(max_length=10, validators=[MinValueValidator(0)])
    horaAperturaReserva = models.CharField(max_length=50,blank=True, validators=[RegexValidator(regex='^(0?[0-9]|1[0-9]|2[0-3])$', message="Formato de hora incorrecto, debe estar entre 0 y 23")])
    minAperturaReserva = models.CharField(max_length=50,blank=True,validators=[RegexValidator(regex='^[0-5]?[0-9]$', message="Formato de hora incorrecto, debe estar entre 0 y 59")])
    horaCierreReserva = models.CharField(max_length=50,blank=True, validators=[RegexValidator(regex='^(0?[0-9]|1[0-9]|2[0-3])$', message="Formato de hora incorrecto, debe estar entre 0 y 23")])
    minCierreReserva = models.CharField(max_length=50,blank=True,validators=[RegexValidator(regex='^[0-5]?[0-9]$', message="Formato de hora incorrecto, debe estar entre 0 y 59")])
    
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
    horaInicio = models.CharField(max_length=10, validators=[RegexValidator(regex='^(0?[0-9]|1[0-9]|2[0-3])$', message="Formato de hora incorrecto, debe estar entre 0 y 23")])
    minInicio = models.CharField(max_length=10, validators=[RegexValidator(regex='^[0-5]?[0-9]$', message="Formato de hora incorrecto, debe estar entre 0 y 59")])
    horaFin = models.CharField(max_length=10, validators=[RegexValidator(regex='^(0?[0-9]|1[0-9]|2[0-3])$', message="Formato de hora incorrecto, debe estar entre 0 y 23")])
    minFin = models.CharField(max_length=10, validators=[RegexValidator(regex='^[0-5]?[0-9]$', message="Formato de hora incorrecto, debe estar entre 0 y 59")])


    def __unicode__(self):
        return "Hora de entrada -> "+ self.horaInicio+ ":"+ self.minInicio+"\nHora de salida ->"+self.horaFin+":"+self.minFin
    
    
    
    
    
    
    