opcion = 0

def separador():
    print("---------------------------------------------------------------")

while opcion!=6:
    separador()
    print("Menú principal")
    print("\t1. Cargar archivo")
    print("\t2. Procesar archivo")
    print("\t3. Escribir archivo salida")
    print("\t4. Mostrar datos del estudiante")
    print("\t5. Generar gráfica")
    print("\t6. Salida")
    opcion = int(input("\nIngrese el número de opción: "))
    if opcion==4:
        separador()
        print("José Ernesto Pajoc Raymundo")
        print("201115455")
        print('Introducción a la programación y computación 2, sección "A"')
        print("Ingenieria en Ciencias y Sistemas")
        print("4to. Semestre")
print("prueba")