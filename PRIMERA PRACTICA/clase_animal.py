# Creamos una clase animal
# Con los siguientes atributos --nombre --edad --imprime sonido
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def emite_sonido(self):
        print("Este animal realiza un sonido")

