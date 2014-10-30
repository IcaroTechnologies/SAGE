'''
Created on Oct 29, 2014

@author: nelson
'''
from Estacionamiento import Estacionamiento

ListaEstacionamientos = []

def imprimiropcionionesMenu():
    print("\n---MENU PRINCIPAL---")
    print("Si desea agregar un nuevo estacionamiento marque uno (1).")
    print("Si desea ver los datos de TODOS estacionamiento marque dos (2)")
    print("Para salir del sistema presione cero (0)\n")

def obtenerTelefonos():
    
    i = 0
    opcion = 1
    telefono = []
    
    while opcion == 1 and i < 3:
        entrada = input("Introduzca un n. de telefono (movil o local de caracas): ")
        if not(entrada in telefono):    
            telefono.append(entrada)
            i = i + 1
        else:
            print("\nNumero de telefono ya existente. Por favor introduzca un nuevo numero.")
        if i < 3:
            opcion = int(input("Si desea agregar otro numero de telefono marque uno(1). "
                               + "De lo contrario marque cero (0): "))
            while opcion != 0 and opcion != 1:
                print("Opcion invalida, vuelva a intentar.")
                opcion = int(input("Si desea agregar otro numero de telefono marque uno(1). "
                                   + "De lo contrario marque cero(0): "))
            
    return telefono

def obtenerCorreo():
    
    correo = []
    opcion = 1
    i = 0
    
    while opcion == 1 and i < 2:
        entrada = input("Intoduzca un correo electronico (Ej. sage@hotmail.com): ")
        if not(entrada in correo):    
            correo.append(entrada)
            i = i + 1
        else:
            print("\nCorreo ya existente. Por favor introduzca una nueva direccion.")
        if i < 2:
            opcion = int(input("Si desea agregar otra direccion de correo electronico marque uno(1). "
                               + "De lo contrario marque cero(0): "))
            while opcion != 0 and opcion != 1:
                print("Opcion invalida, vuelva a intentar.")
                opcion = int(input("Si desea agregar otra direccion de correo electronico marque uno(1). "
                                   + "De lo contrario marque cero(0): "))
    return correo
            
def imprimirEstacionamientos(ListaEstacionamientos):
    
    if len(ListaEstacionamientos) == 0:
        print("\nNo se ha registrado ningun estacionamiento.\n")
    else:
        print("\n**ESTACIONAMIENTOS REGISTRADOS**\n\n")
        for i in ListaEstacionamientos:
            print(i,"\n")
    
def menu(ListaEstacionamientos):
    opcion = 1
    
    print("\nBienvenido al Sistema Automatizado de Gestion de Estacionamientos.\n") 
    while opcion != 0:
        
        imprimiropcionionesMenu()
        opcion = int(input("Introduzca el numero de su opcion: "))
        if opcion == 1:
            if len(ListaEstacionamientos) >= 5:
                print("\nError, no se puede agregar un nuevo estacionamiento,"
                      + "porque se ha llegado al limite.\n")
            else:
                print("\n**AGREGAR ESTACIONAMIENTO**\n")
                nombreDueno = input("Introduzca el nombre del dueno del estacionamiento: ")
                nombreEst = input("Indique el nombre del estacionamineto: ")             
                direccionEst = input("Indique la direccion del estacionamiento: ")             
                telefono = obtenerTelefonos() 
                correo = obtenerCorreo()       
                rif = input("Introduzca el rif de la empresa: ")
                try:    
                    empresa = Estacionamiento(nombreDueno, nombreEst, direccionEst,
                                              telefono, correo, rif)
                    ListaEstacionamientos.append(empresa)
                except Exception:
                    print("Introdujo uno o varios datos incorrectos.\n")
                    
        elif opcion == 2:
            imprimirEstacionamientos(ListaEstacionamientos)      
        elif opcion < 0 or opcion > 2:
            print("Opcion incorrecta, introduzca la opcion nuevamente.\n")
    print("Gracias por usar el Sistema Automatizado de Gestion de Estacionamientos.")
    
menu(ListaEstacionamientos)
