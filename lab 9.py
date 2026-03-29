
# normalizar evita duplicados como BODEGA y bodega

def normalizar(nombre):
    # Quita espacios y convierte a minúsculas para comparar sin errores
    return nombre.strip().lower()


# 1. Creamos la estructura del red_bodegas

def crear_red_bodegas():
    # Retorna un diccionario vacío {}. 
    # la 'llave' es la bodega y el 'valor' es su lista de conexiones.
    return {}


# 2. Agregar vértice (bodega)

def agregar_vertice(red_bodegas, v):
    
    v_norm = normalizar(v)

    # Verifica si la bodega ya existe (sin importar mayúsculas o espacios)
    for bodega in red_bodegas:
        if normalizar(bodega) == v_norm:
            print("La bodega ya existe")
            return

    # Se guarda el nombre original
    red_bodegas[v.strip()] = []
    print("Bodega agregada correctamente")


# 3. Conectar bodegas (arista)

def agregar_arista(red_bodegas, u, v):
    
    u_norm = normalizar(u)
    v_norm = normalizar(v)

    u_real = None
    v_real = None

    # Busca los nombres reales dentro del red_bodegas
    for bodega in red_bodegas:
        if normalizar(bodega) == u_norm:
            u_real = bodega
        if normalizar(bodega) == v_norm:
            v_real = bodega

    # Validación: ambas bodegas deben existir
    if u_real is None or v_real is None:
        print("Error: ambas bodegas deben existir")
        return
    
    # Evita duplicar conexión
    if v_real in red_bodegas[u_real]:
        print("La conexion ya existe")
        return
    
    # Conexion bidireccional
    red_bodegas[u_real].append(v_real)

    if u_real != v_real:
        red_bodegas[v_real].append(u_real)
    
    # Ordena conexiones
    for bodega in red_bodegas:
        red_bodegas[bodega].sort()
    
    print("Conexion agregada correctamente")


# 4. LISTA DE ADYACENCIA

def lista_ad(red_bodegas):
    if not red_bodegas:
        print("La red de bodegas esta vacia")
    else:
        print("\n LISTA DE CONEXIONES")
        for bodega in red_bodegas:
            print(bodega, ":", red_bodegas[bodega])


# 5. BFS (RUTAS MAS CORTAS)

def bfs(red_bodegas, inicio):

    inicio_norm = normalizar(inicio)

    inicio_real = None

    # Buscar la bodega real
    for bodega in red_bodegas:
        if normalizar(bodega) == inicio_norm:
            inicio_real = bodega

    if inicio_real is None:
        print("La bodega no existe en la red")
        return
    
    visitados = []
    cola = []
    
    # Guarda desde que bodega se llega a otra
    padres = {}
    
    cola.append(inicio_real)
    visitados.append(inicio_real)
    padres[inicio_real] = None
    
    print("\n RUTAS MAS CORTAS DESDE LA BODEGA ", inicio_real)
    
    while len(cola) > 0:

        actual = cola.pop(0)
        
        for vecino in red_bodegas[actual]:
            if vecino not in visitados:
                visitados.append(vecino)
                cola.append(vecino)
                padres[vecino] = actual
    
    # Mostrar rutas
    for bodega in visitados:
        ruta = []
        actual = bodega
        
        while actual is not None:
            ruta.append(actual)
            actual = padres[actual]
        
        ruta.reverse()
        
        print("Ruta hasta la bodega", bodega, ":", ruta)


# 6. DFS (RUTAS DE EXPLORACION)

def dfs(red_bodegas, inicio, ruta=None):

    inicio_norm = normalizar(inicio)

    inicio_real = None

    for bodega in red_bodegas:
        if normalizar(bodega) == inicio_norm:
            inicio_real = bodega

    if inicio_real is None:
        print("La bodega no existe en la red")
        return

    if ruta is None:
        ruta = []
        print("\n RUTAS DE EXPLORACION DFS ")
    
    ruta.append(inicio_real)
    
    es_final = True
    
    for vecino in red_bodegas[inicio_real]:
        
        if vecino not in ruta:
            es_final = False
            dfs(red_bodegas, vecino, ruta)
    
    if es_final:
        print("Ruta encontrada:", ruta)
    
    ruta.pop()


