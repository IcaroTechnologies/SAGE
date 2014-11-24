#!/usr/bin/env python
# -*- coding: utf_8 -*-
'''
Created on Nov 6, 2014

@author: luis
'''
from Sist_SAGE.models import  Estacionamiento, reserva, pago
from Sist_SAGE.forms import EstacionamientoForm, ReservaForm, PagoForm
from django.shortcuts import render
from datetime import timedelta
import random

def home(request):
    return render (request,'index.html')

def menu (request):
    return render (request, 'menu.html')

def agregar(request):
    return render (request,'agregar.html')


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


def cliente (request):
    return render (request,'cliente.html')

def solicitar(request):
    return render (request, 'solicitar.html')

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
            if verificar_minimo_reserva(inicioReserva, finReserva):
                if hayPuesto:
                    form.save()
                    return render(request,'exitoreserva.html',{'res' : form})
                else:
                    return render(request,'solicitar.html',{'sinres' : form})
            else: 
                return render(request,'solicitar.html',{'minhor' : form})
                
    else:
        form = ReservaForm()
    args['form']=form
    return render(request,'solicitar.html',args) 
    

def verificarReserva(puestos, inicioReserva, finReserva):
    for puesto in puestos:
        if len(puesto)==0:
            return True
        elif len(puesto)==1:
            reserva=puesto[0]
            inicio=reserva[0]
            fin=reserva[1]
            if (inicioReserva > fin) | (finReserva < inicio):
                return True
        else:
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
    

def verificar_minimo_reserva(inicio,fin):
    
    hora=timedelta(hours=0,minutes=59,seconds=59)
    if fin > inicio or fin==inicio:
        return fin-inicio > hora
    else:
        return True
    
def pagar (request):
    return render (request, 'pagar.html')
    
def confirmarPago(request):
    args = {}
    if request.method == 'POST':
       
        form = PagoForm(request.POST)      
        if form.is_valid():
            model = form.save(commit=False)
            model.codigoConfirmacion = generarCodigoConfirmacion()
            sol = reserva.objects.last()
            inicio=timedelta(hours=int(sol.get_horaInicio()), minutes=int(sol.get_minInicio()))
            fin=timedelta(hours=int(sol.get_horaFin()), minutes=int(sol.get_minFin()))
            model.monto = calcularMonto(inicio,fin)
            model.reserva = sol
            model.save()
            return render (request, 'confirmacion.html',{'pago': model})
    else:
        form = EstacionamientoForm()
    args['form'] = form
    return render(request,'pagar.html',args)

def generarCodigoConfirmacion():
    codigo = ''
    i=0
    numeroDigitos=10
    while i < numeroDigitos:
        digito=random.randint(0,9)
        codigo = codigo + str(digito)
        i+=1
    return "SAGE"+codigo

def calcularMonto(inicio,fin):
    precio_por_hora = 8.772
    segundos_de_una_hora = 3600
    bloques = (fin-inicio).total_seconds() // segundos_de_una_hora
    bloque_incompleto = int((fin-inicio).total_seconds()) - (bloques*segundos_de_una_hora)
    if bloque_incompleto > 0:
        bloques+=1
    return bloques * precio_por_hora
    
def reservas_registradas(request):
    entradas = pago.objects.all()
    return render(request,'reservas_registradas.html', {'pagos' : entradas})

def datos_pago (request,id):
    datosPago=pago.objects.get(pk=id)
    return render (request,'datosPago.html', {'pago' : datosPago})