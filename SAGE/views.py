#!/usr/bin/env python
# -*- coding: utf_8 -*-


'''
Created on Nov 6, 2014

@author: luis
'''
from Sist_SAGE.models import  Estacionamiento, reserva
from django.core.exceptions import ValidationError
from Sist_SAGE.forms import EstacionamientoForm, ReservaForm
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render
from datetime import timedelta

def home(request):
    return render (request,'index.html')

def agregar(request):
    return render (request,'agregar.html')

def menu (request):
    return render (request, 'menu.html')

def cliente (request):
    return render (request,'cliente.html')

def solicitar(request):
    return render (request, 'solicitar.html')

def crearEst(request):
    
    args = {}
    if request.method == 'POST':
        form = EstacionamientoForm(request.POST)
        if form.is_valid():
            form.save()
            return render (request, 'exito.html',{'est': form})
    else:
        form = EstacionamientoForm()
    args['form'] = form

    return render(request,'agregar.html',args)

def estacionamientos_registrados(request):
    entradas = Estacionamiento.objects.all()
    return render(request,'estacionamientos_registrados.html', {'estacionamientos_registrados' : entradas})

def datos_estacionamiento(request,id):
    estDatos=Estacionamiento.objects.get(pk=id)
    return render (request,'datos_estacionamiento.html', {'datos' : estDatos})

def reservar (request):
    args={}
    if request.method=='POST':
        form=ReservaForm(request.POST)
        if form.is_valid():
            horaIniReserva=request.POST.get('horaInicio',default=0)
            minIniReserva=request.POST.get('minInicio',default=0)
            horaFinReserva=request.POST.get('horaFin',default=0)
            minFinReserva=request.POST.get('minFin',default=0)
            inicioReserva =timedelta(hours=int(horaIniReserva),minutes=int(minIniReserva))
            finReserva =timedelta(hours=int(horaFinReserva),minutes=int(minFinReserva))
            puestos=estacionamiento_ficticio()
            hayPuesto=verificarReserva(puestos,inicioReserva,finReserva)
            if hayPuesto:
                form.save()
                return render(request,'exitoreserva.html',{'res' : form})
            else:
                return render(request,'solicitar.html',{'sinres' : form})
                
    else:
        form = ReservaForm()
    args['form']=form
    return render(request,'solicitar.html',args) 
    

def verificarReserva(puestos, inicioReserva, finReserva):
    for puesto in puestos:
        if len(puesto)==0:
            print "caso 0"
            return True
        elif len(puesto)==1:
            print "caso 1"
            reserva=puesto[0]
            inicio=reserva[0]
            fin=reserva[1]
            if (inicioReserva > fin) | (finReserva < inicio):
                return True
        else:
            print "caso 2"
            i=0
            while i<len(puesto):
                primera_reserva=puesto[i]
                if i<len(puesto)-1:
                    segunda_reserva=puesto[i+1]
                    fin_bloque=segunda_reserva[0]
                comienzo_bloque=primera_reserva[1]
                if i==0:
                    if finReserva < primera_reserva[0]:
                        return True
                elif i==len(puesto)-1:
                    print inicioReserva, segunda_reserva[1]
                    if inicioReserva > segunda_reserva[1]:
                        return True
                else:
                    if (inicioReserva > comienzo_bloque) & (finReserva < fin_bloque):
                        return True
                #Se revisa el primer puesto, caso borde
                i+=1
    return False
            
def estacionamiento_ficticio():    
    
    puesto1=[(timedelta(hours=12,minutes=30),timedelta(hours=14,minutes=30)),(timedelta(hours=15,minutes=30),timedelta(hours=17,minutes=30))]
    puesto2=[(timedelta(hours=9,minutes=30),timedelta(hours=12,minutes=0)),(timedelta(hours=12,minutes=30),timedelta(hours=14,minutes=30))]
    puesto3=[(timedelta(hours=7,minutes=30),timedelta(hours=9,minutes=30)),(timedelta(hours=12,minutes=30),timedelta(hours=14,minutes=30))]
    puesto4=[(timedelta(hours=10,minutes=15),timedelta(hours=11,minutes=35)),(timedelta(hours=12,minutes=30),timedelta(hours=14,minutes=30))]
    puesto5=[(timedelta(hours=11,minutes=17),timedelta(hours=11,minutes=20)),(timedelta(hours=12,minutes=30),timedelta(hours=14,minutes=30))]
    puesto6=[(timedelta(hours=7,minutes=30),timedelta(hours=8,minutes=45)),(timedelta(hours=12,minutes=30),timedelta(hours=14,minutes=30)),(timedelta(hours=15,minutes=30),timedelta(hours=18,minutes=45))]
    puesto7=[(timedelta(hours=12,minutes=30),timedelta(hours=14,minutes=30)),(timedelta(hours=14,minutes=45),timedelta(hours=16,minutes=30)),(timedelta(hours=17,minutes=30),timedelta(hours=20,minutes=30))]
    puesto8=[(timedelta(hours=12,minutes=30),timedelta(hours=14,minutes=30)),(timedelta(hours=20,minutes=30),timedelta(hours=23,minutes=30))]
    puesto9=[(timedelta(hours=0,minutes=0),timedelta(hours=23,minutes=59))]
    puestos=[puesto1,puesto2,puesto3,puesto4,puesto5,puesto6,puesto7,puesto8,puesto9]    
    return puestos
    
