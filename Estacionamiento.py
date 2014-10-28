#!/usr/bin/env python
# -*- coding: utf_8 -*-

'''
Created on Oct 27, 2014

@author: luis
'''
from re import search, match, findall

class Estacionamiento(object):

    def __init__(self,nombreDueno, nombreEst, direccionEst,
                 telefono, correo, rif ):
        
        self.nombreDueno=nombreDueno
        self.nombreEst=nombreEst
        self.direccionEst=direccionEst
        self.telefono=telefono
        self.correo=correo
        self.rif=rif
        
        print self
        
    @property
    def nombreDueno(self):
        return self._nombreDueno

    @nombreDueno.setter
    def nombreDueno(self, dueno):
        if not dueno or (search('\d',dueno)): 
            raise Exception('el nombre del dueno debe existir y no puede contener numeros')
        self._nombreDueno = dueno
        
    @property
    def nombreEst(self):
        return self._nombreEst

    @nombreEst.setter
    def nombreEst(self, estacionamiento):
        if not estacionamiento: 
            raise Exception('el nombre del estacionamiento debe existir')
        self._nombreEst = estacionamiento
        
            
    @property
    def direccionEst(self):
        return self._direccionEst

    @direccionEst.setter
    def direccionEst(self, direccion):
        if not direccion: 
            raise Exception('debe existir una direccion asociada al estacionamiento')
        self._direccionEst = direccion
        
    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, tlf):
        i=0
        while i<len(tlf):
            if (not match('^0?4[12][46]-?[0-9]{7}$',str(tlf[i])) and
                not match('^0?[24]12-?[0-9]{7}$',str(tlf[i]))):
                
                raise Exception('Telefono(s) con formato incorrecto')
            i+=1
        self._telefono = tlf
 
    def __str__(self):
        return ("Dueno: "+self.nombreDueno+
                "\nEstacionamiento: "+self.nombreEst+
               "\nDireccion: "+self.direccionEst+
               "\nRIF: "+ self.rif+
               "\nTelefonos: "+self.imprimirInfo(self.telefono)+
               "\nCorreos: "+self.imprimirInfo(self.correo)+"\n")
        
    def imprimirInfo(self,infoEstacionamiento):
        i=0
        informacion=""
        while i<len(infoEstacionamiento):
            informacion=informacion+infoEstacionamiento[i]
            i+=1
            if i < len(infoEstacionamiento):
                informacion=informacion+" / "
        return informacion
        
    