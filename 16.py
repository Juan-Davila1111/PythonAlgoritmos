#Diseñe un algiritmo que calcule el tieempo que se tarda en viajar de un lugar a otro
#dada la velocidad promedio.

velocidad = float(input("Ingrese la velocidad promedio en km/h: "))
distancia = float(input("Ingrese la distancia a recorrer en km: "))
tiempo = distancia / velocidad
print(f"El tiempo estimado de viaje es de {tiempo:.2f} horas.")