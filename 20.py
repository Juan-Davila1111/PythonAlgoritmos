#Desarrolle un algoritmo que calcule el area de un círculo

import math
def area_circulo(radio):
    return math.pi * (radio ** 2)
while True:
    radio = float(input("Ingrese el radio del círculo: "))
    area = area_circulo(radio)
    print(f"El área del círculo con radio {radio} es: {area:.2f}")
