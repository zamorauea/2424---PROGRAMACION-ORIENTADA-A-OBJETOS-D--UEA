# Clase base Animal
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        return "sonido genérico de animal"

# Subclase Perro, que hereda de Animal
class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau!"

# Subclase Gato, que hereda de Animal
class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau!"

# Creando instancias de las clases
mi_perro = Perro("Roky")
mi_gato = Gato("Mia")

# Usando métodos de las clases
print(f"{mi_perro.nombre} hace {mi_perro.hacer_sonido()}")
print(f"{mi_gato.nombre} hace {mi_gato.hacer_sonido()}")
