'''
Created on Nov 12, 2014

@author: luis
'''
from django import forms
from Sist_SAGE.models import Estacionamiento, reserva
from django.forms import ModelForm

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