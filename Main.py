'''
Created on Oct 29, 2014

@author: nelson
'''
from re import search, match
<<<<<<< HEAD
from Estacionamiento import *
=======
import datetime
from Estacionamiento import *
from __builtin__ import False
>>>>>>> parametrizarEst

ListaEstacionamientos = []

def imprimiropcionionesMenu():
    print("\n---MENU PRINCIPAL---")
    print("Si desea agregar un nuevo estacionamiento marque uno (1).")
    print("Si desea agregar un nuevo estacionamiento parametrizado marque uno (2).")
    print("Si desea ver los datos de TODOS estacionamiento marque dos (3)")
    print("Para salir del sistema presione cero (0)\n")
    
def validarTelefono(telefono):
    
    if (not match('^0?4[12][46]-?[0-9]{7}$',telefono) and
        not match('^0?[24]12-?[0-9]{7}$',telefono)):
            print('Numero incorrecto, por favor vuelva a agregar el telefono')
            return False
        
    return True

def validarCorreo(correo):
  
    if not match('^[0-9a-zA-Z-_]+@[0-9a-zA-Z]+\.[0-9a-zA-Z]+$',correo):
            print('Correo incorrecto, por favor vuelva a agregar el telefono')
            return False
        
    return True

def validarDueno(nombre):
    
    if not nombre or (search('\d',nombre)): 
            print('el nombre del dueno debe existir y no puede contener numeros')
            return False
    return True

def validarNombre(nombre):
    if not nombre: 
        print('El campo debe existir')
        return False
    return True
    
def validarCantidad(Capacidad):
    if not Capacidad or Capacidad <=0: 
        print('El campo debe existir y la capacidad tiene que ser mayor a cero')
        return False
    return True

<<<<<<< HEAD
def validarHora(Hora):
    if not Capacidad or Capacidad <=0: 
        print('El campo debe existir y la capacidad tiene que ser mayor a cero')
        return False
    return True


=======
def validarDatoEntero(hora):
    if not hora:
        return False
    return True

def validarHora(hora):
    if hora > 23 or hora < 0:
        return False
    return True

def validarMinuto(minuto):
    if minuto > 60 or minuto < 0:
        return False
    return True
>>>>>>> parametrizarEst
        
def obtenerTelefonos():
    
    i = 0
    opcion = 1
    telefono = []
    
    while opcion == 1 and i < 3:
        entrada = raw_input("Introduzca un n. de telefono (movil o local de caracas): ")
        while not validarTelefono(entrada):
            entrada = str(raw_input("Introduzca un n. de telefono (movil o local de caracas): "))
                
        if not(entrada in telefono):    
            telefono.append(entrada)
            i = i + 1
        else:
            print("\nNumero de telefono ya existente. Por favor introduzca un nuevo numero.")
            
        if i < 3:
            opcion = int(raw_input("Si desea agregar otro numero de telefono marque uno(1). "
                               + "De lo contrario marque cero (0): "))
<<<<<<< HEAD
            while opcion != 0 and opcion != 1:
                print("Opcion invalida, vuelva a intentar.")
                opcion = int(raw_input("Si desea agregar otro numero de telefono marque uno(1). "
                                    + "De lo contrario marque cero(0): "))
=======
            while  int(opcion != 0 and opcion != 1):
                print("Opcion invalida, vuelva a intentar.")
                opcion = int(raw_input("Si desea agregar otro numero de telefono marque uno(1). "
                                    + "De lo contrario marque cero(0): "))
                print opcion
>>>>>>> parametrizarEst
                
    return telefono

def obtenerCorreo():
    
    correo = []
    opcion = 1
    i = 0
    
    while opcion == 1 and i < 2:
        entrada = str(raw_input("Intoduzca un correo electronico (Ej. sage@hotmail.com): "))
        while not validarCorreo(entrada):
            entrada = str(raw_input("Intoduzca un correo electronico (Ej. sage@hotmail.com): "))
        
        if not(entrada in correo):    
            correo.append(entrada)
            i = i + 1
        else:
            print("\nEl correo ya existe. Por favor introduzca una nueva direccion de correo.")
        if i < 2:
            opcion = int(raw_input("Si desea agregar otra direccion de correo electronico marque uno(1). "
                               + "De lo contrario marque cero(0): "))
<<<<<<< HEAD
            while opcion != 0 and opcion != 1:
=======
            while  (opcion != 0 and opcion != 1):
>>>>>>> parametrizarEst
                print("Opcion invalida, vuelva a intentar.")
                opcion = int(raw_input("Si desea agregar otra direccion de correo electronico marque uno(1). "
                                   + "De lo contrario marque cero(0): "))
    return correo

            
def imprimirEstacionamientos(ListaEstacionamientos):
    
    if len(ListaEstacionamientos) == 0:
        print("\nNo se ha registrado ningun estacionamiento.\n")
    else:
        print("\n**ESTACIONAMIENTOS REGISTRADOS**\n\n")
        for i in ListaEstacionamientos:
            print i
            
