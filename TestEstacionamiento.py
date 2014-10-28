#!/usr/bin/env python
# -*- coding: utf_8 -*-


'''
Created on Oct 27, 2014

@author: luis
'''
import unittest
from Estacionamiento import Estacionamiento


class Test(unittest.TestCase):


    def testInicial(self):
        pass
    
    def testParametros(self):
        correo=["SAGE@USB.com","SAGERESER@USB.com"]
        telefono=["04143113333","04141234567"]
        self.assertTrue(Estacionamiento("Luis Perez", "Estacionamiento CCS",
                                        "Urb el placer, CC. Colinas del placer",
                                        telefono,correo,"J-2992823"))
    def testNombreDueno(self):
        correo=["SAGE@USB.com","SAGERESER@USB.com"]
        telefono=["04143113333","04141234567"]
        try:
            self.assertTrue(Estacionamiento('ada3', "Estacionamiento CCS",
                                        "Urb el placer, CC. Colinas del placer",
                                        telefono,correo,"J-2992823"))
        except Exception:
            print "El nombre del dueno debe existir y no puede contener numeros \n"
    
    def testNombreEstacionamiento(self):
        correo=["SAGE@USB.com","SAGERESER@USB.com"]
        telefono=["04143113333","04141234567"]
        try:
            self.assertTrue(Estacionamiento('ada',"",
                                        "Urb el placer, CC. Colinas del placer",
                                        telefono,correo,"J-2992823"))
        except Exception:
            print "El nombre del estacionamiento debe existir \n"
            
    
    def testDireccionEstacionamiento(self):
        correo=["SAGE@USB.com","SAGERESER@USB.com"]
        telefono=["04143113333","04141234567"]
        try:
            self.assertTrue(Estacionamiento('Luis', "Estacionamiento CC Plaza",
                                        "",telefono,correo,"J-2992823"))
        except Exception:
            print "Debe de existir una direccion asociada al estacionamiento \n"
            
    
    def testTelefono(self):
        correo=["SAGE@USB.com","SAGERESER@USB.com"]
        telefono=["041431133334"]
        try:
            self.assertTrue(Estacionamiento('Luis', "Estacionamiento CC Plaza",
                                        "Urb el placer",telefono,correo,"J-2992823"))
        except Exception:
            print "Telefono(s) con formato incorrecto \n"
            
    def testMaxNumeroTelefonos(self):
        correo=["SAGE@USB.com","SAGERESER@USB.com"]
        telefono=["04143113333","04241022323","04241223453","04141111111"]
        try:
            self.assertTrue(Estacionamiento('Luis', "Estacionamiento CC Plaza",
                                        "Urb el placer",telefono,correo,"J-2992823"))
        except Exception:
            print "El maximo numero de telefonos es 3 \n"
            
                
    def testTelefonoconGuion(self):
        correo=["SAGE@USB.com","SAGERESER@USB.com"]
        telefono=["0414-3113333",]
        try:
            self.assertTrue(Estacionamiento('Luis', "Estacionamiento CC Plaza",
                                        "Urb el placer",telefono,correo,"J-2992823"))
        except Exception:
            print "El formato del telefono es invalido \n"
            
    def testCorreoElectronico(self):
        correo=["adwa"]
        telefono=["0414-3113333",]
        try:
            self.assertTrue(Estacionamiento('Luis', "Estacionamiento CC Plaza",
                                        "Urb el placer",telefono,correo,"J-2992823"))
        except Exception:
            print "El formato del correo es invalido \n"
            
                
    def testMaxCorreoElectronico(self):
        correo=["luis@gmail.com","a@usb.com","adaw@tet.com"]
        telefono=["0414-3113333",]
        try:
            self.assertTrue(Estacionamiento('Luis', "Estacionamiento CC Plaza",
                                        "Urb el placer",telefono,correo,"J-2992823"))
        except Exception:
            print "El numero maximo de correos es 2 \n"
            
    
            
    
            
        
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()