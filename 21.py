#Desarrolle un algoritmo que me permita saber si un número es primo o no

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True
while True:
    numero = int(input("Ingrese un número para verificar si es primo: "))
    if es_primo(numero):
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")