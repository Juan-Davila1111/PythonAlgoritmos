try:
    num1 = int(input("Digite el numerador: "))
    num2 = int(input("Digite el denominaor: "))
    
    division = num1 / num2
except ZeroDivisionError:
    print("El denominador no puede ser 0.")