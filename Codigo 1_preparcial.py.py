
def procesar_cola(consultas):
    pila_entrada = []
    pila_salida = []

    # Funciones basicas de Pila
    def push(pila, elemento):
        pila.append(elemento)

    def pop(pila):
        if len(pila) > 0:
            return pila.pop()
        return None

    # Procesamos cada comando de la lista
    for query in consultas:
        partes = query.split()
        tipo = partes[0]

        if tipo == "1":
            # ENQUEUE: Agregar al final
            valor = partes[1]
            push(pila_entrada, valor)
        else:
            # Si la pila de salida esta vacia, movemos todo de entrada a salida
            # Esto invierte el orden para cumplir el principio FIFO
            if len(pila_salida) == 0:
                while len(pila_entrada) > 0:
                    dato_temp = pop(pila_entrada)
                    push(pila_salida, dato_temp)
            
            if tipo == "2":
                # DEQUEUE: Eliminar el frente
                pop(pila_salida)
            elif tipo == "3":
                # PRINT: Mostrar el frente
                if len(pila_salida) > 0:
                    print(pila_salida[-1])


# Ejemplo de uso con los datos del preparcial
print("\nEjecutando Ejemplo 2:")
ejemplo2 = ["1 42", "1 14", "2", "1 28", "3"]
procesar_cola(ejemplo2)