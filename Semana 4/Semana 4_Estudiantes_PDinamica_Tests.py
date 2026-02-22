
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
    while True:
        entrada = input("Ingrese datos: ")
        datos = entrada.split()
        #test 1
        if len(datos) == 0:
            print("No se ingresaron datos, intentelo nuevamente")
            continue
        try: #Test 2, 3, 4 y 5 : datos en diferente orden, datos sin espacio, nota escrita como texto, nombre sin nota, nota sin nombre
            nombres = [datos[i] for i in range(0, len(datos), 2)]
            #test 6: cambia coma por punto en las notas
            notas = [float(datos[i+1].replace(',', '.')) for i in range(0, len(datos), 2)]
            #test 7:nota fuera del rango, negativa o mayor que 5
            error_nota = False
            for n in notas:
                if n < 0 or n > 5:
                    error_nota = True
                    
            if error_nota:
                print("Error: las notas deben estar entre 0 y 5.")
                continue
            break

        except (ValueError, IndexError):
            print("Error: datos inválidos. Asegurese de escribir: Nombre (espacio) Nota.")
            continue
    
    continuar = True
    while continuar:
        print("\nTotal estudiantes:" , len(nombres))
        inicio = int(input("Desde qué índice (0 a " + str(len(nombres)-1) + "): "))
        fin = int(input("Hasta qué índice (0 a " + str(len(nombres)-1) + "): "))
        #Test 8: El rango no es valido 
        # Test 9: el incio del rango es mayor al fin de este
        #test 10: el rango es igual a un solo estudiante
        if inicio < 0 or fin >= len(nombres) or inicio > fin:
                print("Los índices deben estar entre 0 y",len(nombres)-1," y el inicio no puede ser mayor al fin.\n")
                continue # Salta el cálculo y vuelve a pedir los índices
        
        #promedio con el rango dado
        prom_ref = calcular_promedio_memo(notas, inicio, fin)
        #filtrar con D&C
        aprobados = filtrar_estudiantes_DyC(nombres, notas, prom_ref, 0, len(notas)-1)
        
        print("Los estudiamtes que superan el promedio de", prom_ref, ":", aprobados)

        opcion = input("\n¿Desea probar otro rango? (si/no): ")
        if opcion.lower() != 'si':
            continuar = False

gestor_estudiantes_dinamico()