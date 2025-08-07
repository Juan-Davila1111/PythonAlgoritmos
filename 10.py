#Diseñe un algoritmo que calcule el precio de un producto después de aplicar un descuento
def calcular_precio_con_descuento(precio_original, descuento):
    precio_final = precio_original - (precio_original * descuento / 100)
    return print(f"El precio final del producto después de aplicar un descuento del {descuento}% es: {precio_final:.2f} unidades monetarias.")

precio = float(input("Digite el precio del producto: \n"))
descuento = float(input("Digite el % de descuento que le desea aplicar: \n"))
if descuento > 60:
    print("Jmmmm, pero conchudito")
calcular_precio_con_descuento(precio, descuento)