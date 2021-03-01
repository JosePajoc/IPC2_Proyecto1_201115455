import xml.etree.ElementTree as ET      #importando libreria

class archivoXML():                     #Creando clase para el archivo XML
    matrizDatos = []                    #Matriz de elementos
    documentoXML = None                 #Variable para el archivo XML
    matricesRaiz = None

    def __init__(self, ruta):           #En el constructor se pide ruta
        global documentoXML
        global matricesRaiz
        try:
            documentoXML = ET.parse(ruta)
            matricesRaiz = documentoXML.getroot()
            print(matricesRaiz)
            print("Carga éxitosa...")
        except:
            print("Error al cargar archivo...")


    def ProcesarArchivo(self):      #Obtener atributos de cada matriz
        global documentoXML
        global matricesRaiz
        for matriz in matricesRaiz:
            print('Nombre de la matriz', matriz.attrib.get('nombre'))       #nombre matriz
            print('Las filas son: ', matriz.attrib.get('n'), ' las columnas son ', matriz.attrib.get('m'))
            for dato in matriz:
                print(dato.text)
        
                
            

