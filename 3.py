# Implementa un algoritmo en el que clasifique a una persona en niño, adolescente, adulto, adulto mayor

while True:
    edad = int(input("Digite su edad: "))
    if edad < 0:
        break
    if edad <= 13: 
        print("Usted es un niño")
    if edad > 13 and edad < 18:
        print("Usted es un adolescente")
    if edad >= 18 and edad < 65:
        print("Usted es un mayor de edad")
    if edad >= 65:
        print("Usted es un adulto mayor")
        
print("Usted ha salido del sistema")