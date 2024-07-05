# Clase base DispositivoElectronico
class DispositivoElectronico:
    def encender(self):
        return "Dispositivo electrónico prendido"

# Subclase Telefono, que hereda de DispositivoElectronico
class Telefono(DispositivoElectronico):
    def encender(self):
        return "Teléfono iniciado y listo para usar"

# Subclase Computadora, que hereda de DispositivoElectronico
class Computadora(DispositivoElectronico):
    def encender(self):
        return "Computadora arrancando, bienvenido"

# Subclase Tablet, que hereda de DispositivoElectronico
class Tablet(DispositivoElectronico):
    def encender(self):
        return "Tablet encendida, listo para trabajar o jugar"

# Creando objetos de las clases derivadas
mi_telefono = Telefono()
mi_computadora = Computadora()
mi_tablet = Tablet()

# Utilizando el método sobrescrito
print(mi_telefono.encender())
print(mi_computadora.encender())
print(mi_tablet.encender())
