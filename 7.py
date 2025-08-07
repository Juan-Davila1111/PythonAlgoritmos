def hacerMatriz (filas: int, columnas: int):
    # llena las columnas y las repite la cantidad de filas
    return [[0 for i in range(columnas)] for i in range (filas)]

def mostrarAsientos(matriz):
    #Recorre las filas
    for fila in matriz:
        #Imprime cada columna y la separa por un " "
        print(' '.join(str(columna) for columna in fila))

def hacientosDisponibles(matriz):
    for filas in matriz:
        if 0 in filas:
            return print("Enhorabuena, aún quedan asientos")
    return print("Ya no quedan más asientos")
    
def agendarAsiento(fila: int, columna: int, matriz):
    for filas in range(len(matriz)):
        for columnas in range(len(matriz[0])):
            if matriz[fila][columna] == 0:
                matriz[fila][columna] = 1
                return print(f"Asiento reservado en la posición {fila + 1},{columna + 1}.")
    print("Este asiento no está disponible.")

matriz = hacerMatriz(4, 4)
mostrarAsientos(matriz)
hacientosDisponibles(matriz)
agendarAsiento(3,2, matriz)
mostrarAsientos(matriz)