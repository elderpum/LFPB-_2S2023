# Librería: pyinstaller

# Comando para crear el ejecutable:
# pyinstaller main.py

# Para crear el ejecutable:
salir = False
while (not salir):
    respuesta = input("¿Desea cerrar esta ventana? (s/n): ")
    if (respuesta == "s"):
        salir = True
        print ("Cerrando ventana...")