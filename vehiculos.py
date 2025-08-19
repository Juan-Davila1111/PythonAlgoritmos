class Motor:
    def __init__(self):
        self.encendido = False

    def arrancar(self):
        if not self.encendido:
            self.encendido = True
            print("Motor arrancado.")
        else:
            print("Motor ya está encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print("Motor apagado.")
        else:
            print("Motor ya está apagado.")

class Rueda:
    def __init__(self):
        self.inflada = False

    def inflar(self):
        if not self.inflada:
            self.inflada = True
            print("Rueda inflada.")
        else:
            print("Rueda ya está inflada.")

    def desinflar(self):
        if self.inflada:
            self.inflada = False
            print("Rueda desinflada.")
        else:
            print("Rueda ya está desinflada.")

class Ventana:
    def __init__(self):
        self.abierta = False

    def abrir(self):
        if not self.abierta:
            self.abierta = True
            print("Ventana abierta.")
        else:
            print("Ventana ya está abierta.")

    def cerrar(self):
        if self.abierta:
            self.abierta = False
            print("Ventana cerrada.")
        else:
            print("Ventana ya está cerrada.")

class Puerta:
    def __init__(self):
        self.ventana = Ventana()
        self.abierta = False

    def abrir_puerta(self):
        if not self.abierta:
            self.abierta = True
            print("Puerta abierta.")
        else:
            print("Puerta ya está abierta.")

    def cerrar_puerta(self):
        if self.abierta:
            self.abierta = False
            print("Puerta cerrada.")
        else:
            print("Puerta ya está cerrada.")

class Coche:
    def __init__(self):
        self.motor = Motor()
        self.ruedas = [Rueda() for _ in range(4)]
        self.puertas = [Puerta() for _ in range(2)]

    def arrancar_motor(self):
        self.motor.arrancar()

    def apagar_motor(self):
        self.motor.apagar()

    def inflar_ruedas(self):
        for i, rueda in enumerate(self.ruedas, 1):
            print(f"Inflando rueda {i}...")
            rueda.inflar()

    def desinflar_ruedas(self):
        for i, rueda in enumerate(self.ruedas, 1):
            print(f"Desinflando rueda {i}...")
            rueda.desinflar()

    def abrir_puerta(self, indice):
        if 0 <= indice < len(self.puertas):
            self.puertas[indice].abrir_puerta()
        else:
            print("Índice de puerta inválido.")

    def cerrar_puerta(self, indice):
        if 0 <= indice < len(self.puertas):
            self.puertas[indice].cerrar_puerta()
        else:
            print("Índice de puerta inválido.")
