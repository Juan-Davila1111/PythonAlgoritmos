#Escribe un algoritmo que verifique si un elemento está en una lista
def elemento_en_lista(elemento, lista):
    return elemento in lista

# Ejemplo de uso
lista = [1, 2, 3, 4, 5]
while True:
    elemento = int(input("Ingrese un número para verificar si está en la lista: "))
    if elemento_en_lista(elemento, lista):
        print(f"{elemento} está en la lista.")
    else:
        print(f"{elemento} no está en la lista.")