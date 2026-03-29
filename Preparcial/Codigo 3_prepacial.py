
def calcular_movimientos_posibles(m, n):
    """Genera el conjunto de saltos únicos evitando duplicados si M=N o M=0"""
    saltos = set([
        (m, n), (m, -n), (-m, n), (-m, -n),
        (n, m), (n, -m), (-n, m), (-n, -m)
    ])
    return saltos

def es_posicion_valida(r, c, entorno):
    """Verifica si una coordenada esta dentro del mapa y no es agua"""
    dentro_limites = 0 <= r < entorno["limite_filas"] and 0 <= c < entorno["limite_columnas"]
    if dentro_limites:
        # El agua se representa como un set de tuplas para busqueda rapida
        return (r, c) not in entorno["coordenadas_agua"]
    return False

def analizar_terreno(r, c, m, n, lista_aguas):
    # Inicializamos el estado del problema en un diccionario
    entorno_guerra = {
        "limite_filas": r,
        "limite_columnas": c,
        "coordenadas_agua": set(lista_aguas),
        "nodos_visitados": set(),
        "movimientos_ley_caballero": calcular_movimientos_posibles(m, n)
    }

    conteo_pares = 0
    conteo_impares = 0

    # Cola para exploracion (BFS) empezando en el origen
    itinerario_busqueda = [(0, 0)]
    entorno_guerra["nodos_visitados"].add((0, 0))

    # Proceso de exploracion
    indice_actual = 0
    while indice_actual < len(itinerario_busqueda):
        f_actual, c_actual = itinerario_busqueda[indice_actual]
        indice_actual += 1

        # Para el cuadro actual, contamos sus conexiones validas (ki)
        conexiones_validas = 0
        for df, dc in entorno_guerra["movimientos_ley_caballero"]:
            nf, nc = f_actual + df, c_actual + dc

            if es_posicion_valida(nf, nc, entorno_guerra):
                conexiones_validas += 1
                
                # Si es un cuadro nuevo, lo agendamos para visitar
                if (nf, nc) not in entorno_guerra["nodos_visitados"]:
                    entorno_guerra["nodos_visitados"].add((nf, nc))
                    itinerario_busqueda.append((nf, nc))

        # Clasificamos el cuadro segun la paridad de sus conexiones
        if conexiones_validas % 2 == 0:
            conteo_pares += 1
        else:
            conteo_impares += 1

    return conteo_pares, conteo_impares


# Ejemplo de uso con los datos del preparcial
# Caso 1: 3x3, M=2, N=1, Sin agua
pares1, impares1 = analizar_terreno(3, 3, 2, 1, [])
print("Caso 1 -> Even:", pares1, "Odd:", impares1) # Resultado esperado: 5 0

# Caso 2: 4x4, M=1, N=2, Aguas en (3,3) y (1,1)
aguas_caso2 = [(3, 3), (1, 1)]
pares2, impares2 = analizar_terreno(4, 4, 1, 2, aguas_caso2)
print("Caso 2 -> Even:", pares2, "Odd:", impares2) # Resultado esperado: 4 10
