#!/usr/bin/env python
# -*- coding: utf_8 -*-

from django.test import TestCase
from SAGE.views import estacionamiento_ficticio, verificarReserva, verificar_minimo_reserva
from datetime import timedelta
from Sist_SAGE.forms import EstacionamientoForm, PagoForm, ReservaForm
# Create your tests here.

class EstacionamientoFormTests(TestCase):
    def test_Estacionamiento_campo_obligatorio_dueno_vacio(self):
        form_data = {'nombreEst': 'CC Plaza', 'nombreDueno': '',
                     'direccionEst':'CC Plaza','correo_1':'sage@gmail.com',
                     'telefono_1':'04141111111','rif':'J-232323',
                      'puestos':'50','horaApertura':"10",
                      'minApertura':'40','horaCierre':'12', 
                      'minCierre':'50','tarifa':'300'}
        form = EstacionamientoForm(data=form_data)
        self.assertEqual(form.is_valid(), False)   
         
    def test_Estacionamiento_campo_obligatorio_nombre_estacionamiento_vacio(self):
        form_data = {'nombreEst': '', 'nombreDueno': 'Luis',
                     'direccionEst':'CC Plaza','correo_1':'sage@gmail.com',
                     'telefono_1':'04141111111','rif':'J-232323',
                      'puestos':'50','horaApertura':"10",
                      'minApertura':'40','horaCierre':'12', 
                      'minCierre':'50','tarifa':'300'}
        form = EstacionamientoForm(data=form_data)
        self.assertEqual(form.is_valid(), False)  
        
    def test_Estacionamiento_campo_obligatorio_direccion_vacio(self):
        form_data = {'nombreEst': 'CC Plaza', 'nombreDueno': 'Luis',
                     'direccionEst':'','correo_1':'sage@gmail.com',
                     'telefono_1':'04141111111','rif':'J-232323',
                      'puestos':'50','horaApertura':"10",
                      'minApertura':'40','horaCierre':'12', 
                      'minCierre':'50','tarifa':'300'}
        form = EstacionamientoForm(data=form_data)
        self.assertEqual(form.is_valid(), False)   
        
    def test_Estacionamiento_campo_obligatorio_correo_vacio(self):
        form_data = {'nombreEst': 'CC Plaza', 'nombreDueno': 'Luis',
                     'direccionEst':'La Boyera','correo_1':'',
                     'telefono_1':'04141111111','rif':'J-232323',
                      'puestos':'50','horaApertura':"10",
                      'minApertura':'40','horaCierre':'12', 
                      'minCierre':'50','tarifa':'300'}
        form = EstacionamientoForm(data=form_data)
        self.assertEqual(form.is_valid(), False)
        
    def test_Estacionamiento_campo_obligatorio_rif_vacio(self):
        form_data = {'nombreEst': 'CC Plaza', 'nombreDueno': 'Luis',
                     'direccionEst':'La Boyera','correo_1':'sage@usb.ve',
                     'telefono_1':'04141111111','rif':'',
                      'puestos':'50','horaApertura':"10",
                      'minApertura':'40','horaCierre':'12', 
                      'minCierre':'50','tarifa':'300'}
        form = EstacionamientoForm(data=form_data)
        self.assertEqual(form.is_valid(), False)
        
    def test_Estacionamiento_campo_obligatorio_capidad_vacio(self):
        form_data = {'nombreEst': 'CC Plaza', 'nombreDueno': 'Luis',
                     'direccionEst':'La Boyera','correo_1':'sage@usb.ve',
                     'telefono_1':'04141111111','rif':'J-2322322',
                      'puestos':'','horaApertura':"10",
                      'minApertura':'40','horaCierre':'12', 
                      'minCierre':'50','tarifa':'300'}
        form = EstacionamientoForm(data=form_data)
        self.assertEqual(form.is_valid(), False) 
           
    def test_Estacionamiento_campo_obligatorio_horaApertura_vacio(self):
        form_data = {'nombreEst': 'CC Plaza', 'nombreDueno': 'Luis',
                     'direccionEst':'La Boyera','correo_1':'sage@usb.ve',
                     'telefono_1':'04141111111','rif':'J-2323232',
                      'puestos':'50','horaApertura':"",
                      'minApertura':'40','horaCierre':'12', 
                      'minCierre':'50','tarifa':'300'}       
        form = EstacionamientoForm(data=form_data)
        self.assertEqual(form.is_valid(), False)      
        
    def test_Estacionamiento_campo_obligatorio_minApertura_vacio(self):
        form_data = {'nombreEst': 'CC Plaza', 'nombreDueno': 'Luis',
                     'direccionEst':'La Boyera','correo_1':'sage@usb.ve',
                     'telefono_1':'04141111111','rif':'J-2323232',
                      'puestos':'50','horaApertura':"12",
                      'minApertura':'','horaCierre':'12', 
                      'minCierre':'50','tarifa':'300'}       
        form = EstacionamientoForm(data=form_data)
        self.assertEqual(form.is_valid(), False)    
        
    def test_Estacionamiento_campo_obligatorio_horaClausura_vacio(self):
        form_data = {'nombreEst': 'CC Plaza', 'nombreDueno': 'Luis',
                     'direccionEst':'La Boyera','correo_1':'sage@usb.ve',
                     'telefono_1':'04141111111','rif':'J-2323232',
                      'puestos':'50','horaApertura':"12",
                      'minApertura':'40','horaCierre':'', 
                      'minCierre':'50','tarifa':'300'}       
        form = EstacionamientoForm(data=form_data)
        self.assertEqual(form.is_valid(), False)    
        
    def test_Estacionamiento_campo_obligatorio_minClausura_vacio(self):
        form_data = {'nombreEst': 'CC Plaza', 'nombreDueno': 'Luis',
                     'direccionEst':'La Boyera','correo_1':'sage@usb.ve',
                     'telefono_1':'04141111111','rif':'J-2323232',
                      'puestos':'50','horaApertura':"12",
                      'minApertura':'40','horaCierre':'20', 
                      'minCierre':'','tarifa':'300'}       
        form = EstacionamientoForm(data=form_data)
        self.assertEqual(form.is_valid(), False)        
        
    def test_Estacionamiento_campo_obligatorio_tarifa_vacio(self):
        form_data = {'nombreEst': 'CC Plaza', 'nombreDueno': 'Luis',
                     'direccionEst':'La Boyera','correo_1':'sage@usb.ve',
                     'telefono_1':'04141111111','rif':'J-2323232',
                      'puestos':'50','horaApertura':"12",
                      'minApertura':'40','horaCierre':'15', 
                      'minCierre':'50','tarifa':''}       
        form = EstacionamientoForm(data=form_data)
        self.assertEqual(form.is_valid(), False)  
        
    def test_Estacionamiento_duenoConNumeros(self):
        form_data = {'nombreEst': 'CC Plaza', 'nombreDueno': 'Luis33',
                     'direccionEst':'La Boyera','correo_1':'sage@usb.ve',
                     'telefono_1':'04141111111','rif':'J-2323232',
                      'puestos':'50','horaApertura':"12",
                      'minApertura':'40','horaCierre':'15', 
                      'minCierre':'50','tarifa':'200'}       
        form = EstacionamientoForm(data=form_data)
        self.assertEqual(form.is_valid(), False)    
        
    def test_Estacionamiento_correo_formato_invalido(self):
        form_data = {'nombreEst': 'CC Plaza', 'nombreDueno': 'Luis',
                     'direccionEst':'La Boyera','correo_1':'sage@usb...ve',
                     'telefono_1':'04141111111','rif':'J-2323232',
                      'puestos':'50','horaApertura':"12",
                      'minApertura':'40','horaCierre':'15', 
                      'minCierre':'50','tarifa':'200'}       
        form = EstacionamientoForm(data=form_data)
        self.assertEqual(form.is_valid(), False)  
        
            
    def test_Estacionamiento_telefono_formato_invalido(self):
        form_data = {'nombreEst': 'CC Plaza', 'nombreDueno': 'Luis',
                     'direccionEst':'La Boyera','correo_1':'sage@usb.ve',
                     'telefono_1':'04141111111333','rif':'J-2323232',
                      'puestos':'50','horaApertura':"12",
                      'minApertura':'40','horaCierre':'15', 
                      'minCierre':'50','tarifa':'200'}       
        form = EstacionamientoForm(data=form_data)
        self.assertEqual(form.is_valid(), False) 
        
    def test_Estacionamiento_puestos_cero(self):
        form_data = {'nombreEst': 'CC Plaza', 'nombreDueno': 'Luis',
                     'direccionEst':'La Boyera','correo_1':'sage@usb.ve',
                     'telefono_1':'04141111111333','rif':'J-2323232',
                      'puestos':'0','horaApertura':"12",
                      'minApertura':'40','horaCierre':'15', 
                      'minCierre':'50','tarifa':'200'}       
        form = EstacionamientoForm(data=form_data)
        self.assertEqual(form.is_valid(), False)
        
    def test_horaApertura_invalida_mayor23(self):
        form_data = {'nombreEst': 'CC Plaza', 'nombreDueno': 'Luis',
                     'direccionEst':'La Boyera','correo_1':'sage@usb.ve',
                     'telefono_1':'04141111111333','rif':'J-2323232',
                      'puestos':'10','horaApertura':"24",
                      'minApertura':'40','horaCierre':'15', 
                      'minCierre':'50','tarifa':'200'}       
        form = EstacionamientoForm(data=form_data)
        self.assertEqual(form.is_valid(), False)   
        
    def test_horaClausura_invalida_mayor23(self):
        form_data = {'nombreEst': 'CC Plaza', 'nombreDueno': 'Luis',
                     'direccionEst':'La Boyera','correo_1':'sage@usb.ve',
                     'telefono_1':'04141111111333','rif':'J-2323232',
                      'puestos':'10','horaApertura':"23",
                      'minApertura':'40','horaCierre':'24', 
                      'minCierre':'50','tarifa':'200'}       
        form = EstacionamientoForm(data=form_data)
        self.assertEqual(form.is_valid(), False) 
        
    def test_horaApertura_invalida_menor0(self):
        form_data = {'nombreEst': 'CC Plaza', 'nombreDueno': 'Luis',
                     'direccionEst':'La Boyera','correo_1':'sage@usb.ve',
                     'telefono_1':'04141111111333','rif':'J-2323232',
                      'puestos':'10','horaApertura':"-1",
                      'minApertura':'40','horaCierre':'23', 
                      'minCierre':'50','tarifa':'200'}       
        form = EstacionamientoForm(data=form_data)
        self.assertEqual(form.is_valid(), False) 
        
    def test_horaClausura_invalida_menor0(self):
        form_data = {'nombreEst': 'CC Plaza', 'nombreDueno': 'Luis',
                     'direccionEst':'La Boyera','correo_1':'sage@usb.ve',
                     'telefono_1':'04141111111333','rif':'J-2323232',
                      'puestos':'10','horaApertura':"23",
                      'minApertura':'40','horaCierre':'23', 
                      'minCierre':'-1','tarifa':'200'}       
        form = EstacionamientoForm(data=form_data)
        self.assertEqual(form.is_valid(), False)      
        
    def test_minApertura_invalida_mayor59(self):
        form_data = {'nombreEst': 'CC Plaza', 'nombreDueno': 'Luis',
                     'direccionEst':'La Boyera','correo_1':'sage@usb.ve',
                     'telefono_1':'04141111111333','rif':'J-2323232',
                      'puestos':'10','horaApertura':"23",
                      'minApertura':'60','horaCierre':'23', 
                      'minCierre':'50','tarifa':'200'}       
        form = EstacionamientoForm(data=form_data)
        self.assertEqual(form.is_valid(), False)   
        
        
    def test_minClausura_invalida_mayor59(self):
        form_data = {'nombreEst': 'CC Plaza', 'nombreDueno': 'Luis',
                     'direccionEst':'La Boyera','correo_1':'sage@usb.ve',
                     'telefono_1':'04141111111333','rif':'J-2323232',
                      'puestos':'10','horaApertura':"23",
                      'minApertura':'40','horaCierre':'23', 
                      'minCierre':'60','tarifa':'200'}       
        form = EstacionamientoForm(data=form_data)
        self.assertEqual(form.is_valid(), False)
          
    def test_minApertura_invalida_menor0(self):
        form_data = {'nombreEst': 'CC Plaza', 'nombreDueno': 'Luis',
                     'direccionEst':'La Boyera','correo_1':'sage@usb.ve',
                     'telefono_1':'04141111111333','rif':'J-2323232',
                      'puestos':'10','horaApertura':"23",
                      'minApertura':'-1','horaCierre':'23', 
                      'minCierre':'50','tarifa':'200'}       
        form = EstacionamientoForm(data=form_data)
        self.assertEqual(form.is_valid(), False)
        
    def test_minClausura_invalida_menor0(self):
        form_data = {'nombreEst': 'CC Plaza', 'nombreDueno': 'Luis',
                     'direccionEst':'La Boyera','correo_1':'sage@usb.ve',
                     'telefono_1':'04141111111333','rif':'J-2323232',
                      'puestos':'10','horaApertura':"23",
                      'minApertura':'-1','horaCierre':'23', 
                      'minCierre':'50','tarifa':'200'}       
        form = EstacionamientoForm(data=form_data)
        self.assertEqual(form.is_valid(), False)  
        
    def test_tarifa_invalida_menor0(self):
        form_data = {'nombreEst': 'CC Plaza', 'nombreDueno': 'Luis',
                     'direccionEst':'La Boyera','correo_1':'sage@usb.ve',
                     'telefono_1':'04141111111333','rif':'J-2323232',
                      'puestos':'10','horaApertura':"23",
                      'minApertura':'20','horaCierre':'23', 
                      'minCierre':'50','tarifa':'0'}       
        form = EstacionamientoForm(data=form_data)
        self.assertEqual(form.is_valid(), False)                             

