#Desarrolle un algoritmo que saque el promedio de una lista de números

def calcular_promedio(lista_numeros):
    if not lista_numeros:
        return 0
    return sum(lista_numeros) / len(lista_numeros)

# Ejemplo de uso
numeros = []
while True:
    entrada = input("Ingrese un número (o 'fin' para terminar): ")
    if entrada.lower() == 'fin':
        break
    try:
        numero = float(entrada)
        numeros.append(numero)
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
        
promedio = calcular_promedio(numeros)
print(f"El promedio de los números ingresados es: {promedio:.2f}")