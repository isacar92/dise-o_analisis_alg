def leer_puntos(nombre):
    puntos = []
    with open(nombre, "r") as f:
        for linea in f:
            x, y = map(int, linea.split())
            if x == -1 and y == -1:
                break
            puntos.append((x, y))
    return puntos


def area(p1, p2, p3):
    (x1, y1), (x2, y2), (x3, y3) = p1, p2, p3
    return abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2


def mayor_triangulo_bruteforce(puntos):
    n = len(puntos)
    max_area = 0
    mejor = None

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                a = area(puntos[i], puntos[j], puntos[k])
                if a > max_area:
                    max_area = a
                    mejor = (puntos[i], puntos[j], puntos[k])

    return mejor
puntos = leer_puntos("campo.in")

p1, p2, p3 = mayor_triangulo_bruteforce(puntos)

with open("campo.out", "w") as f:
    f.write(f"{p1[0]} {p1[1]}\n")
    f.write(f"{p2[0]} {p2[1]}\n")
    f.write(f"{p3[0]} {p3[1]}\n")

print("Listo, se generó campo.out")