def obtenerDueno():

    nombreDueno = str(raw_input("Introduzca el nombre del dueno del estacionamiento: "))
    while not validarDueno(nombreDueno):
        nombreDueno = str(raw_input("Introduzca el nombre del dueno del estacionamiento: "))
    return nombreDueno

def obtenerRif():
    
    rif = str(raw_input("Introduzca el rif de la empresa: "))
    while not validarNombre(rif):
        rif = str(raw_input("Introduzca el rif de la empresa: "))
    return rif
    
def obtenerDireccion():

    direccionEst = str(raw_input("Indique la direccion del estacionamiento: "))  
    while not validarNombre(direccionEst):
        direccionEst = str(raw_input("Indique la direccion del estacionamiento: "))  
    return direccionEst
    
def obtenerNombreEstacionamiento():
    nombreEst = raw_input("Indique el nombre del estacionamiento: ")    
    while not validarNombre(nombreEst):
        nombreEst = str(raw_input("Indique el nombre del estacionamiento: "))
    return nombreEst  

def obtenerCapacidad():
    Capacidad = int(raw_input("Indique la capacidad del estacionamiento: "))    
    while not validarCantidad(Capacidad):
        Capacidad = int(raw_input("Indique la capacidad del estacionamiento: "))
    return Capacidad  

def obtenerHoraApertura():
<<<<<<< HEAD
    Hora = str(raw_input("Indique la Hora de Apertura del estacionamiento en el siguiente formato '(hh:mm)':  "))    
    #while not validarHora(Hora):
    #    Hora = str(raw_input("Indique la Hora de Apertura del estacionamiento en el siguiente formato '(hh:mm)':  "))
    return Hora

def obtenerHoraClausura():
    Hora = str(raw_input("Indique la Hora de Apertura del estacionamiento en el siguiente formato '(hh:mm)':  "))    
    #while not validarHora(Hora):
    #    Hora = str(raw_input("Indique la Hora de Apertura del estacionamiento en el siguiente formato '(hh:mm)':  "))
    return Hora  	  	
    
def obtenerTarifa():
    Tarifa = str(raw_input("Indique la Tarifa del estacionamiento en BsF:  "))    
    #while not validarTarifa(Tarifa):
    #    Tarifa = str(raw_input("Indique la Tarifa de Apertura del estacionamiento en el siguiente formato '(hh:mm)':  "))
    return Tarifa  	

def obtenerHoraAperturaReserva():
    HoraAperturaReserva = str(raw_input("Indique la Hora de Apertura de la Reserva del estacionamiento en el siguiente formato '(hh:mm)':  "))    
    #while not validarHoraAperturaReserva(HoraAperturaReserva):
    #    HoraAperturaReserva = str(raw_input("Indique la HoraAperturaReserva de Apertura del estacionamiento en el siguiente formato '(hh:mm)':  "))
    return HoraAperturaReserva  

def obtenerHoraClausuraReserva():			
    HoraClausuraReserva = str(raw_input("Indique la Hora de Clausura de la Reserva del estacionamiento en el siguiente formato '(hh:mm)':  "))    
    #while not validarHoraClausuraReserva(HoraClausuraReserva):
    #    HoraClausuraReserva = str(raw_input("Indique la HoraClausuraReserva de Apertura del estacionamiento en el siguiente formato '(hh:mm)':  "))
    return HoraClausuraReserva  
=======
    Hora = int(raw_input("Indique la Hora de Apertura del estacionamiento en formato militar (sin minutos) :"))
    Min =  int(raw_input("Indique los minutos :"))
    while not (validarHora(Hora) or not validarMinuto(Min) or
        not validarDatoEntero(Hora) or not validarDatoEntero(Min)):
        Hora = int(raw_input("Indique la Hora de Apertura del estacionamiento en formato militar (sin minutos) :"))
        Min =  int(raw_input("Indique los minutos :"))  
    return datetime.timedelta(hours=Hora,minutes=Min)

def obtenerHoraClausura():
    Hora = int(raw_input("Indique la Hora de Clausura del estacionamiento en formato militar (sin minutos) :"))
    Min =  int(raw_input("Indique los minutos :"))
    while not (validarHora(Hora) or not validarMinuto(Min) or
          not validarDatoEntero(Hora) or not validarDatoEntero(Min)):
        Hora = int(raw_input("Indique la Hora de Clausura del estacionamiento en formato militar (sin minutos) :"))
        Min =  int(raw_input("Indique los minutos :"))
    return datetime.timedelta(hours=Hora,minutes=Min) 	  	
    
def obtenerTarifa():
    Tarifa = int(raw_input("Indique la Tarifa del estacionamiento en BsF:  "))    
    while not validarDatoEntero(Tarifa):
        Tarifa = int(raw_input("Indique la Tarifa de Apertura del estacionamiento en el siguiente formato '(hh:mm)':  "))
    return Tarifa  	

