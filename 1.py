# desarrolla un algoritmo que calcule la propina y el total a pagar en un restaurante, dado el monto de la cuenta y el porcentaje de propina

cuenta = int(input("Digite el valor de la cuenta: \n"))
porcentajePropina = int(input("Digite el % de la propina: \n"))
valorTotalCuenta = cuenta + cuenta * (porcentajePropina/100)
print(f"El valor total de la cuenta es: {valorTotalCuenta}")