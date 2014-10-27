#!/usr/bin/env python
# -*- coding: utf_8 -*-

'''
Created on Oct 27, 2014

@author: luis
'''

class Estacionamiento(object):
    '''
    classdocs
    '''

    def __init__(self,nombreDueno, nombreEst, direccionEst,
                 telefono, correo, rif ):
        
        self.nombreDueno=nombreDueno
        self.nombreEst=nombreEst
        self.direccionEst=direccionEst
        self.telefono=telefono
        self.correo=correo
        self.rif=rif
        
    def imprimirInfo(self,info):
        for i in info:
            print info[i]
            if i < len(info):
                print " / "
        
    def __str__(self):
        print ("Dueño: ", self.nombreDueno, "\n",
               "Estacionamiento: ",self.nombreEst,"\n",
               "Dirección: ", self.direccionEst,"\n",
               "RIF: ", self.rif, "\n",
               "Telefonos: ", self.imprimirTelefono(self.telefono), "\n",
               "Correos: ", self.imprimirCorreo(self.correo), "\n")
        
        
        
           
        
        
    