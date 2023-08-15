import os

# Variables para loguearse
usuario = "admin"
password = "1234"

diccionarioDatos = dict()
listaDatos = []

# Login
def login():
    print("########## LOGIN ##########")
    ingresarUsuario = input("Ingrese su usuario: ")
    ingresarPassword = input("Ingrese su password: ")

    if ingresarUsuario == usuario and ingresarPassword == password:
        print("\nBienvenido al sistema!\n")
        menuPrincipal()
    else:
        print("\nUsuario o password incorrecto\n")
        login()

def menuPrincipal():
    print("########## MENU PRINCIPAL ##########")
    print("1. Cargar archivo .inv")
    print("2. Cargar archivo .mov")
    print("3. Salir")

    while True:
        opcion = input("\nIngrese una opcion: ")
        if opcion.isdigit():
            opcion = int(opcion)
            if opcion == 1:
                cargarArchivoInv()
            elif opcion == 2:
                cargarArchivoMov()
            elif opcion == 3:
                print("\nGracias por utilizar el sistema!\n")
                exit()
            else:
                print("\nOpcion incorrecta\n")
        else:
            print("\nOpcion incorrecta\n")

def cargarArchivoInv():
    print("\nHa seleccionado cargar archivo .inv\n")
    ruta = input("Ingrese la ruta del archivo: ")

    while True:
        nombre, extension = os.path.splitext(ruta)
        if extension == ".inv":
            print("\nArchivo valido\n")
            break
        else:
            print("\nArchivo invalido\n")
            ruta = input("\nIngrese la ruta del archivo: ")

    with open(ruta, "r") as archivo:
            for linea in archivo:
                array = linea.split(',')
                for i in range(len(array)):
                    listaDatos.append(array[i])
        
    print(listaDatos)

def cargarArchivoMov():
    print("\nHa seleccionado cargar archivo .mov\n")
    ruta = input("Ingrese la ruta del archivo: ")

    while True:
        nombre, extension = os.path.splitext(ruta)
        if extension == ".mov":
            print("\nArchivo valido\n")
            break
        else:
            print("\nArchivo invalido\n")
            ruta = input("\nIngrese la ruta del archivo: ")

    with open(ruta, "r") as archivo:
            for linea in archivo:
                array = linea.split(',')
                for i in range(len(array)):
                    diccionarioDatos[i + 1] = array[i]
        
    print(diccionarioDatos)

login()