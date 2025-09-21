def suma(lista):
    if lista == []:   
        print("Lista vacía")
        return 0
    else:
        print("Suma", lista[0], "con los numeros que faltan", lista[1:])
        return lista[0] + suma(lista[1:])

numeros = [10, 20, 30]
resultado = suma(numeros)
print("Resultado final de la suma:", resultado)
