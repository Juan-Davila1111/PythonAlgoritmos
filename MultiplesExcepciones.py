try:
    archivo = open('archivo','r')
    contenido = archivo.read()
    resultado = 30 / 0
except FileNotFoundError:
    print("Error: El archivo no ha sido encontrado.")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
finally:
    print("Final del algoritmo.")