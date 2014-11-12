#!/usr/bin/env python
# -*- coding: utf_8 -*-

from django import forms
from django.core import validators
from django.core.validators import EmailValidator, RegexValidator
from django.core.exceptions import ValidationError
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
    
    
    def __unicode__(self):              # __unicode__ on Python 2
        return (u"Dueño: "+self.nombreDueno+
                "\nEstacionamiento: "+self.nombreEst+
                "\nDireccion: "+self.direccionEst+
                "\nRIF: "+ self.rif+
                "\nTelefono principal: "+self.telefono_1+
                "\nTelefono opcional #1: "+self.telefono_2+
                "\nTelefono opcional #2: "+self.telefono_3+
                "\nCorreo principal: "+self.correo_1+
                "\nCorreo secundario: "+self.correo_2+
                "\nRIF: "+self.rif)
    
