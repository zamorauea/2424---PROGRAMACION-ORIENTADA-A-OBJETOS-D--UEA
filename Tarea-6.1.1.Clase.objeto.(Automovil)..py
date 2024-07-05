# Definición de la clase Automovil
class Automovil:
    # Método constructor para inicializar los atributos
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.encendido = False  # Estado inicial del automóvil apagado
        self.velocidad = 0  # Velocidad inicial del automóvil

    # Método para encender el automóvil
    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"El {self.marca} {self.modelo} del año {self.año} ha sido encendido.")
        else:
            print("El automóvil ya está encendido.")

    # Método para apagar el automóvil
    def apagar(self):
        if self.encendido:
            self.encendido = False
            self.velocidad = 0  # Al apagar el automóvil, la velocidad se establece a 0
            print(f"El {self.marca} {self.modelo} ha sido apagado.")
        else:
            print("El automóvil ya está apagado.")

    # Método para acelerar el automóvil
    def acelerar(self, cantidad):
        if self.encendido:
            self.velocidad += cantidad
            print(f"El {self.marca} {self.modelo} está acelerando a {self.velocidad} km/h.")
        else:
            print("No se puede acelerar porque el automóvil está apagado.")

    # Método para frenar el automóvil
    def frenar(self, cantidad):
        if self.velocidad >= cantidad:
            self.velocidad -= cantidad
            print(f"El {self.marca} {self.modelo} ha reducido su velocidad a {self.velocidad} km/h.")
        else:
            print("No se puede frenar más de lo que el automóvil está acelerando.")


# Creando una instancia de la clase Automovil
mi_auto = Automovil("Chevrolet", "Spark", 2022)

# Probando los métodos de la instancia
mi_auto.encender()
mi_auto.acelerar(50)
mi_auto.frenar(20)
mi_auto.acelerar(80)
mi_auto.frenar(100)
mi_auto.apagar()
