#!/usr/bin/env python
# -*- coding: utf_8 -*-


'''
Created on Nov 6, 2014

@author: luis
'''
from Sist_SAGE.models import  Estacionamiento
from django.core.exceptions import ValidationError
from Sist_SAGE.forms import EstacionamientoForm
from django.http import HttpResponse
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
    
    args = {}
    if request.method == 'POST':
        form = EstacionamientoForm(request.POST)
        if form.is_valid():
            print form.is_valid()
            form.save()
            return render (request, 'exito.html',{'est': form})
    else:
        form = EstacionamientoForm()
    args['form'] = form

    return render(request,'Agregar.html',args)


