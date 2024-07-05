class RegistroLlamadas:
    def __init__(self):
        self.llamadas = []

    def registrar_llamada(self, numero, duracion):
        self.llamadas.append({
            'numero': numero,
            'duracion': duracion
        })

    def mostrar_llamadas(self):
        if not self.llamadas:
            print("No hay llamadas registradas.")
        else:
            print("Registro de llamadas:")
            for llamada in self.llamadas:
                print(f"Número: {llamada['numero']}, Duración: {llamada['duracion']} segundos")

# Creando un objeto de la clase RegistroLlamadas
registro = RegistroLlamadas()

# Registrando algunas llamadas
registro.registrar_llamada("0999333992", 90)
registro.registrar_llamada("0988855441", 120)
registro.registrar_llamada("0972435679", 70)

# Mostrando el registro de llamadas
registro.mostrar_llamadas()

