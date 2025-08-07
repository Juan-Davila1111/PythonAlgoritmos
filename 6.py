# Diseña un algoritmo que me calcule el costo total de un viaje, sumando el costo del combustible, peaje y alojamiento

costo = 0
costoCombustible = float(input("Digite el costo de combustible: "))
costo += costoCombustible
costoPeaje = float(input("Digite el costo de peaje: "))
costo += costoPeaje
costoAlojamiento = float(input("Digite el costo de alojamiento: "))
costo += costoAlojamiento

print(f"""El viaje de acuerdo a lo ingresado costará:
    {costoPeaje} en costos de peaje
    {costoCombustible} en costos de combustible
    {costoAlojamiento} en costos de alojamiento
    Para un total de {costo:.2f}""")