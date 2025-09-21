def eliminarNumeroDeEnmedio(pila, medio, actual=0):
    if actual == medio:
        pila.pop()
        return

    tope = pila.pop()

    eliminarNumeroDeEnmedio(pila, medio, actual + 1)

    pila.append(tope)


pila = [1, 2, 3, 4, 5]   
medio = (len(pila)-1)// 2

print("Pila original:", pila)
eliminarNumeroDeEnmedio(pila, medio)
print("Pila sin el número de en medio :", pila)
