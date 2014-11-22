#!/usr/bin/env python
# -*- coding: utf_8 -*-

from django.db import models
from django.core import validators
from django.core.validators import EmailValidator, RegexValidator

# Create your models here.
class Estacionamiento(models.Model):
    
    nombreEst = models.CharField(max_length=50)
    nombreDueno = models.CharField(max_length=50)
    direccionEst = models.CharField(max_length=50)
    correo_1 = models.CharField(max_length=50, validators=[EmailValidator()])
    correo_2 = models.CharField(max_length=50, blank=True)
    telefono_1 = models.CharField(max_length=50,validators=[RegexValidator(regex='^0?[24]12-?[0-9]{7}$',message="Formato Invalido")])
    telefono_2 = models.CharField(max_length=50,blank=True)
    telefono_3 = models.CharField(max_length=50,blank=True)
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
    
