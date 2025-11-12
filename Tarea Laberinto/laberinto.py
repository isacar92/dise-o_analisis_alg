def leer_laberinto(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        total_filas = int(archivo.readline().strip())
        total_columnas = int(archivo.readline().strip())

        laberinto = []
        for _ in range(total_filas):
            linea = [celda.strip() for celda in archivo.readline().strip().split(',')]
            laberinto.append(linea)

    return laberinto, total_filas, total_columnas


def buscar_posicion(laberinto, simbolo):
    for fila in range(len(laberinto)):
        for columna in range(len(laberinto[0])):
            if laberinto[fila][columna] == simbolo:
                return (fila, columna)
    return None


def se_puede_mover(laberinto, visitado, fila, columna):
    filas = len(laberinto)
    columnas = len(laberinto[0])

    if fila < 0 or fila >= filas or columna < 0 or columna >= columnas:
        return False
    valor = laberinto[fila][columna]

    if valor in ('0', 'E', 'S') and not visitado[fila][columna]:
        return True

    return False


def resolver_laberinto(laberinto):
    posicion_entrada = buscar_posicion(laberinto, 'E')
    posicion_salida = buscar_posicion(laberinto, 'S')

    if posicion_entrada is None or posicion_salida is None:
        print("No se encontró entrada (E) o salida (S) en el laberinto.")
        return

    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    pila = [(posicion_entrada, [posicion_entrada])]
    visitado = [[False for _ in range(len(laberinto[0]))] for _ in range(len(laberinto))]

    while pila:
        posicion_actual, ruta_actual = pila.pop()
        fila_actual, columna_actual = posicion_actual

        if posicion_actual == posicion_salida:
            print("Ruta encontrada (de E a S):")
            for paso in ruta_actual:
                print(paso)
            return

        if not visitado[fila_actual][columna_actual]:
            visitado[fila_actual][columna_actual] = True

            for d in direcciones:
                nueva_fila = fila_actual + d[0]
                nueva_columna = columna_actual + d[1]

                if se_puede_mover(laberinto, visitado, nueva_fila, nueva_columna):
                    nueva_ruta = ruta_actual + [(nueva_fila, nueva_columna)]
                    pila.append(((nueva_fila, nueva_columna), nueva_ruta))

    print("No existe ninguna ruta desde E hasta S.")


if __name__ == "__main__":
    nombre_archivo = "entrada.txt"
    laberinto, filas, columnas = leer_laberinto(nombre_archivo)

    print("Laberinto:")
    for fila in laberinto:
        print(' '.join(fila))

    resolver_laberinto(laberinto)
