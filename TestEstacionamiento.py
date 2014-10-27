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
        self.assertTrue(Estacionamiento("Luis Perez", "Estacionamiento CCS",
                                        "Urb el placer, CC. Colinas del placer",
                                        "J-2992823",04241033434,"SAGE@usb.ve"))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()