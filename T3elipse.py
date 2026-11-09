import math
import random

a = int(input("a (elipse): "))
b = int(input("b (elipse): "))
c = int(input("c (hiperbola): "))
d = int(input("d (hiperbola): "))
n = int(input("Cantidad de puntos: "))

pts = [(random.uniform(-a, a), random.uniform(-b, b)) for _ in range(n)]

en_el = [(x, y) for x, y in pts if x**2 / a**2 + y**2 / b**2 <= 1]
en_in = [(x, y) for x, y in en_el if x**2 / c**2 - y**2 / d**2 >= 1]

pe = len(en_el)
pi_ = len(en_in)

ae = math.pi * a * b
ai = ae * pi_ / pe

print("\n--- Resultados ---")
print("Puntos dentro de la elipse:", pe)
print("Puntos en la interseccion hiperbola-elipse:", pi_)
print("Area de la elipse:", round(ae))
print("Area aprox. de la interseccion:", round(ai))