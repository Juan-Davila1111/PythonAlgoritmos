try:
    numeros = [1,2,3,4,5,6,7,8,9,10]
    index = int(input("Digite el índice que desea encontrar: "))
    print(numeros[index])
except IndexError:
    print("El índice está fuera del alcance de la longitud de la lista.")