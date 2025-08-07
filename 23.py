#Implementa un algiritmo que convierta de temperatura Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32
while True:
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"{celsius} grados Celsius son {fahrenheit:.2f} grados Fahrenheit.")