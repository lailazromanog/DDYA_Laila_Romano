#Usando dividir y cosquistar 
def filtrar_estudiantes_DyC(nombres, notas, promedio, low, high):
#caso base: solo hay un estudiante
    if low == high:
        if notas[low] >= promedio:
            return [nombres[low]]
        else:
            return []
#Se parte a la mitad los datos ingresados
    mid = (low + high) // 2
#Llama recursivamente para cada mitad de los datos de estudiantes
    izq = filtrar_estudiantes_DyC(nombres, notas, promedio, low, mid)
    der = filtrar_estudiantes_DyC(nombres, notas, promedio, mid + 1, high)
#Une los datos de la derecha y la izquierda 
    return izq + der

def gestor_de_estudiantes():
    n = input("Ingrese los datos de los estudiantes: ")
    datos = n.split()
    nombres = []
    notas = []
    for i in range(0, len(datos), 2):
        nombres.append(datos[i])
        notas.append(float(datos[i + 1]))

    if len(notas) > 0:
        prom_general = sum(notas) / len(notas)
#llamo a mi función que aplica dividir y conquistar, para filtrar
        estudiantes_aprobados = filtrar_estudiantes_DyC(nombres, notas, prom_general, 0, len(notas) - 1)
        print("Los estudiantes que están por encima del promedio y aprueban son:")
        for nombre in estudiantes_aprobados:
            print(nombre)
    else:
        print("No se ingresaron datos.")
    print("Finalizamos, vuelva pronto")
gestor_de_estudiantes()
