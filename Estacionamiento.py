#!/usr/bin/env python
# -*- coding: utf_8 -*-

'''
Created on Oct 27, 2014

@author: luis
'''

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
        if not dueno: 
            raise Exception(u'El nombre del dueno debe existir')
        self._nombreDueno = dueno


        
    def __str__(self):
        return ("Dueno: "+self.nombreDueno+
                "\nEstacionamiento: "+self.nombreEst+
               "\nDireccion: "+self.direccionEst+
               "\nRIF: "+ self.rif+
               "\nTelefonos: "+self.imprimirInfo(self.telefono)+
               "\nCorreos: "+self.imprimirInfo(self.correo))
        
    def imprimirInfo(self,infoEstacionamiento):
        i=0
        informacion=""
        while i<len(infoEstacionamiento):
            informacion=informacion+infoEstacionamiento[i]
            i+=1
            if i < len(infoEstacionamiento):
                informacion=informacion+" / "
        return informacion
        
     
        
        
        
           
        
        
    