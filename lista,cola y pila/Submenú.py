import time
from listas import *
from Menú import principal
from pilas import *
from cola import *
import os

os.system("cls")
var = principal()
orden = ["1)Lista","2)Pila","3)Cola","4)Salir"]
opcion = ""
while opcion != "4":
    os.system("cls")
    opcion = var.menu(orden)
    if opcion == '1':
        opc1=""
        lista = Lista()
        while opc1 != "8":
            os.system("cls")
            opc1 = var.menu(["1)Push","2)Pop","3)Show","4)Eliminar elemento","5)Insertar elemento","6)Buscar","7)Salir"])
            os.system("cls")
            if opc1 == "1":
                valor = input("Ingrese numeros a la lista :")
                lista.agregar(valor)
                time.sleep(1)
            elif opc1 == "2":
                    lista.eliminar()
                    time.sleep(1)
            elif opc1 == "3":
                    lista.mostrar()
                    time.sleep(1)
            elif opc1 == "4":
                    while True:
                        indice = int(input("Ingrese una posicion para eliminar: "))
                        os.system("cls")
                        m = lista.eleminarElemento(indice)
                        if m == True:
                            break
                        else:
                            print("No se encuentra")
                            time.sleep(2)
                            os.system("cls")
            elif opc1 == "5":
                    pos = int(input("ingrese una posición: "))
                    dato = input("ingrese un dato: ")
                    lista.InsertarElemento(pos,dato)
                    time.sleep(1)
            elif opc1 == "6": 
                    while True:
                            dato = input("ingrese el número que se encunetre en la lista para conocer su posición: ")
                            os.system("cls")
                            a = lista.buscar(dato)
                            if a == True:
                                break
                            else:
                                print("No se encuentra")
                                time.sleep(1)
                                os.system("cls")
            elif opc1 == "7":
                    print("Salir del menú")
                    time.sleep(1)
                
    
    if opcion == "2":
        opc1=""
        rp = int(input("Ingresar un numero para el tamaño: "))
        pila = Stack(rp)
        while opc1 != "6":
            os.system("cls")
            opc1 = var.menu(["1)Push","2)Pop","3)Show","4)Buscar","5)Longitud","6)Salir"])
            os.system("cls")
            if opc1 == "1":
                dato= input("Ingrese un numero:")
                pila.push(dato)
                time.sleep(1)
            elif opc1 == "2":
                print(pila.pop())
                time.sleep(1)
            elif opc1 == "3":
                pila.show()
                time.sleep(1)
            elif opc1 == "4":
                    while True:
                            buscado = input("ingrese un número que este dentro de la lista para conocer su posición: ")
                            os.system("cls")
                            b = pila.buscar(buscado)
                            if b == True:
                                break
                            else:
                                print("No se encuentra")
                                time.sleep(1)
                                os.system("cls")
            elif opc1 == "5":
                pila.longitud()
                time.sleep(1)
            elif opc1 == "6":
                print("Salir del pila")
                time.sleep(1)


    if opcion == "3":
        opc1=""
        ro = int(input("Ingresar un numero para el tamaño: "))
        cola = back(ro)
        while opc1 != "6":
            os.system("cls")
            opc1 = var.menu(["1)Push","2)Pop","3)Show","4)Buscar","5)Longitud","6)Salir"])
            os.system("cls")
            if opc1 == "1":
                dato= input("Ingrese un numero:")
                cola.push(dato)
                time.sleep(1)
            elif opc1 == "2":
                print(cola.pop())
                time.sleep(1)
            elif opc1 == "3":
                cola.show()
                time.sleep(1)
            elif opc1 == "4":
                    while True:
                            buscado = input("ingrese un número que este dentro de la lista para conocer su posición: ")
                            os.system("cls")
                            b = cola.buscar(buscado)
                            if b == True:
                                break
                            else:
                                print("No se encuentra")
                                time.sleep(1)
                                os.system("cls")
            elif opc1 == "5":
                cola.longitud()
                time.sleep(1)
            elif opc1 == "6":
                print("Salir de la cola")
                time.sleep(1)

    if opcion == "4":
        os.system("cls")
print("Gracias por visitarno")

            