# 7. GRAFICO VISUAL

def graficar_red_bodegas_visual(red_bodegas):

    print("\n--- GRAFICO DE LA RED DE BODEGAS ---\n")

    if not red_bodegas:
        print("La red esta vacia")
        return

    inicio = list(red_bodegas.keys())[0]

    niveles = {inicio: 0}
    visitados = [inicio]
    cola = [inicio]

    while cola:
        actual = cola.pop(0)

        for vecino in red_bodegas[actual]:
            if vecino not in visitados:
                visitados.append(vecino)
                niveles[vecino] = niveles[actual] + 1
                cola.append(vecino)

    niveles_inv = {}

    for bodega in niveles:
        nivel = niveles[bodega]
        if nivel not in niveles_inv:
            niveles_inv[nivel] = []
        niveles_inv[nivel].append(bodega)

    for nivel in niveles_inv:
        niveles_inv[nivel].sort()

    posiciones = {}

    max_len = max(len(b) for b in red_bodegas)
    espacio_x = max_len + 6
    espacio_y = 3

    for nivel in niveles_inv:
        bodegas = niveles_inv[nivel]

        total = len(bodegas) * espacio_x
        inicio_x = 40 - total // 2

        for i, bodega in enumerate(bodegas):
            x = inicio_x + i * espacio_x
            y = nivel * espacio_y
            posiciones[bodega] = (y, x)

    filas = max(y for y, _ in posiciones.values()) + 4
    columnas = 100

    lienzo = [[" " for _ in range(columnas)] for _ in range(filas)]

    for bodega in posiciones:
        y, x = posiciones[bodega]
        texto = "[" + bodega + "]"
        inicio = x - len(texto)//2

        for i, ch in enumerate(texto):
            if 0 <= inicio+i < columnas:
                lienzo[y][inicio+i] = ch

    dibujadas = set()

    for u in red_bodegas:
        for v in red_bodegas[u]:

            if (v, u) in dibujadas:
                continue

            y1, x1 = posiciones[u]
            y2, x2 = posiciones[v]

            if y1 == y2:
                for x in range(min(x1, x2), max(x1, x2)):
                    if lienzo[y1][x] == " ":
                        lienzo[y1][x] = "-"

            else:
                for y in range(min(y1, y2)+1, max(y1, y2)):
                    if lienzo[y][x1] == " ":
                        lienzo[y][x1] = "|"

                y_con = max(y1, y2)
                for x in range(min(x1, x2), max(x1, x2)):
                    if lienzo[y_con][x] == " ":
                        lienzo[y_con][x] = "-"

            dibujadas.add((u, v))

    for fila in lienzo:
        print("".join(fila))


# 8. MENU PRINCIPAL

red_bodegas = crear_red_bodegas()

while True:
    
    print("\n---------- MENU PRINCIPAL ----------")
    print("1. Agregar bodega")
    print("2. Conectar bodegas")
    print("3. Ver conexiones")
    print("4. Ver rutas mas cortas (BFS)")
    print("5. Ver rutas de exploracion (DFS)")
    print("6. Ver grafico")
    print("7. Salir")
    
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "1":
        v = input("Ingrese la bodega: ")
        
        if v.strip() != "":
            agregar_vertice(red_bodegas, v)
        else:
            print("Error: no puede estar vacio")
    
    elif opcion == "2":
        u = input("Bodega origen: ")
        v = input("Bodega destino: ")
        
        if u.strip() != "" and v.strip() != "":
            agregar_arista(red_bodegas, u, v)
        else:
            print("Error: no puede estar vacio")
    
    elif opcion == "3":
        lista_ad(red_bodegas)
    
    elif opcion == "4":
        inicio = input("Bodega inicial: ")
        bfs(red_bodegas, inicio)
    
    elif opcion == "5":
        inicio = input("Bodega inicial: ")
        dfs(red_bodegas, inicio)
    
    elif opcion == "6":
        graficar_red_bodegas_visual(red_bodegas)

    elif opcion == "7":
        print("Saliendo del sistema...")
        break
    
    else:
        print("Opcion invalida")
