# Crea un algoritmo que convierta dólares a euros
dolar = 1.16
euro = 0.86

while True:
    decision = int(input("Digite 1 si desea convertir de dolar a euro, o 2 si quieres convertir de euro a dolar: "))
    if (decision != 1 and decision != 2):
        break
    moneda = float(input("Digite el monto: "))
    if(decision == 1):
        moneda = moneda * ( 1 / dolar)

    if(decision == 2):
        moneda = moneda * ( 1 / euro)
    
    print(f"El resultado es {moneda}")

print("Saliste del programa")