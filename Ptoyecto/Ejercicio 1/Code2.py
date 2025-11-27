
#Emiliano Isacar Olmedo Sámano
#Holi maestro Cabrera, este es la resolucion del ejercicio 1 pero ek inicio B

def buscar_rutas(filas, columnas):
    visitados = {}
    rutas = []

    def explorar(x, y, camino):
        # Si se sale del tablero :c
        if x < 0 or x >= filas or y < 0 or y >= columnas:
            return
        
        # Si ya pasamos por ahí
        if (x, y) in visitados:
            return
        
        # en esta se marca los caminos
        camino.append((x, y))
        visitados[(x, y)] = True

       
        if x == filas - 1 and y == columnas - 1:
            rutas.append(camino[:])
        else:
            # Aqi ise los miviemeintos
            explorar(x, y + 3, camino)
            explorar(x + 2, y, camino)

        # Esto hace q el backtrracking funcione :3
        camino.pop()
        del visitados[(x, y)]

   
    explorar(0, 0, [])
    return rutas


resultado = buscar_rutas(3,5)

print("Total de caminos encontrados:", len(resultado))
contador = 1
for ruta in resultado:
    print("Camino", contador)
    for paso in ruta:
        print(paso)
    print()
    contador += 1
