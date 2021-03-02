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
            print(matricesRaiz)
            print("Carga éxitosa...")
        except:
            print("Error al cargar archivo...")


    def ProcesarArchivo(self):                                      #Obtener atributos de cada matriz
        global documentoXML
        global matricesRaiz
        sublista = []                                               #Lista para extraer cada dato
        indice = 0
        for matriz in matricesRaiz:
            print('Nombre de la matriz: ', matriz.attrib.get('nombre'))       #nombre matriz
            fil = int(matriz.attrib.get('n'))
            col = int(matriz.attrib.get('m'))
            print('Las filas son: ', fil, ' las columnas son ', col)
            dimensiones = (fil, col)
            matrizVacia = np.zeros(dimensiones)
            for dato in matriz:
                print(dato.text)                                    #-----------> QUITAR
                sublista.append(int(dato.text))
            for i in range(fil):
                for j in range(col):
                    matrizVacia[i][j] = sublista[indice]
                    indice = indice + 1
                             
            print(matrizVacia)
            

            

