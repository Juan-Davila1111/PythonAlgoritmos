# Desarrolla un algoritmo que me permita agregar, eliminar y mostrar una lista de compras.
productos = []
def agregarProducto():
    productoNombre = input("Digite el nombre del producto: ")
    productoCantidad = int(input("Digite la cantidad de productos: "))
    productoPrecio = float(input("Digite el valor del producto"))
        
    infoProducto = {
        productoNombre : productoNombre,
        productoCantidad : productoCantidad,
        productoPrecio : productoCantidad * productoPrecio
    }
    
    productos.append(infoProducto)

def eliminarProducto():
    productoNombre = input("Digite el nombre del producto que desea eliminar: ")
    if infoProducto[productoNombre] not in productos:
        print("El producto no se ha encontrado")
    
    #Encontrar el producto en la lista y eliminarlo
    for producto in productos:
        if productoNombre in producto:
            productos.remove(producto)
            print(f"Producto {productoNombre} eliminado.")
            break
    else:
        print(f"Producto {productoNombre} no encontrado en la lista.")

def mostrarProductos():
    for producto in productos:
        print(f"""Nombre del producto {producto[productoNombre]}
        Cantidad de productos {producto[productoCantidad]}
        Precio producto {producto[productoPrecio]}""")

while True:
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Mostrar lista de compras")
    print("4. Salir")
    
    opcion = int(input("Seleccione una opción: "))
    
    if opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4:
        print("Opción no válida. Intente de nuevo.")
        continue
    if opcion == 4:
        print("Saliendo del sistema...")
        break
    
    if opcion == 1:
        agregarProducto()
        
    if opcion == 2:
        eliminarProducto()
        
    if opcion == 3:
        mostrarProductos()
print("Usted ha salido del sistema")