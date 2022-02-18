import time
class Lista:
    def __init__(self,datos=[]):
       self.datos = []

        
    def agregar(self,dato):
        self.datos.append(dato)
        print(f'Se agrego un nuevo elemento a la lista: {self.datos}\n')
        
    def eliminar(self):
        print("Se enlimino el número:{}".format(self.datos.pop()))
        print(f'Se elimino un numero de la lista: {self.datos}\n')
     
    def eleminarElemento(self,indice):
        try:
            if indice <= len(self.datos):
                self.datos.pop(indice)
                print('Lista actualizada con el elemento eliminado: {}'.format(self.datos))
                return True

        except ValueError:
            return False

    def InsertarElemento(self,pos,dato):
        self.datos.insert(pos,dato)
        print(f'Se agrego un dato a la lista : {self.datos}\n')

    def buscar(self,dato):
        try:
            if dato in self.datos:
                print('El elemento se encuentra: {}'.format(self.datos.index(dato)))
                time.sleep(1)
                return True
        except ValueError:
            return False
        
    def mostrar(self):
         print(f'Aqui se muestra como esta actualmente la lista: {self.datos}\n')





