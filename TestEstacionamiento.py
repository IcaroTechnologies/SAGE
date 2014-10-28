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
        correo=["SAGE@USB.VE","SAGERESER@USB.VE"]
        telefono=["04143113333","04141234567"]
        
        self.assertTrue(Estacionamiento("Luis Perez", "Estacionamiento CCS",
                                        "Urb el placer, CC. Colinas del placer",
                                        telefono,correo,"J-2992823"))
    def testNombreDueno(self):
        correo=["SAGE@USB.VE","SAGERESER@USB.VE"]
        telefono=["04143113333","04141234567"]
        try:
            self.assertRaises(Exception,Estacionamiento('', "Estacionamiento CCS",
                                        "Urb el placer, CC. Colinas del placer",
                                        telefono,correo,"J-2992823"))
        except Exception:
            print "El nombre del dueño debe existir"
            
        
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()