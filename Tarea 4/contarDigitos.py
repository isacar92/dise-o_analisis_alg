def contarDigitos(numeroEntero):
    if numeroEntero == 0:   
        return 0
    else:
        return  1 + contarDigitos(numeroEntero//10)


numeroEntero = 123456
resultado = contarDigitos(numeroEntero)
print("Cantidad de digitos: ", resultado)
