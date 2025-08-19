from math import gcd

class Racional:
    def __init__(self, numerador=0, denominador=1):
        if denominador == 0:
            raise ValueError("El denominador no puede ser cero.")
        self.numerador = numerador
        self.denominador = denominador
        self.simplificar()

    def simplificar(self):
        divisor = gcd(self.numerador, self.denominador)
        self.numerador //= divisor
        self.denominador //= divisor
        # Mantener el denominador positivo
        if self.denominador < 0:
            self.denominador = -self.denominador
            self.numerador = -self.numerador

    def leer(self):
        self.numerador = int(input("Numerador: "))
        self.denominador = int(input("Denominador: "))
        if self.denominador == 0:
            raise ValueError("Denominador no puede ser cero.")
        self.simplificar()

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def suma(self, otro):
        num = self.numerador * otro.denominador + otro.numerador * self.denominador
        den = self.denominador * otro.denominador
        return Racional(num, den)

    def resta(self, otro):
        num = self.numerador * otro.denominador - otro.numerador * self.denominador
        den = self.denominador * otro.denominador
        return Racional(num, den)

    def multiplicacion(self, otro):
        num = self.numerador * otro.numerador
        den = self.denominador * otro.denominador
        return Racional(num, den)

    def division(self, otro):
        if otro.numerador == 0:
            raise ZeroDivisionError("No se puede dividir por cero.")
        num = self.numerador * otro.denominador
        den = self.denominador * otro.numerador
        return Racional(num, den)
