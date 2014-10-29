#!/usr/bin/env python
# -*- coding: utf_8 -*-

'''
Created on Oct 27, 2014

@author: luis
'''
from re import search, match

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
    
    
    #Validacion del nombre del dueño    
    @property
    def nombreDueno(self):
        return self._nombreDueno

    @nombreDueno.setter
    def nombreDueno(self, dueno):
        if not dueno or (search('\d',dueno)): 
            raise Exception('el nombre del dueno debe existir y no puede contener numeros')
        self._nombreDueno = dueno
       
    #Validacion del nombre del estacionamiento 
    @property
    def nombreEst(self):
        return self._nombreEst

    @nombreEst.setter
    def nombreEst(self, estacionamiento):
        if not estacionamiento: 
            raise Exception('el nombre del estacionamiento debe existir')
        self._nombreEst = estacionamiento
        
    #Validacion de la direccion del estacionamiento        
    @property
    def direccionEst(self):
        return self._direccionEst

    @direccionEst.setter
    def direccionEst(self, direccion):
        if not direccion: 
            raise Exception('debe existir una direccion asociada al estacionamiento')
        self._direccionEst = direccion
     
    #Validacion de los telefonos   
    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, tlf):
        
        i=0
        if len(tlf)<1 or len(tlf)>3:
            raise Exception('Deben haber entre 1 y 3 telefonos asociados al estacionamiento')
        else:
            while i<len(tlf):
                if (not match('^0?4[12][46]-?[0-9]{7}$',str(tlf[i])) and
                    not match('^0?[24]12-?[0-9]{7}$',str(tlf[i]))):
                
                    raise Exception('Telefono(s) con formato incorrecto')
                i+=1
            self._telefono = tlf
    
    #Validacion de los correos   
    @property
    def correo(self):
        return self._correo

    
    @correo.setter
    def correo(self, correo):
        i=0
        if len(correo) <1 or len(correo)>2: 
            raise Exception('Deben haber entre 1 y 2 correos asociados al estacionamiento')
        else:
            while i<len(correo):
                if not match('^[0-9a-zA-Z-_]+@[0-9a-zA-Z]+\.com$',str(correo[i])):
                    raise Exception('Correo(s) con formato incorrecto')
                i+=1
        self._correo = correo
    
    #Validacion del RIF    
    @property
    def rif(self):
        return self._rif

    @rif.setter
    def rif(self, rif):
        if not rif: 
            raise Exception('debe haber un RIF asociado al estacionamiento')
        self._rif = rif
 
    def __str__(self):
        return ("Dueno: "+self.nombreDueno+
                "\nEstacionamiento: "+self.nombreEst+
                "\nDireccion: "+self.direccionEst+
                "\nRIF: "+ self.rif+
                "\nTelefonos: "+self.imprimirInfo(self.telefono)+
                "\nCorreos: "+self.imprimirInfo(self.correo)+"\n")
    
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
        
    
