class nodo(object):                                     #Creando la clase nodo
    def __init__(self, nombre, matriz):
        self.nombre = nombre                            #Atributo de tipo nombre
        self.matriz = matriz                            #Atributo de tipo matriz
        self.siguienteNodo = None                       #Atributo de tipo objeto


class listaCircular(object):                            #Creando clase para la lista circular
    def __init__(self):                                 #En el constructor se inicia el puntero cabeza como nulo
        self.cabeza = None

    def verVacio(self):                                 #Ver si existen nodos en la lista
        return self.cabeza is None                      #retorna boolenao si el puntero cabeza es nulo


    def agregarFinalLista(self, nombre, matriz):              
        nodoCreado = nodo(nombre, matriz)               #Se crea un objeto de tipo nodo con el parametro enviado
        if self.verVacio():                             #Si es vacía la lista se inserta el nodo
            self.cabeza = nodoCreado                    #Al puntero cabeza se le asigna el nodo creado
            nodoCreado.siguienteNodo = self.cabeza      #El nodo creado apunta a cabeza, esto significa que el nodo creado apunta a si mismo
        else:                                           #En el caso de que existan ya nodos en la lista
            auxiliar = self.cabeza                      #Un nodo auxiliar tendra copia del nodo asignado a la cabeza
            while auxiliar.siguienteNodo != self.cabeza: #Mientras que el nodo auxiliar no vuelva a ser la cabeza recorrerá la lista
                auxiliar = auxiliar.siguienteNodo       #auxiliar recorre uno a uno los elementos hasta llegar al último elemento ya que se cumple la condición
            auxiliar.siguienteNodo = nodoCreado         #Ya que se tiene el último elemento se le indica que su siguiente nodo ya NO es cabeza sino el nuevo nodo creado
            nodoCreado.siguienteNodo = self.cabeza      #Ese nuevo nodo creado se le asigna el nodo cabeza para cerrar el circulo


    def recorrerLista(self):                            #Mostrar cada elemento de la lista
        if self.verVacio():
            return
        auxiliar = self.cabeza
        print(auxiliar.nombre)
        print(auxiliar.matriz)
        while auxiliar.siguienteNodo != self.cabeza:
            auxiliar = auxiliar.siguienteNodo
            print(auxiliar.nombre)
            print(auxiliar.matriz)
    
    
    def tamanoLista(self):
        auxiliar = self.cabeza
        conteo = 0
        while auxiliar is not None:
            conteo += 1
            if auxiliar.siguienteNodo == self.cabeza:
                break
            else:
                auxiliar = auxiliar.siguienteNodo
        return conteo

'''
nuevaLista = listaCircular()
nuevaLista.agregarFinalLista("lista1", [1,2,3,4,5])
nuevaLista.agregarFinalLista("lista2", [2,2,2,2,2,2,2])
nuevaLista.agregarFinalLista("lista3", [3,3,3])
print("El tamaño de la lista es ", nuevaLista.tamanoLista())
nuevaLista.recorrerLista()'''
