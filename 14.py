import random

canciones = ["Colombia tierra querida", "Hola", "Tú con él", "Que locura enamorarme de tí"]
cantidad = int(input("Digite la cantidad de canciones que tendrá su lista: \n"))
while cantidad > len(canciones):
    print("La cantidad que pedistes es mayor a la cantidad de canciones que tenemos.")
    cantidad = int(input("Digite la cantidad de canciones que tendrá su lista: \n"))

lista = random.sample(canciones, cantidad)
print("La lista de canciones es:")
for cancion in lista:
    print(cancion)