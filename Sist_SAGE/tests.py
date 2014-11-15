from django.test import TestCase
from SAGE.views import estacionamiento_ficticio, verificarReserva
from datetime import timedelta
# Create your tests here.
class ReservaTests(TestCase):
    
    global _puestos
    _puestos=estacionamiento_ficticio()
    
    def test_reserva_primera_hora(self):
        global _puestos
        inicioReserva =timedelta(hours=5,minutes=30)
        finReserva =timedelta(hours=6,minutes=30)
        self.assertTrue(verificarReserva(_puestos, inicioReserva, finReserva))
        
        
    def test_reserva_entre_reservas(self):
        global _puestos
        inicioReserva =timedelta(hours=11,minutes=30)
        finReserva =timedelta(hours=12,minutes=0)
        self.assertTrue(verificarReserva(_puestos, inicioReserva, finReserva))
        
    def test_reserva_ultima_hora(self):
        global _puestos
        inicioReserva =timedelta(hours=19,minutes=30)
        finReserva =timedelta(hours=21,minutes=30)
        self.assertTrue(verificarReserva(_puestos, inicioReserva, finReserva))
    