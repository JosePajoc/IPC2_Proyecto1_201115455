from xml.dom import minidom     #Importando módulo para lectura XML

class archivoXML():             #Creando clase para el archivo XML
    matrizDatos = []                 #Matriz de elementos
    documentoXML = None         #Variable para el archivo XML

    def __init__(self, ruta):   #En el constructor se pide ruta
        global documentoXML
        try:
            documentoXML = minidom.parse(ruta)  #Realizando parseo para poder ser legible
            print("Carga éxitosa...")
        except:
            print("Error al cargar archivo...")
    
    def verDatos(self):             #------------> función de prueba
        global documentoXML
        print(documentoXML)

    def ProcesarArchivo(self):      #Obtener atributos de cada matriz
        global documentoXML
        etiquetaMatrices = documentoXML.getElementsByTagName("matrices")    #obtner todo lo que posee la etiqueta "matrices"
        for matrices in etiquetaMatrices:
            etiquetaMatriz = documentoXML.getElementsByTagName("matriz")    #Obtener todo lo que posee la etiqueta "matriz"
            for matriz in etiquetaMatriz:
                nombre = matriz.getAttribute("nombre")
                nFila = matriz.getAttribute("n")
                mColumna = matriz.getAttribute("m")
                print("nombre: ", nombre, " filas: ", nFila, "columnas: ", mColumna)
                xFila = 0
                yColumna = 0
                for valor in range( int(mColumna) * int(nFila) ):
                    print("Dato: ", matriz.getElementsByTagName("dato")[valor].firstChild.data)
                
            

