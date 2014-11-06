'''
Created on Oct 29, 2014

@author: nelson
'''
from re import search, match
from Estacionamiento import Estacionamiento
from datetime import date

ListaEstacionamientos = []

def imprimiropcionionesMenu():
    print("\n---MENU PRINCIPAL---")
    print("Si desea agregar un nuevo estacionamiento marque uno (1).")
    print("Si desea ver los datos de TODOS estacionamiento marque dos (2)")
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
    
def validarHora(hora):
    print "VALIDAR"
    
def validarHorario(horaApertura,horaClausura):
    print "VALIDAR"
    
def validarTarifa(tarifa):
    print "VALIDAR"
    
        
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
            while opcion != 0 and opcion != 1:
                print("Opcion invalida, vuelva a intentar.")
                opcion = int(raw_input("Si desea agregar otro numero de telefono marque uno(1). "
                                    + "De lo contrario marque cero(0): "))
                
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
            while opcion != 0 and opcion != 1:
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
            imprimirEstacionamientos(ListaEstacionamientos)      
        elif opcion < 0 or opcion > 2:
            print("Opcion incorrecta, introduzca la opcion nuevamente.\n")
    print("Gracias por usar el Sistema Automatizado de Gestion de Estacionamientos.")
    
menu(ListaEstacionamientos)
