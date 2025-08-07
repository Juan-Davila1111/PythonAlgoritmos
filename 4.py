# Escriba un algoritmo que determine el IMC
while True: 
    peso = float(input("Digite su peso en kg: "))
    altura = float(input("Digite su altura en metros: "))
    if peso <= 0 or altura <= 0:
        break
    imc = peso / (altura ** 2)
    print(f"Su IMC es: {imc:.2f}")
print("Usted ha salido del sistema")