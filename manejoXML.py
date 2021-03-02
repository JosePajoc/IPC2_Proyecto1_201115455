import xml.etree.ElementTree as ET                                  #importando libreria
import numpy as np                                                  #Instalar en la terminal con pip install numpy

class archivoXML():                                                 #Creando clase para el archivo XML
    documentoXML = None                                             #Variable para el archivo XML
    matricesRaiz = None                                             #Variable para la etiqueta matrices

    def __init__(self, ruta):                                       #En el constructor se pide ruta
        global documentoXML
        global matricesRaiz
        try:
            documentoXML = ET.parse(ruta)                           #Conviritendo a legible
            matricesRaiz = documentoXML.getroot()                   #Obteniendo la raíz
            print(matricesRaiz)                                     #-----------> QUITAR
            print("Carga éxitosa...")
        except:
            print("Error al cargar archivo...")


    def ProcesarArchivo(self):                                      #Obtener atributos de cada matriz
        global documentoXML
        global matricesRaiz
        sublista = []                                               #Lista para extraer cada dato
        indice = 0                                                  #índice para recorrer sublista
        for matriz in matricesRaiz:                                 #Recorriendo etiqueta "matriz"
            print('Nombre de la matriz: ', matriz.attrib.get('nombre'))       #nombre matriz
            fil = int(matriz.attrib.get('n'))
            col = int(matriz.attrib.get('m'))
            print('Las filas son: ', fil, ' las columnas son ', col)
            dimensiones = (fil, col)
            matrizEntrada = np.zeros(dimensiones)
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
            
            print('Matriz de entrada')                 
            print(matrizEntrada)
            print('Matriz de frecuencia')
            print(matrizPatrones)
            filasRepetidas = []                                     #lista para filas repetidas
            texto = ''                                              
            for i in range(fil):                                    #Encontrando filas repetidas
                for j in range(fil):
                    if (matrizPatrones[i] == matrizPatrones[j]).all():  #comparando fila por fila con valores booleanos de numpy
                        texto = texto + str(j) +  ','
                filasRepetidas.append(texto[:len(texto)-1])         #Agregando a la lista de filas repetidas sin la , extra usando slice
                texto = ''
            print(filasRepetidas)
            filasUnicas = []                                        #Listas para filas únicas
            for elemento in filasRepetidas:
                if elemento not in filasUnicas:                     #Si no existe el dato se agrega
                    filasUnicas.append(elemento)
            print(filasUnicas)
            print('---------------------->')



