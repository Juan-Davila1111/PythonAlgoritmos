# Determine en un algoritmo que verifique si la temperatura de una 
# Habitación está dentro de un rango aceptable (25° y 20°)

while True:
    temperatura = int(input("Digite la temperatura a la que está su habitación: \n"))
    if temperatura > 25:
        print("Joa, que cule calor")
        continue
    if temperatura < 20:
        print("Te vas a salir resfriando")
        continue
    print("Estás bien de temperatura.")