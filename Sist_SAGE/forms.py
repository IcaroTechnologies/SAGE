'''
Created on Nov 12, 2014

@author: luis
'''
from django import forms
from Sist_SAGE.models import Estacionamiento, reserva, pago
from django.forms import ModelForm
import random

class EstacionamientoForm(ModelForm):
    class Meta: 
        model = Estacionamiento
        fields = '__all__'
        error_messages = {
            'nombreEst': {
                'required':("Este campo es obligatorio"),
            },
            'nombreDueno': {
                'required':("Este campo es obligatorio"),
            },
            'direccionEst': {
                'required':("Este campo es obligatorio"),
            },
            'correo_1': {
                'required':("Este campo es obligatorio"),
            },
            'telefono_1': {
                'required':("Este campo es obligatorio"),
            },
            'rif': {
                'required':("Este campo es obligatorio"),
            },
            'puestos': {
                'required':("Este campo es obligatorio"),
            },
            'tarifa': {
                'required':("Este campo es obligatorio"),
            },
            'horaApertura': {
                'required':("Este campo es obligatorio"),
            },
            'minApertura': {
                'required':("Este campo es obligatorio"),
            },
            'horaCierre': {
                'required':("Este campo es obligatorio"),
            },
            'minCierre': {
                'required':("Este campo es obligatorio"),
            },
        }
        
        
class ReservaForm(ModelForm):
    class Meta:
        model = reserva
        fields ='__all__'
        error_messages = {
            'horaInicio': {
                'required':("Este campo es obligatorio"),
            },
            'minInicio': {
                'required':("Este campo es obligatorio"),
            },
            'horaFin': {
                'required':("Este campo es obligatorio"),
            },
            'minFin': {
                'required':("Este campo es obligatorio"),
            },
        }
        
        
class PagoForm(ModelForm):
    class Meta:
        model = pago
        fields ='__all__'
        error_messages = {
            'nombre': {
                'required':("Este campo es obligatorio"),
            },
            'cedula': {
                'required':("Este campo es obligatorio"),
            },
            'tipoTarjeta': {
                'required':("Este campo es obligatorio"),
            },
            'digitos': {
                'required':("Este campo es obligatorio"),
            },
            'anoVencimiento': {
                'required':("Este campo es obligatorio"),
            },
            'mesVencimiento': {
                'required':("Este campo es obligatorio"),
            },
            'codigoSeguridad': {
                'required':("Este campo es obligatorio"),
            },
        }
 

    def obtener_ultimos_4_digitos(self):
        var = self.cleaned_data['digitos']
        return "************"+var[12:]
        