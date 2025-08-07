# Desarrolla un algoritmo que reste los gastos de un presupuesto mensual
# y muestre el saldo restante
presupuesto = float(input("Ingrese el presupuesto mensual: "))
gastos = 0.0
while presupuesto > 0:
    gasto = float(input("Ingrese un gasto mensual: "))
    gastos += gasto
    saldo = presupuesto - gastos
    print(f"Saldo restante: {saldo:.2f}")
    if saldo <= 0:
        print("El saldo ha llegado a cero o es negativo. Fin del presupuesto.")
        break
# Fin del algoritmo