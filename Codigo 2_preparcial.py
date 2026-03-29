
def preOrder(root):
    # CASO BASE: Si el nodo es None, no hay nada que hacer
    if root is None:
        return
    
    # 1)visita la raiz: Imprimimos el valor asociado a la llave 'info'
    print(root['info'], end=" ")
    
    # 2)izquierda: Llamada recursiva usando la llave 'left'
    preOrder(root['left'])
    
    # 3. DERECHA: Llamada recursiva usando la llave 'right'
    preOrder(root['right'])


# Ejemplo de uso con los datos del preparcial
arbol = {
    'info': 1,
    'left': None,
    'right': {
        'info': 2,
        'left': None,
        'right': {
            'info': 5,
            'left': {
                'info': 3,
                'left': None,
                'right': {
                    'info': 4,
                    'left': None,
                    'right': None
                }
            },
            'right': {
                'info': 6,
                'left': None,
                'right': None
            }
        }
    }
}

#impimir prueba del recorrido preorden
print("Recorrido Preorden:")
preOrder(arbol)