class ReservaFormTests(TestCase):
        def test_horaInicio_mayor23(self):
            form_data = {'horaInicio':"24",'minInicio':'20',
                         'horaFin':'23', 'minFin':'50'}       
            form = ReservaForm(data=form_data)
            self.assertEqual(form.is_valid(), False) 
            
        def test_horaFin_mayor23(self):
            form_data = {'horaInicio':"23",'minInicio':'20',
                         'horaFin':'24', 'minFin':'50'}       
            form = ReservaForm(data=form_data)
            self.assertEqual(form.is_valid(), False)  
            
        def test_horaInicio_menor0(self):
            form_data = {'horaInicio':"-1",'minInicio':'20',
                         'horaFin':'23', 'minFin':'50'}       
            form = ReservaForm(data=form_data)
            self.assertEqual(form.is_valid(), False) 
            
        def test_horaFin_menor0(self):
            form_data = {'horaInicio':"23",'minInicio':'20',
                         'horaFin':'-1', 'minFin':'50'}       
            form = ReservaForm(data=form_data)
            self.assertEqual(form.is_valid(), False)   
            
        def test_minInicio_mayor59(self):
            form_data = {'horaInicio':"23",'minInicio':'60',
                         'horaFin':'23', 'minFin':'50'}       
            form = ReservaForm(data=form_data)
            self.assertEqual(form.is_valid(), False) 
            
        def test_minFin_mayor59(self):
            form_data = {'horaInicio':"23",'minInicio':'59',
                         'horaFin':'23', 'minFin':'60'}       
            form = ReservaForm(data=form_data)
            self.assertEqual(form.is_valid(), False) 
            
        def test_minInicio_menor0(self):
            form_data = {'horaInicio':"2",'minInicio':'-1',
                         'horaFin':'23', 'minFin':'50'}       
            form = ReservaForm(data=form_data)
            self.assertEqual(form.is_valid(), False) 
            
        def test_minFin_menor0(self):
            form_data = {'horaInicio':"2",'minInicio':'20',
                         'horaFin':'23', 'minFin':'-1'}       
            form = ReservaForm(data=form_data)
            self.assertEqual(form.is_valid(), False) 
            

