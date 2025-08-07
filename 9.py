#Desarrolle un algoritmo que simule el lanzamiento de un dado
import random
import time

def lanzar_dado():
    print("Lanzando el dado...")
    time.sleep(2)  # Pausa de 2 segundos para simular el lanzamiento
    resultado = random.randint(1, 6)
    return print(f"El resultado del lanzamiento del dado es: {resultado}")

lanzar_dado()