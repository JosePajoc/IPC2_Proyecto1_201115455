from manejoXML import archivoXML
import time
opcion = 0
carga = False
proceso = False

def separador():
    print("---------------------------------------------------------------")

while opcion!=6:
    try:
        separador()
        print("Menú principal")
        print("\t1. Cargar archivo")
        print("\t2. Procesar archivo")
        print("\t3. Escribir archivo salida")
        print("\t4. Mostrar datos del estudiante")
        print("\t5. Generar gráfica")
        print("\t6. Salida")
        opcion = int(input("\nIngrese el número de opción: "))
        if opcion == 1:
            separador()
            ruta = input("Ingrese la ruta del archivo XML: ")
            infoXML = archivoXML(ruta)                                  #Creación de objeto tipo archivoXML
            carga = True
        elif opcion == 2 and carga:
            separador()
            print("Procesando archivo XML")
            infoXML.ProcesarArchivo()
            proceso = True
        elif opcion == 3 and carga and proceso:
            infoXML.escribirXML()
        elif opcion == 4:
            separador()
            print("José Ernesto Pajoc Raymundo")
            print("201115455")
            print('Introducción a la programación y computación 2, sección "A"')
            print("Ingenieria en Ciencias y Sistemas")
            print("4to. Semestre")
            time.sleep(4)
        elif opcion == 5 and carga and proceso:
            infoXML.generarGrafica()
        else:
            print('\nRevisar que se haya cargado  y procesado correctamente el archivo XML...')
    except:
        separador()
        print('Dato no valido u opción incorrecta...')