class ReservaTests(TestCase):
    
    global _puestos
    _puestos=estacionamiento_ficticio()
    
    def test_minimo_reserva_horaInicio_cero(self ):
        inicioReserva =timedelta(hours=0,minutes=0)
        finReserva =timedelta(hours=1,minutes=0)
        self.assertTrue(verificar_minimo_reserva(inicioReserva, finReserva))
                
    def test_minimo_reserva_cero(self):
        inicioReserva =timedelta(hours=0,minutes=0)
        finReserva =timedelta(hours=0,minutes=0)
        self.assertFalse(verificar_minimo_reserva(inicioReserva, finReserva))
    
    def test_minimo_reserva_minimo_1_hora(self ):
        inicioReserva =timedelta(hours=5,minutes=30)
        finReserva =timedelta(hours=6,minutes=29)
        self.assertFalse(verificar_minimo_reserva(inicioReserva, finReserva))
        
    def test_minimo_reserva_minimo_1_hora_horaInicio_mayor_horaFin(self ):
        inicioReserva =timedelta(hours=5,minutes=30)
        finReserva =timedelta(hours=4,minutes=31)
        self.assertTrue(verificar_minimo_reserva(inicioReserva, finReserva))
        
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
        
    def test_rechazo_reserva(self):
        global _puestos
        inicioReserva =timedelta(hours=13,minutes=30)
        finReserva =timedelta(hours=14,minutes=30)
        self.assertFalse(verificarReserva(_puestos, inicioReserva, finReserva)) 
    

