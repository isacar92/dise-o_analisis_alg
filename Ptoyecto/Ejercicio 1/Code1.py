#Emiliano Isacar Olmedo Sámano
#Holi maestro Cabrera, este es la resolucion del ejercicio 1

def hay_camino(filas, columnas):
    visitados = set()

    def explorar(i, j):
        if i < 0 or i >= filas or j < 0 or j >= columnas:
            return False
        if (i, j) in visitados:
            return False
        if i == filas - 1 and j == columnas - 1:
            return True

        visitados.add((i, j))

        # Aqui ise los movimientos permitidos
        derecha = explorar(i, j + 3) #esto es el movimiento horizontal :3
        abajo = explorar(i + 2, j) #esto es el movimiento vertical

        if derecha or abajo:
            return True
        
        visitados.remove((i, j))
        return False

    return explorar(0, 0)


resultado = hay_camino(6,9)

if resultado:
    print("Existe al menos un posible camino")
else:
    print("Desafortunadamente no existe un posible camino")