def obtenerHoraAperturaReserva():
    Hora = int(raw_input("Indique la Hora de Apertura de reservas del estacionamiento en formato militar (sin minutos) :"))
    Min =  int(raw_input("Indique los minutos  :"))
    while not (validarHora(Hora) or not validarMinuto(Min) or
        not validarDatoEntero(Hora) or not validarDatoEntero(Min)):
        Hora = int(raw_input("Indique la Hora de Apertura de reservas del estacionamiento en formato militar (sin minutos) :"))
        Min =  int(raw_input("Indique los minutos  :"))
    return datetime.timedelta(hours=Hora,minutes=Min)     
 

def obtenerHoraClausuraReserva():			
    Hora = int(raw_input("Indique la Hora de Clausura de reservas del estacionamiento en formato militar (sin minutos) :"))
    Min =  int(raw_input("Indique los minutos  :"))
    while not (validarHora(Hora) or not validarMinuto(Min) or
    not validarDatoEntero(Hora) or not validarDatoEntero(Min)):
        Hora = int(raw_input("Indique la Hora de Clausura de reservas del estacionamiento en formato militar (sin minutos) :"))
        Min =  int(raw_input("Indique los minutos  :"))
    return datetime.timedelta(hours=Hora,minutes=Min)     
 
>>>>>>> parametrizarEst

def menu(ListaEstacionamientos):
    opcion = 1
    ListaEstacionamientos=[]
    print("\nBienvenido al Sistema Automatizado de Gestion de Estacionamientos.\n") 
    while opcion != 0:
        imprimiropcionionesMenu()
        opcion = int(raw_input("Introduzca el numero de su opcion: "))
        if opcion == 1:
            if len(ListaEstacionamientos) >= 5:
                print("\nError, no se puede agregar un nuevo estacionamiento,"
                      + "porque se ha llegado al limite.\n")
            else:
                print("\n**AGREGAR ESTACIONAMIENTO**\n")
                
                nombreDueno = obtenerDueno()
                nombreEst=obtenerNombreEstacionamiento()
                direccionEst=obtenerDireccion()
                telefono=obtenerTelefonos()
                correo=obtenerCorreo()
                rif=obtenerRif()
                empresa = Estacionamiento(nombreDueno, nombreEst, direccionEst,
                                          telefono, correo, rif)
                print empresa
                ListaEstacionamientos.append(empresa)

        elif opcion == 2:
            if len(ListaEstacionamientos) >= 5:
                print("\nError, no se puede agregar un nuevo estacionamiento,"
                      + "porque se ha llegado al limite.\n")
            else:
                print("\n**AGREGAR ESTACIONAMIENTO PARAMETRIZADO**\n")
                
                nombreDueno = obtenerDueno()
                nombreEst=obtenerNombreEstacionamiento()
                direccionEst=obtenerDireccion()
                telefono=obtenerTelefonos()
                correo=obtenerCorreo()
                rif=obtenerRif()
                capacidad = obtenerCapacidad()
                horaApertura = obtenerHoraApertura()
                horaClausura = obtenerHoraClausura()
<<<<<<< HEAD
                tarifa = obtenerTarifa()
                horaAperturaReserva = obtenerHoraAperturaReserva()
                horaClausuraReserva = obtenerHoraClausuraReserva()
=======
                opcion1 = int(raw_input("Si desea agregar horario de reserva presione 1, de lo contrario 0 "))
                while opcion1 !=1 and opcion1 !=0:
                    opcion1 = int(raw_input("Opcion invalida, si desea agregar horario de reserva presione 1, de lo contrario 0 "))
                if opcion1 == 1:
                    tarifa = obtenerTarifa()
                    horaAperturaReserva = obtenerHoraAperturaReserva()
                    horaClausuraReserva = obtenerHoraClausuraReserva()
                else: 
                    tarifa ="NA"
                    horaAperturaReserva="NA"
                    horaClausuraReserva="NA"
>>>>>>> parametrizarEst

                empresa = EstacionamientoParametrizado(nombreDueno, nombreEst, direccionEst, telefono, correo, rif,
                										capacidad, horaApertura, horaClausura,tarifa,
                										horaAperturaReserva,horaClausuraReserva)

<<<<<<< HEAD
                print empresa
                ListaEstacionamientos.append(empresa)

        elif opcion == 3:
            imprimirEstacionamientos(ListaEstacionamientos)      
=======
             
                ListaEstacionamientos.append(empresa)
        
        elif opcion == 3:
            k=0
            while k < len(ListaEstacionamientos):
                nombre=ListaEstacionamientos[k].get_nombre()
                print (k+1)," ",nombre
                k+=1
            opcion1 = int(raw_input("Seleccione un estacionamiento"))
            print ListaEstacionamientos[opcion1-1]     
>>>>>>> parametrizarEst
        elif opcion < 0 or opcion > 3:
            print("Opcion incorrecta, introduzca la opcion nuevamente.\n")
    print("Gracias por usar el Sistema Automatizado de Gestion de Estacionamientos.")
    
menu(ListaEstacionamientos)