class IntegracionFormatoSolicitudYDisponibilidad(TestCase):
    
    def test_solicitud_posible_primera_hora(self):
        form_data = {'horaInicio':"5",'minInicio':'20',
                     'horaFin':'7', 'minFin':'40'}       
        form = ReservaForm(data=form_data)
        model=form.save(commit=False)
        inicio=timedelta(hours=int(model.horaInicio),minutes=int(model.minInicio))
        fin=timedelta(hours=int(model.horaFin),minutes=int(model.minFin))
        self.assertTrue(verificarReserva(estacionamiento_ficticio(), inicio, fin))
        
    def test_solicitud_posible_ultima_hora(self):
        form_data = {'horaInicio':"20",'minInicio':'20',
                     'horaFin':'23', 'minFin':'40'}       
        form = ReservaForm(data=form_data)
        model=form.save(commit=False)
        inicio=timedelta(hours=int(model.horaInicio),minutes=int(model.minInicio))
        fin=timedelta(hours=int(model.horaFin),minutes=int(model.minFin))
        self.assertTrue(verificarReserva(estacionamiento_ficticio(), inicio, fin))
        
    def test_solicitud_posible_entre2Reservas(self):
        form_data = {'horaInicio':"10",'minInicio':'30',
                     'horaFin':'11', 'minFin':'30'}       
        form = ReservaForm(data=form_data)
        model=form.save(commit=False)
        inicio=timedelta(hours=int(model.horaInicio),minutes=int(model.minInicio))
        fin=timedelta(hours=int(model.horaFin),minutes=int(model.minFin))
        self.assertTrue(verificarReserva(estacionamiento_ficticio(), inicio, fin))
        
    def test_solicitud_infactible(self):
        form_data = {'horaInicio':"13",'minInicio':'20',
                     'horaFin':'14', 'minFin':'20'}       
        form = ReservaForm(data=form_data)
        model=form.save(commit=False)
        inicio=timedelta(hours=int(model.horaInicio),minutes=int(model.minInicio))
        fin=timedelta(hours=int(model.horaFin),minutes=int(model.minFin))
        self.assertFalse(verificarReserva(estacionamiento_ficticio(), inicio, fin))
    
    
    
    
    
