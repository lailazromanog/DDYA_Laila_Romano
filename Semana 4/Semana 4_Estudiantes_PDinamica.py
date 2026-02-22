
memo = {}

def calcular_promedio_memo(notas, inicio, fin):
    # Creamos una llave única para el rango
    rango = (inicio, fin)
    
    # Si el rango ya fue calculado antes, lo retornamos
    if rango in memo:
        return memo[rango]
    # Si no está en memo, lo calculamos
    
    notas_rango = notas[inicio : fin + 1]
    promedio = sum(notas_rango) / len(notas_rango)
    # Guardamos el resultado para el futuro
    memo[rango] = promedio
    return promedio

def filtrar_estudiantes_DyC(nombres, notas, promedio, low, high):
    # Caso base: un solo estudiante
    if low == high:
        if notas[low] >= promedio:
            return [nombres[low]]
        else:
            return []
    mid = (low + high) // 2
    
    izq = filtrar_estudiantes_DyC(nombres, notas, promedio, low, mid)
    der = filtrar_estudiantes_DyC(nombres, notas, promedio, mid + 1, high)
    
    return izq + der

def gestor_estudiantes_dinamico():
    entrada = input("Ingrese datos: ")
    datos = entrada.split()
    
    nombres = [datos[i] for i in range(0, len(datos), 2)]
    notas = [float(datos[i+1]) for i in range(0, len(datos), 2)]
    
    continuar = True
    while continuar:
        print("\nTotal estudiantes:" , len(nombres))
        inicio = int(input("Desde qué índice (0 a " + str(len(nombres)-1) + "): "))
        fin = int(input("Hasta qué índice (0 a " + str(len(nombres)-1) + "): "))
        #promedio con el rango dado
        prom_ref = calcular_promedio_memo(notas, inicio, fin)
        #filtrar con D&C
        aprobados = filtrar_estudiantes_DyC(nombres, notas, prom_ref, 0, len(notas)-1)
        
        print("Superan el promedio de", prom_ref, ":", aprobados)

        opcion = input("\n¿Desea probar otro rango? (si/no): ")
        if opcion.lower() != 'si':
            continuar = False

gestor_estudiantes_dinamico()