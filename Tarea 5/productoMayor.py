#Número alto
def producto_mas_alto(lista):
    mayor = float('-inf')
    num1 = num2 = 0

    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            producto = lista[i] * lista[j]

            if producto > mayor:
                mayor = producto
                num1, num2 = lista[i], lista[j]

    print("El producto más alto es", mayor, "obtenido al multiplicar", num1, "y", num2)

producto_mas_alto([-9, 3, 5, -2, 9, -7, 4, 8, 6])