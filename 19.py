#Implementa un algoritmo que encuentre los elementos comunes entre dos listas

def elementos_comunes(lista1, lista2):
    comunes = []
    for elemento in lista1:
        if elemento in lista2:
            comunes.append(elemento)
    return comunes

# Ejemplo de uso
lista_a = [1, 2, 3, 4, 5]
lista_b = [4, 5, 6, 7, 8]
resultado = elementos_comunes(lista_a, lista_b)
print("Elementos comunes:", resultado)