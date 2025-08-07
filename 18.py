def tablaMultiplicacion(num):
    for i in range (10):
        print(f"{num} * {i} = {num * i}")
        
while True:
    numero = int(input("Digite el número del cuál desea saber la tabla: "))
    tablaMultiplicacion(numero)