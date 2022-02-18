import time
class back:                
    def __init__(self,tamanio):
        self.lista=[]
        self.tope=0
        self.size=tamanio
     
    def empty(self):
        return self.tope == 0
    
    def push(self,dato):
        if self.tope < self.size:
            self.lista += [dato]
            print (f'La lista es :{self.lista}\n')
            self.tope += 1
        else:
            print("La Pila está Llena")
   
    def pop(self):
        if self.empty():
            print ("Lista Vacia")
        else:
            top = self.lista[0]
            self.tope -= 1
            self.lista = self.lista[1:]
            print("El elemento eliminador es:{}".format(top))
            print("La lista queda:{}".format(self.lista))
            
    def longitud(self):
        print(self.tope)
        
    def show(self):
        if self.empty():
            print("Lista vacia")
        else:                    
            for tope in range(0,self.tope):
                print("[{}]".format(self.lista[tope]))    
    
    def buscar(self,buscado):
        try:
            if buscado in self.lista:
                print('El elemento se encuentra: {}'.format(self.lista.index(buscado)))
                time.sleep(1)
                return True
        except ValueError:
            return False