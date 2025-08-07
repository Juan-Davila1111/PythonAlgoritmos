# #Crea un algoritmo que calcule el pago mensual de un préstamo, dado el monto
# la tasa de interés anual y el número de meses

def calcular_pago_mensual(monto, tasa_interes_anual, meses):
    tasa_interes_mensual = tasa_interes_anual / 12 / 100
    pago_mensual = (monto * tasa_interes_mensual) / (1 - (1 + tasa_interes_mensual) ** -meses)
    return print(f"""Señor usuario, el pago mensual de su préstamo es: {pago_mensual:.2f} unidades monetarias
ya que el monto del préstamo es {monto} unidades monetarias,
la tasa de interés anual es {tasa_interes_anual}% y el número de meses es {meses}.
"""
)
# Ejemplo de uso
monto = float(input("Digite el monto del prestamo: "))
tasa_interes_anual = float(input("Digite la tasa de interes anual del préstamo: ")) 
meses = int(input("Digite el número de meses del préstamo: "))
calcular_pago_mensual(monto, tasa_interes_anual, meses)