#Desarrolla un algoritmo que ordene los numeros de una lista de menor a mayor
def ordenar_lista(lista_numeros):
    return sorted(lista_numeros)

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
        
numeros_ordenados = ordenar_lista(numeros)
print(f"Los números ordenados de menor a mayor son: {numeros_ordenados}")