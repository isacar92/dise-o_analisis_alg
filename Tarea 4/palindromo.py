def esPalindromo(cadena):
    if len(cadena) <= 1:
        return "es palindromo"

        
    if cadena[0] != cadena[-1]:
        return "no es palindromo"
        
    return esPalindromo(cadena[1:-1])  


palabra1 = "reconocer"
palabra2 = "hola"

print(palabra1, "->", esPalindromo(palabra1))
print(palabra2, "->", esPalindromo(palabra2))  
