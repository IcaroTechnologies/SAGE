#!/usr/bin/env python
# -*- coding: utf_8 -*-

'''
Created on Oct 27, 2014

@author: luis
'''

class Estacionamiento(object):
    
    max_correo=2
    max_telefono=3
 
    def __init__(self,nombreDueno, nombreEst, direccionEst,
                 telefono, correo, rif ):
        
        self.nombreDueno=nombreDueno
        self.nombreEst=nombreEst
        self.direccionEst=direccionEst
        self.telefono=telefono
        self.correo=correo
        self.rif=rif
        self.horaApertura="NA"
        self.horaClausura="NA"
        self.horaAperturaReserva="NA"
        self.horaClausuraReserva="NA"
        self.tarifa="NA"
 
    def __str__(self):
        return ("Dueno: "+self.nombreDueno+
                "\nEstacionamiento: "+self.nombreEst+
                "\nDireccion: "+self.direccionEst+
                "\nRIF: "+ self.rif+
                "\nTelefonos: "+self.imprimirInfo(self.telefono)+
                "\nCorreos: "+self.imprimirInfo(self.correo)+"\n"+
                "}nTarifa: "+self.tarifa+
                "}nHora de Apertura: "+self.horaApertura+
                "}nHora de Clausura: "+self.horaClausura+
                "}nHora de inicio de reservas: "+self.horaAperturaReserva+
                "}nHora de cierre de reservas: "+self.horaClausuraReserva)
    
    #Funcion que imprime los correos y telefonos    
    def imprimirInfo(self,infoEstacionamiento):
        i=0
        informacion=""
        while i<len(infoEstacionamiento):
            informacion=informacion+infoEstacionamiento[i]
            i+=1
            if i < len(infoEstacionamiento):
                informacion=informacion+" / "
        return informacion
        

    
    