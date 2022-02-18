import os
os.system("cls")
class principal:
    def __init__(self):
        pass
    def menu(self,opciones):
        print("*"*8,"Menú","*"*8)
        for opcion in opciones: 
            print(opcion)
        opc = input("Elija opcion[1...{}] : " .format(len(opciones)))
        return opc 