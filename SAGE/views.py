#!/usr/bin/env python
# -*- coding: utf_8 -*-


'''
Created on Nov 6, 2014

@author: luis
'''
from re import match, search
from Sist_SAGE.models import Estacionamiento
from django.core.exceptions import ValidationError

from django.http import HttpResponse
import datetime
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render

def home(request):
    return render (request,'index.html')

def agregar(request):
    return render (request,'Agregar.html')

def menu (request):
    return render (request, 'menu.html')

def crearEst(request):
    nDueno=request.POST['nombreDueno']
    nEst=request.POST['nombreEst']
    dirEst=request.POST['direccionEst']
    corr1=request.POST['correo_1']
    corr2=request.POST['correo_2']
    tel1=request.POST['telefono_1']
    tel2=request.POST['telefono_2']
    tel3=request.POST['telefono_3']
    rif1=request.POST['rif']
    p= Estacionamiento(nombreEst=nEst, nombreDueno=nDueno, direccionEst=dirEst,
                       correo_1=corr1, correo_2=corr2, telefono_1=tel1,
                        telefono_2=tel2, telefono_3=tel3, rif=rif1)
    try:
        p.clean_fields()
    except ValidationError:
        return render (request, 'error.html')
    p.save()
    return render (request, 'exito.html',{'est': p})
