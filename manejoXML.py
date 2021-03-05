import xml.etree.ElementTree as ET                                  #importando libreria
import numpy as np                                                  #Instalar en la terminal con pip install numpy
from claseListaCircular import listaCircular                        #importando la clase lista circular enlazada

class archivoXML():                                                 #Creando clase para el archivo XML
    documentoXML = None                                             #Variable para el archivo XML
    matricesRaiz = None                                             #Variable para la etiqueta matrices

    def __init__(self, ruta):                                       #En el constructor se pide ruta
        #Variables globales
        global documentoXML
        global matricesRaiz
        global nuevaLista
        try:
            documentoXML = ET.parse(ruta)                           #Conviritendo a legible
            matricesRaiz = documentoXML.getroot()                   #Obteniendo la raíz
            print("\nCarga éxitosa...")
        except:
            print("\nError al cargar archivo...")

    def ProcesarArchivo(self):                                      #Obtener atributos de cada matriz
        global documentoXML
        global matricesRaiz
        global nuevaLista
        nuevaLista = listaCircular()                                #Creando lista circular
        sublista = []                                               #Lista para extraer cada dato
        indice = 0                                                  #índice para recorrer sublista
        for matriz in matricesRaiz:                                 #Recorriendo etiqueta "matriz"
            print('_________________________________________________________________')
            print('Nombre de la matriz: ', matriz.attrib.get('nombre'))       #nombre matriz
            fil = int(matriz.attrib.get('n'))
            col = int(matriz.attrib.get('m'))
            print('Las filas son: ', fil, ' las columnas son ', col)
            dimensiones = (fil, col)
            matrizEntrada = np.zeros(dimensiones)                   #Matrices creadas con dimensiones
            matrizPatrones = np.zeros(dimensiones)
            for dato in matriz:
                #print(dato.text)                                    #-----------> QUITAR
                sublista.append(int(dato.text))                     #Lista para extraer cada dato de la matriz xml
            for i in range(fil):                                    #Recorrer la matriz para asignar los datos de la lista
                for j in range(col):
                    matrizEntrada[i][j] = sublista[indice]
                    if sublista[indice]==0:                         #Creando matriz de patrones
                        matrizPatrones[i][j] = 0
                    else:
                        matrizPatrones[i][j] = 1
                    indice = indice + 1
            
            print('\nMatriz de entrada')                 
            print(matrizEntrada)
            print('\nMatriz de frecuencia')
            print(matrizPatrones)
            filasRepetidas = []                                     #lista para filas repetidas
            texto = ''                                              
            for i in range(fil):                                    #Encontrando filas repetidas
                for j in range(fil):
                    if (matrizPatrones[i] == matrizPatrones[j]).all():  #comparando fila por fila con valores booleanos de numpy
                        texto = texto + str(j) +  ','
                filasRepetidas.append(texto[:len(texto)-1])         #Agregando a la lista de filas repetidas sin la , extra usando slice
                texto = ''
            #print(filasRepetidas)                                   #-----------> QUITAR
            print('---------------------->')
            filasUnicas = []                                        #Listas para filas únicas
            for elemento in filasRepetidas:
                if elemento not in filasUnicas:                     #Si no existe el dato se agrega
                    filasUnicas.append(elemento)
            print('A continuación, se muestran agrupadas las filas que se repiten en frecuencia como también las filas únicas')
            print(filasUnicas)
            print('---------------------->')
            #Proceso de suma para las filas repetidas
            filasNuevas = len(filasUnicas)                          #Número de filas para dar nuevas dimensiones a la matriz reducida
            dimensiones = (filasNuevas, col)
            matrizReducida = np.zeros(dimensiones)                  #Creando matriz reducida con dimensiones necesarias
            indice = 0                                              #Índoce para las filas de la matriz reducida
            for unicas in filasUnicas:                              #Recorriendo lista de filas únicas
                if len(unicas)==1:                                  #si solo hay una fila única se agrega a la matriz reducida
                    matrizReducida[indice] = matrizEntrada[int(unicas)]
                else:
                    separadorFilas = unicas.split(',')              #extrayendo filas que se repiten
                    for ele in separadorFilas:                      #usando filas repetidas para suma 
                        for j in range(col):                        #Recorrer columnas
                            matrizReducida[indice][j] = matrizReducida[indice][j] + matrizEntrada[int(ele)][j]
                indice = indice + 1
            print('\nLa matriz reducida es: ')
            print(matrizReducida)

            #Para crear nodo se necesita los parametros:  nuevaLista(nombre de la matriz, matriz reducida, vector de filas únicas) 
            nuevaLista.agregarFinalLista(matriz.attrib.get('nombre'), matrizReducida, filasUnicas) #Creando nodo y agregando a la lista circular simple
        print('------------------------------------------>')
        print("\nEl número de matrices en la lista circular es ", nuevaLista.tamanoLista())
        print('------------------------------------------>')
    
    def escribirXML(self):
        ruta = input("\nIngrese la ruta donde desea crear el archivo XML, no olvide colocar al final de la ruta el nombre y extensión")
        print('_________________________________________________________________')
        print("\nCreando archivo XML...")
        print('_________________________________________________________________')
        #print('\nIngrese la ruta')
        nuevaLista.crearXML(ruta)
        print('Los datos exportados al archivo XML son')
        nuevaLista.recorrerLista()                                  #Ver datos de la lista circular simple  
        print('_________________________________________________________________')                

    def generarGrafica(self):
        print('El gráfico se creará en la carpeta raíz del proyecto')
        nuevaLista.crearGrafo()


