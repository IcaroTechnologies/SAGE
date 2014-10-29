'''
Created on Oct 29, 2014

@author: nelson
'''
from Estacionamiento import Estacionamiento

ListaEstacionamientos = []


def menu():
    opc = 1
    
    print("Bienvenido al Sistema Automatizado de Gestion de Estacionamientos.")
    print()
    
    while opc != 0:
        
        print()
        print("Si desea agregar un nuevo estacionamiento marque uno (1).")
        print("Si desea ver los datos de TODOS estacionamiento marque dos (2)")
        print("Para salir del sistema presione cero (0)")
        
        opc = int(input("Introduzca el numero de su opcion: "))
        
        if opc == 1:
            if len(ListaEstacionamientos) >= 5:
                print("Error, no se puede agregar un nuevo estacionamiento,"
                      + "porque se ha llegado al limite.")
            else:
                nombreDueno = input("Introduzca el nombre del dueno del estacionamiento: ")
                nombreEst = input("Indique el nombre del estacionamineto: ")
                direccionEst = input("Indique la direccion del estacionamiento: ")
                i = 0
                opc2 = 1
                telefono = []
                while opc2 == 1 and i < 3:
                    entrada = input("Introduzca un n. de telefono (movil o local de caracas): ")
                    if not(entrada in telefono):    
                        telefono.append(entrada)
                        i = i + 1
                    else:
                        print("Numero de telefono ya existente.")
                    if i < 3:
                        opc2 = int(input("Si desea agregar otro numero de telefono marque uno(1). "
                                     + "De lo contrario marque cero (0): "))
                    
                correo = []
                opc2 = 1
                correo.append(input("Intoduzca un correo electronico (Ej. sage@hotmail.com): "))
                opc2 = int(input("Si desea agregar otra direccion de correo electronico marque uno(1). "
                                + "De lo contrario marque cero(0)"))
                if opc2 == 1:
                    entrada = input("Intoduzca un correo electronico (Ej. sage@hotmail.com): ")
                    if not(entrada in correo):
                        correo.append(entrada)
                    else:
                        print("Correo ya existente.")
                           
                rif = input("Introduzca el rif de la empresa: ")
                try:    
                    empresa = Estacionamiento(nombreDueno, nombreEst, direccionEst,
                                              telefono, correo, rif)
                    ListaEstacionamientos.append(empresa)
                except Exception:
                    print("Introdujo uno o varios datos incorrectos.\n")
                    
        elif opc == 2:
            if len(ListaEstacionamientos) == 0:
                print("No se ha registrado ningun estacionamiento.")
            else:
                print("Estacionamientos Registrados: \n\n")
                for i in ListaEstacionamientos:
                    print(i,"\n")
        elif opc < 0 or opc > 2:
            print("Numero de opcion incorrecto, vuelva a intentarlo.\n")
                
    
    print("Gracias por usar el Sistema Automatizado de Gestion de Estacionamientos.")
    
menu()

