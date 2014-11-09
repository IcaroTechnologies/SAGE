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
    
    def get_nombre(self):
        return self.nombreEst
		

class EstacionamientoParametrizado(Estacionamiento):
	"""docstring for EstacionamientoParametrizado"""
	def __init__(self,nombreDueno, nombreEst, direccionEst,telefono, correo, rif,
				 capacidad, horaApertura, horaClausura,tarifa,horaAperturaReserva="NA",horaClausuraReserva="NA"):

		super(EstacionamientoParametrizado, self).__init__(nombreDueno, nombreEst, direccionEst,telefono, correo, rif )
		self.capacidad = capacidad
		self.horaApertura = horaApertura
		self.horaClausura = horaClausura
		self.tarifa = tarifa
		self.horaAperturaReserva = horaAperturaReserva
		self.horaClausuraReserva = horaClausuraReserva

	def __str__(self):
		return ("Dueno: "+self.nombreDueno+
	            "\nEstacionamiento: "+self.nombreEst+
	            "\nDireccion: "+self.direccionEst+
	            "\nRIF: "+ self.rif+
	            "\nTelefonos: "+self.imprimirInfo(self.telefono)+
	            "\nCorreos: "+self.imprimirInfo(self.correo)+"\n"+
	            "\nCapacidad del Estacionamiento: "+str(self.capacidad)+
	            "\nTarifa: "+str(self.tarifa)+
	            "\nHora de Apertura: "+str(self.horaApertura)+
	            "\nHora de Clausura: "+str(self.horaClausura)+
	            "\nHora de inicio de reservas: "+str(self.horaAperturaReserva)+
                "\nHora de cierre de reservas: "+str(self.horaClausuraReserva))
		
        

    
    
