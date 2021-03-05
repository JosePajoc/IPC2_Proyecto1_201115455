from io import open                                     #Importando libreria para crear archivo plano

class nodo(object):                                     #Creando la clase nodo
    def __init__(self, nombre, matriz, filasUnicas):
        self.nombre = nombre                            #Atributo de tipo nombre
        self.matriz = matriz                            #Atributo de tipo matriz
        self.filasUnicas = filasUnicas                  #Atributo de tipo vector
        self.siguienteNodo = None                       #Atributo de tipo objeto


class listaCircular(object):                            #Creando clase para la lista circular
    def __init__(self):                                 #En el constructor se inicia el puntero cabeza como nulo
        self.cabeza = None

    def verVacio(self):                                 #Ver si existen nodos en la lista
        return self.cabeza is None                      #retorna boolenao si el puntero cabeza es nulo

    def agregarFinalLista(self, nombre, matriz, filasUnicas):              
        nodoCreado = nodo(nombre, matriz, filasUnicas)      #Se crea un objeto de tipo nodo con el parametro enviado
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
        print('Filas que se repetian en frecuencia')
        print(auxiliar.filasUnicas)
        while auxiliar.siguienteNodo != self.cabeza:
            auxiliar = auxiliar.siguienteNodo
            print(auxiliar.nombre)
            print(auxiliar.matriz)
            print('Filas que se repetian en frecuencia')
            print(auxiliar.filasUnicas)   
    
    def tamanoLista(self):                              #Ver cantidad de nodos en la lista circular
        auxiliar = self.cabeza
        conteo = 0
        while auxiliar is not None:
            conteo += 1
            if auxiliar.siguienteNodo == self.cabeza:
                break
            else:
                auxiliar = auxiliar.siguienteNodo
        return conteo

    def crearXML(self, ruta):
        salidaXML = open(ruta,'w')
        if self.verVacio():                             #Verificar que la lista no este vacía
            return
        auxiliar = self.cabeza
        
        n = len(auxiliar.matriz)                        #Obteniendo datos de las matrices
        m = len(auxiliar.matriz[0])
        g = len(auxiliar.filasUnicas)
        #Encabezado del archivo plano
        salidaXML.write('<matriz nombre="' + auxiliar.nombre + '" n="' + str(n) + '" m="' + str(m) + '" g="' + str(g) + '">\n')
        #Datos
        for x in range(n):                              #Concatenando datos de la matriz con cadenas de texto
            for y in range(m):
                salidaXML.write('<dato x="' + str(x+1) + '" y="' + str(y+1) + '">' + str(auxiliar.matriz[x][y]) + '</dato>\n')
        #Frecuencias
        for g in range(len(auxiliar.filasUnicas)):
            if len(auxiliar.filasUnicas[g]) == 1:
                salidaXML.write('<frecuencia g="' + str(g+1) + '">' + str(len(auxiliar.filasUnicas[g])) + '</frecuencia>\n')
            else:
                tamano = auxiliar.filasUnicas[g].split(',')
                salidaXML.write('<frecuencia g="' + str(g+1) + '">' + str(len(tamano)) + '</frecuencia>\n')
        #Fin matriz
        salidaXML.write('</matriz>\n')
        
        while auxiliar.siguienteNodo != self.cabeza:
            auxiliar = auxiliar.siguienteNodo
            
            n = len(auxiliar.matriz)
            m = len(auxiliar.matriz[0])
            g = len(auxiliar.filasUnicas)
            #Encabezado
            salidaXML.write('<matriz nombre="' + auxiliar.nombre + '" n="' + str(n) + '" m="' + str(m) + '" g="' + str(g) + '">\n')
            #Datos
            for x in range(n):
                for y in range(m):
                    salidaXML.write('<dato x="' + str(x+1) + '" y="' + str(y+1) + '">' + str(auxiliar.matriz[x][y]) + '</dato>\n')
            #Frecuencia
            for g in range(len(auxiliar.filasUnicas)):
                if len(auxiliar.filasUnicas[g]) == 1:
                    salidaXML.write('<frecuencia g="' + str(g+1) + '">' + str(len(auxiliar.filasUnicas[g])) + '</frecuencia>\n')
                else:
                    tamano = auxiliar.filasUnicas[g].split(',')
                    salidaXML.write('<frecuencia g="' + str(g+1) + '">' + str(len(tamano)) + '</frecuencia>\n')
            #Fin matriz
            salidaXML.write('</matriz>\n')

        salidaXML.close()                               #Cierre del flujo para el archivo plano
    
    def crearGrafo(self):
        print('Creando el grafo...')
