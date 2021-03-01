class nodo(object):                                 #Creando la clase nodo
    def __init__(self, dato):
        self.dato = dato                            #Atributo de tipo dato
        self.siguienteNodo = None                   #Atributo de tipo objeto

class listaCircular(object):                        #Creando clase para la lista circular
    def __init__(self):                             #En el constructor se inicia el puntero cabeza como nulo
        self.cabeza = None

    def verVacio(self):                             #Ver si existen nodos en la lista
        return self.cabeza is None                  #retorna boolenao si el puntero cabeza es nulo


    def agregarFinalLista(self, dato):              
        nodoCreado = nodo(dato)                     #Se crea un objeto de tipo nodo con el parametro enviado
        if self.verVacio():                         #Si es vacía la lista se inserta el nodo
            self.cabeza = nodoCreado                #Al puntero cabeza se le asigna el nodo creado
            nodoCreado.siguienteNodo = self.cabeza  #El nodo creado apunta a cabeza, esto significa que el nodo creado apunta a si mismo
        else:                                   #En el caso de que existan ya nodos en la lista
            auxiliar = self.cabeza                  #Un nodo auxiliar tendra copia del nodo asignado a la cabeza
            while auxiliar.siguienteNodo != self.cabeza: #Mientras que el nodo auxiliar no vuelva a ser la cabeza recorrerá la lista
                auxiliar = auxiliar.siguienteNodo   #auxiliar recorre uno a uno los elementos hasta llegar al último elemento ya que se cumple la condición
            auxiliar.siguienteNodo = nodoCreado     #Ya que se tiene el último elemento se le indica que su siguiente nodo ya NO es cabeza sino el nuevo nodo creado
            nodoCreado.siguienteNodo = self.cabeza  #Ese nuevo nodo creado se le asigna el nodo cabeza para cerrar el circulo


    def eliminarNodo(self, dato):
        if self.verVacio():              #Verificando que no este vacía la lista
            return
        elif dato == self.cabeza.dato:  #Si el dato a borrar coincide con el dato del nodo cabeza, entonces
            auxiliar = self.cabeza      #un nodo auxiliar hara una copia del nodo cabeza
            while auxiliar.siguienteNodo != self.cabeza:    #Mientras que el nodo auxiliar no vuelva a ser la cabeza recorrerá la lista
                auxiliar = auxiliar.siguienteNodo       #auxiliar recorre uno a uno los elementos hasta llegar al último elemento ya que se cumple la condición
            auxiliar.siguienteNodo = self.cabeza.siguienteNodo  #Ya que se tiene el último elemento sele indica que su siguiente nodo sera el siguiente nodo de la cabeza, de esa forma se omite el nodo inicial de la cabeza, cerrando de nuevo el circulo
            self.cabeza = self.cabeza.siguienteNodo     #El nodo cabeza se integra de nuevo indicando que el nodo que era el segundo pasa a ser el primero
        else:
            auxiliar = self.cabeza  #En caso de que el dato no este en el nodo cabeza, se crea un nodo auxiliar para copiar a la cabeza y así recorrer la lista
            predecesor = None       #Se crea un nodo predecesor con valor nulo
            while auxiliar.dato != dato:    #mientras que no vuelvan a coincidir se recorre la lista
                predecesor = auxiliar       #Se asigna el predecesor al auxiliar para ir una posición atrás
                auxiliar = auxiliar.siguienteNodo   #El auxiliar toma el valor de su siguiente apuntador, se recorre la lista de dos en dos
            predecesor.siguienteNodo = auxiliar.siguienteNodo #Al salir del ciclo el predecesor toma el apuntador del auxiliar de esta forma se obtine el nodo siguiente y se deja de hacer referencia a auxiliar, en otras palabras predecesor se salta al nodo que tiene el dato

    def recorrerLista(self):
        if self.verVacio():
            return
        auxiliar = self.cabeza
        print(auxiliar.dato)
        while auxiliar.siguienteNodo != self.cabeza:
            auxiliar = auxiliar.siguienteNodo
            print(auxiliar.dato)
    
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
nuevaLista.agregarFinalLista(33)
nuevaLista.agregarFinalLista(5)
nuevaLista.agregarFinalLista(50)
nuevaLista.recorrerLista()
print("El tamaño de la lista es ", nuevaLista.tamanoLista())
nuevaLista.eliminarNodo(33)
nuevaLista.recorrerLista()
print("El tamaño de la lista es ", nuevaLista.tamanoLista())
'''