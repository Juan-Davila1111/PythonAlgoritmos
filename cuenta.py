class Cuenta:
    _numero_cuenta_generado = 1000000000  # para generar números de cuenta automáticamente
    
    def __init__(self, dni=None, saldo=0.0, interes_anual=0.0):
        self.numero_cuenta = Cuenta._numero_cuenta_generado
        Cuenta._numero_cuenta_generado += 1
        self.dni = dni
        self.saldo = saldo
        self.interes_anual = interes_anual

    # Accesores
    def get_numero_cuenta(self):
        return self.numero_cuenta

    def get_dni(self):
        return self.dni

    def set_dni(self, dni):
        self.dni = dni

    def get_saldo(self):
        return self.saldo

    def set_saldo(self, saldo):
        self.saldo = saldo

    def get_interes_anual(self):
        return self.interes_anual

    def set_interes_anual(self, interes):
        self.interes_anual = interes

    def actualizar_saldo(self):
        interes_diario = self.interes_anual / 365 / 100  # porcentaje a decimal
        self.saldo += self.saldo * interes_diario

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
        else:
            print("Cantidad a ingresar debe ser positiva.")

    def retirar(self, cantidad):
        if cantidad > 0:
            if self.saldo >= cantidad:
                self.saldo -= cantidad
            else:
                print("Saldo insuficiente.")
        else:
            print("Cantidad a retirar debe ser positiva.")

    def mostrar_datos(self):
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"DNI: {self.dni}")
        print(f"Saldo actual: {self.saldo:.2f}")
        print(f"Interés anual: {self.interes_anual:.2f}%")