class PagoFormTests(TestCase):
    def test_Pago_campo_obligatorio_nombre_vacio(self):
        form_data = {'nombre': '', 'cedula': '21289762',
                     'tipoTarjeta':'Visa','digitos':'1234123412341234',
                     'anoVencimiento':'2015','mesVencimiento':'10',
                     'codigoSeguridad':'504'}
        form = PagoForm(data=form_data)
        self.assertEqual(form.is_valid(), False) 
         
    def test_Pago_campo_obligatorio_cedula_vacio(self):
        form_data = {'nombre': 'Luis', 'cedula': '',
                     'tipoTarjeta':'Visa','digitos':'1234123412341234',
                     'anoVencimiento':'2015','mesVencimiento':'10',
                     'codigoSeguridad':'504'}
        form = PagoForm(data=form_data)
        self.assertEqual(form.is_valid(), False)  
        
    def test_Pago_campo_obligatorio_tipoTarjeta_vacio(self):
        form_data = {'nombre': 'Luis', 'cedula': '21289762',
                     'tipoTarjeta':'','digitos':'1234123412341234',
                     'anoVencimiento':'2015','mesVencimiento':'10',
                     'codigoSeguridad':'504'}
        form = PagoForm(data=form_data)
        self.assertEqual(form.is_valid(), False)  
        
    def test_Pago_campo_obligatorio_digitos_vacio(self):
        form_data = {'nombre': 'Luis', 'cedula': '21289762',
                     'tipoTarjeta':'Visa','digitos':'',
                     'anoVencimiento':'2015','mesVencimiento':'10',
                     'codigoSeguridad':'504'}
        form = PagoForm(data=form_data)
        self.assertEqual(form.is_valid(), False)  
        
    def test_Pago_campo_obligatorio_ano_vacio(self):
        form_data = {'nombre': 'Luis', 'cedula': '21289762',
                     'tipoTarjeta':'Visa','digitos':'1234123412341234',
                     'anoVencimiento':'','mesVencimiento':'10',
                     'codigoSeguridad':'504'}
        form = PagoForm(data=form_data)
        self.assertEqual(form.is_valid(), False)  
        
    def test_Pago_campo_obligatorio_mes_vacio(self):
        form_data = {'nombre': 'Luis', 'cedula': '21289762',
                     'tipoTarjeta':'Visa','digitos':'1234123412341234',
                     'anoVencimiento':'2015','mesVencimiento':'',
                     'codigoSeguridad':'504'}
        form = PagoForm(data=form_data)
        self.assertEqual(form.is_valid(), False)  

    def test_Pago_campo_obligatorio_codigoSeg_vacio(self):
        form_data = {'nombre': '', 'cedula': '21289762',
                     'tipoTarjeta':'Visa','digitos':'1234123412341234',
                     'anoVencimiento':'2015','mesVencimiento':'10',
                     'codigoSeguridad':''}
        form = PagoForm(data=form_data)
        self.assertEqual(form.is_valid(), False)  
    
    def test_Pago_campo_nombre_conNumeros(self):
        form_data = {'nombre': 'Luis8', 'cedula': '21289762',
                     'tipoTarjeta':'Visa','digitos':'1234123412341234',
                     'anoVencimiento':'2015','mesVencimiento':'10',
                     'codigoSeguridad':'504'}
        form = PagoForm(data=form_data)
        self.assertEqual(form.is_valid(), False)
        
    def test_Pago_campo_nombre_conEspaciado(self):
        form_data = {'nombre': 'Luis Miglietti', 'cedula': '21289762',
                     'tipoTarjeta':'Visa','digitos':'1234123412341234',
                     'anoVencimiento':'2015','mesVencimiento':'10',
                     'codigoSeguridad':'504'}
        form = PagoForm(data=form_data)
        self.assertEqual(form.is_valid(), True)    
        
    def test_Pago_campo_cedula_conLetras(self):
        form_data = {'nombre': 'Luis', 'cedula': '21289762a',
                     'tipoTarjeta':'Visa','digitos':'1234123412341234',
                     'anoVencimiento':'2015','mesVencimiento':'10',
                     'codigoSeguridad':'504'}
        form = PagoForm(data=form_data)
        self.assertEqual(form.is_valid(), False)  
        
    def test_Pago_campo_cedula_MaxTamano(self):
        form_data = {'nombre': 'Luis8', 'cedula': '21289762899',
                     'tipoTarjeta':'Visa','digitos':'1234123412341234',
                     'anoVencimiento':'2015','mesVencimiento':'10',
                     'codigoSeguridad':'504'}
        form = PagoForm(data=form_data)
        self.assertEqual(form.is_valid(), False)

    
    def test_Pago_campo_Tipotarjeta_invalido(self):
        form_data = {'nombre': 'Luis', 'cedula': '21289762',
                     'tipoTarjeta':'BlackCard','digitos':'1234123412341234',
                     'anoVencimiento':'2015','mesVencimiento':'10',
                     'codigoSeguridad':'504'}
        form = PagoForm(data=form_data)
        self.assertEqual(form.is_valid(), False)   
        
    def test_Pago_campo_digitos_menor16(self):
        form_data = {'nombre': 'Luis', 'cedula': '21289762',
                     'tipoTarjeta':'Visa','digitos':'123412341234134',
                     'anoVencimiento':'2015','mesVencimiento':'10',
                     'codigoSeguridad':'504'}
        form = PagoForm(data=form_data)
        self.assertEqual(form.is_valid(), False)
        
    def test_Pago_campo_digitos_mayor16(self):
        form_data = {'nombre': 'Luis', 'cedula': '21289762',
                     'tipoTarjeta':'Visa','digitos':'12341234123413477',
                     'anoVencimiento':'2015','mesVencimiento':'10',
                     'codigoSeguridad':'504'}
        form = PagoForm(data=form_data)
        
    def test_Pago_campo_anoVencimiento_menorFechaActual(self):
        form_data = {'nombre': 'Luis', 'cedula': '21289762',
                     'tipoTarjeta':'Visa','digitos':'1234123412341234',
                     'anoVencimiento':'2013','mesVencimiento':'10',
                     'codigoSeguridad':'504'}
        form = PagoForm(data=form_data)
        self.assertEqual(form.is_valid(), False)  
        
        
    def test_Pago_campo_anoVencimiento_5digitos(self):
        form_data = {'nombre': 'Luis', 'cedula': '21289762',
                     'tipoTarjeta':'Visa','digitos':'1234123412341234',
                     'anoVencimiento':'20133','mesVencimiento':'10',
                     'codigoSeguridad':'504'}
        form = PagoForm(data=form_data)
        self.assertEqual(form.is_valid(), False)

        
    def test_Pago_campo_mesVencimiento_cero(self):
        form_data = {'nombre': 'Luis', 'cedula': '21289762',
                     'tipoTarjeta':'Visa','digitos':'1234123412341234',
                     'anoVencimiento':'2014','mesVencimiento':'0',
                     'codigoSeguridad':'504'}
        form = PagoForm(data=form_data)
        self.assertEqual(form.is_valid(), False)   
        
        
    def test_Pago_campo_mesVencimiento_mayor12(self):
        form_data = {'nombre': 'Luis', 'cedula': '21289762',
                     'tipoTarjeta':'Visa','digitos':'1234123412341234',
                     'anoVencimiento':'2014','mesVencimiento':'13',
                     'codigoSeguridad':'504'}
        form = PagoForm(data=form_data)
        self.assertEqual(form.is_valid(), False)     

        
    def test_Pago_campo_codigoSeguridad_menor3digitos(self):
        form_data = {'nombre': 'Luis', 'cedula': '21289762',
                     'tipoTarjeta':'Visa','digitos':'1234123412341234',
                     'codigoSeguridad':'22',
                     'anoVencimiento':'2014','mesVencimiento':'10'}
        form = PagoForm(data=form_data)
        self.assertEqual(form.is_valid(), False)
        
    def test_Pago_campo_codigoSeguridad_mayor4digitos(self):
        form_data = {'nombre': 'Luis', 'cedula': '21289762',
                     'tipoTarjeta':'Visa','digitos':'1234123412341234',
                     'codigoSeguridad':'22444',
                     'anoVencimiento':'2014','mesVencimiento':'10'}
        form = PagoForm(data=form_data)
        self.assertEqual(form.is_valid(), False)
        
