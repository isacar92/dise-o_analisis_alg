#Emiliano Isacar Olmedo Sámano
import os
from itertools import combinations

def calcular_area(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2

def producto_cruzado(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

# Aqui se lee nuestro bonito archivo jijijijijijijij
directorio = os.path.dirname(os.path.abspath(__file__))
entrada = os.path.join(directorio, "campo.in")

lista_puntos = []
with open(entrada, "r") as archivo:
    for linea in archivo:
        px, py = map(int, linea.split())
        if px == -1 and py == -1:
            break
        lista_puntos.append((px, py))

lista_puntos.sort()

# Cálculo del casco
superior = []
for punto in lista_puntos:
    while len(superior) >= 2 and producto_cruzado(superior[-2], superior[-1], punto) <= 0:
        superior.pop()
    superior.append(punto)

inferior = []
for punto in reversed(lista_puntos):
    while len(inferior) >= 2 and producto_cruzado(inferior[-2], inferior[-1], punto) <= 0:
        inferior.pop()
    inferior.append(punto)

casco_convexo = superior[:-1] + inferior[:-1]

# en esrta parte se encuentra la busqueda del triángulo de mayor área
mayor_area = 0
triangulo_max = None

for p1, p2, p3 in combinations(casco_convexo, 3):
    area_actual = calcular_area(p1, p2, p3)
    if area_actual > mayor_area:
        mayor_area = area_actual
        triangulo_max = (p1, p2, p3)

print("Triángulo de mayor área encontrado:")
for x, y in triangulo_max:
    print(f"{x} {y}")

# aqui sale el .out
salida = os.path.join(directorio, "campo.out")
with open(salida, "w") as archivo_salida:
    for x, y in triangulo_max:
        archivo_salida.write(f"{x} {y}\n")
